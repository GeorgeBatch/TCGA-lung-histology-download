# TCGA Lung Dataset

This repository contains the instructions of how to download the **diagnostic** slides for the lung portion of the TCGA dataset. It will require ~800GB of space.

TCGA lung also has tissue slides which are were not diagnostic. Experimental strategy can be Tissue Slide (non-diagnostic) or/and Diagnostic Slide.


**Important note**
  * Patient ID is the first 12 characters of the slide name, e.g. `TCGA-50-5066`
  * Case ID is the first 15 characters of the slide name, e.g. `TCGA-50-5066-01` or `TCGA-50-5066-02`
  * Slide name, e.g. `TCGA-50-5066-01Z-00-DX1.e161df31-84a4-40a4-a6a2-748b60820f77` contains the slide name `TCGA-50-5066-01Z-00-DX1` and some uid `e161df31-84a4-40a4-a6a2-748b60820f77`; all slide names in the downloaded dataset are unique and so are the uid's so that there is a one-to-one mapping between the slide names and the uid's.

Source: https://docs.gdc.cancer.gov/Encyclopedia/pages/TCGA_Barcode/#creating-barcodes

This explains why the web page refers to **478 cases for LUAD** and 478 cases for LUSC, while the manifest files contain **479 cases for LUAD** and 478 cases for LUSC.
The web page really refers to the patients, while the manifest files refer to the cases.

Patient `TCGA-50-5066` has 2 cases for LUAD. The case IDs are:
  * `TCGA-50-5066-01` with diagnostic slide: `TCGA-50-5066-01Z-00-DX1`
  * `TCGA-50-5066-02` with diagnostic slide: `TCGA-50-5066-02Z-00-DX1`

Every other patient has only 1 case per patient.

## Instructions for Downloading the Dataset

0. Make sure you have enough disk space: ~800**GB**.
1. Download the `gdc-client` Data Transfer Tool binaries from
https://gdc.cancer.gov/access-data/gdc-data-transfer-tool and add it to your
PATH or into `/usr/local/bin` if you have this directory (it's usually already
added to the PATH). I did not have any problems with it on Linux, however on Apple
devices you can run into "MacOS cannot verify app is free from malware" which can be
solved as described here:
https://gadgetstouse.com/blog/2021/04/08/fix-macos-cannot-verify-app-is-free-from-malware/
2. Clone this repository and `cd` into it.

If you want to make sure that the manifests have not changed, download new ones from TCGA data portal and check them. Example of checking the versions from 2023-10-03 vs 2021-11-03. The manifests have not changed.
```
cd tcga-download

for file in gdc_manifest.2023-10-03-TCGA-LUSC.txt gdc_manifest.2023-10-03-TCGA-LUAD.txt gdc_manifest.2021-11-03-TCGA-LUSC.txt gdc_manifest.2021-11-03-TCGA-LUAD.txt; do
    sorted_file="${file%.txt}-sorted.txt"
    echo -e "id\tfilename\tmd5\tsize\tstate" > "$sorted_file"
    tail -n +2 "$file" | sort -k2,2 >> "$sorted_file"
done

diff gdc_manifest.2023-10-03-TCGA-LUAD-sorted.txt gdc_manifest.2021-11-03-TCGA-LUAD-sorted.txt
diff gdc_manifest.2023-10-03-TCGA-LUSC-sorted.txt gdc_manifest.2021-11-03-TCGA-LUSC-sorted.txt

cd ..
```

3. Create `./WSI/LUSC/` and `./WSI/LUAD` folders.
4. If you choose to change the folder structure, make changes to
   1. `./tcga-download/config-LUSC.dtt`
   2. `./tcga-download/config-LUAD.dtt`
5. Run:

```shell
bash ./0-download-LUSC-and-LUAD.sh
```
to download the files. It will take a
while. Restarting the download is not advisable. I am not sure, but I think the
manifest file will need to be modified: already downloaded files fill need to be
excluded. See: https://docs.gdc.cancer.gov/Data_Transfer_Tool/Users_Guide/Data_Download_and_Upload/#resuming-a-failed-download









**Tip:** I used `tmux` for the process to continue on a remote surver after I
closed the connection. See this
[how-to](https://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session)
on StackExchange.

6. Check that the downloaded slides were not currupted during the download:

```shell
md5sum ./WSI/*/*.svs > downloaded_md5sum_hashes.txt
```

The hashes should match the ones in `./tcga_download/` manifest files for LUAD and LUSC.

The code to parse the manifest files and `downloaded_md5sum_hashes.txt` and check the matches is in [2-check-names.ipynb](2-check-names.ipynb).

If you already have a file with md5 checksums, you can use a trick shown here: https://askubuntu.com/questions/318530/generate-md5-checksum-for-all-files-in-a-directory

## Contents

* [./tcga-download/](./tcga-download/) folder was originally copied from https://github.com/binli123/dsmil-wsi/tree/master/tcga-download.
Some names present in the manifest files were not available for download with the
`gdc-client`. So new manifest files were downloaded from these web pages on 
on 03/11/2021 (date is in the names). The manifest files are:
  * TCGA-LUAD
    * [manifest on TCGA portal](https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-LUAD%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22files.experimental_strategy%22%2C%22value%22%3A%5B%22Diagnostic%20Slide%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D&searchTableTab=files)
    * [downloaded manifest from 2021-11-03](./tcga-download/gdc_manifest.2021-11-03-TCGA-LUAD.txt): 541 slides from 478 patients with 479 cases
  * TCGA-LUSC
    * [manifest on TCGA portal](https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-LUSC%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22files.experimental_strategy%22%2C%22value%22%3A%5B%22Diagnostic%20Slide%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D&searchTableTab=files)
    * [downloaded manifest from 2021-11-03](./tcga-download/gdc_manifest.2021-11-03-TCGA-LUSC.txt): 512 slides from 478 patients with 478 cases

* [./0-download-LUSC-and-LUAD.sh](./0-download-LUSC-and-LUAD.sh) contains commands to download
**3 diagnostic slides (check that everything is fine first)** from both the
LUAD (https://portal.gdc.cancer.gov/projects/TCGA-LUAD) and the
LUSC (https://portal.gdc.cancer.gov/projects/TCGA-LUSC) sets of the TCGA
into `./WSI/LUSC/` and `./WSI/LUAD/` respectively. To download all files, remove
"-pilot" from the commands in `./0-download-LUSC-and-LUAD.sh`. The destinations
can be changed in the configuration files:
  * `./tcga-download/config-LUSC.dtt`
  * `./tcga-download/config-LUAD.dtt`

* `./WSI/` folder contains 2 subfolders `./WSI/LUSC/` and `./WSI/LUAD`, which in
turn contain the diagnostic slides. These folders are not present in this
repository and will have to be made.

* [./dsmil-split/](./dsmil-split/) directory contains the information from the DSMIL-WSI ([paper](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Dual-Stream_Multiple_Instance_Learning_Network_for_Whole_Slide_Image_Classification_CVPR_2021_paper.html), [code](https://github.com/binli123/dsmil-wsi/)) on this dataset. See section "Corrupted Slides Excluded in DSMIL-WSI work" of this README for more details.

* [./2-check-names.ipynb](./2-check-names.ipynb) contains code to check that the downloaded slides are not corrupted and that the names of the slides match the names in the manifest files. It also creates [./classes_extended_info.csv](./classes_extended_info.csv) file.

* [./classes_extended_info.csv](./classes_extended_info.csv) was created using [./2-check-names.ipynb](./2-check-names.ipynb) contains the patient ID, case ID, slide ID, slide md5sum, for each slide.
  The file was created by combining 
  * list of the downloaded slides
  * md5sum hashes of the downloaded slides
  * manifest files for LUAD and LUSC

## Corrupted Slides Excluded in [DSMIL-WSI work](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Dual-Stream_Multiple_Instance_Learning_Network_for_Whole_Slide_Image_Classification_CVPR_2021_paper.html)

There seem to be some corrupted files that were excluded from the dataset in DSMIL-WSI work. see [issue](https://github.com/binli123/dsmil-wsi/issues/16) that gives a [Google Drive Link](https://drive.google.com/drive/folders/1UobMSqJEqINX2izxrwbgprugjlTporSQ) to the TCGA-lung dataset. When using the code from the [dsmil-wsi repo](https://github.com/binli123/dsmil-wsi) to download pre-trained features for TCGA-lung, the excluded set is different. The names of the folders within the google drive folder have changed, however, the slide names contain the patient ID (first 12 characters) and case ID (first 15 characters). See [./classes_extended_info.csv](./classes_extended_info.csv). Use [./2-check-names.ipynb](./2-check-names.ipynb) code to investigate and choose which of the slides you want to exclude.

My investigation results:

1. All of the slides have a significantly darker background around the tissue.

2. In Google Drive version, 11 LUAD parients 1 case per patient and 1 slide per case were excluded

| patient_id   | case_id          | slide_id_short              |
|--------------|------------------|-----------------------------|
| TCGA-05-4384| TCGA-05-4384-01 | TCGA-05-4384-01Z-00-DX1    |
| TCGA-05-4390| TCGA-05-4390-01 | TCGA-05-4390-01Z-00-DX1    |
| TCGA-05-4410| TCGA-05-4410-01 | TCGA-05-4410-01Z-00-DX1    |
| TCGA-05-4425| TCGA-05-4425-01 | TCGA-05-4425-01Z-00-DX1    |
| TCGA-05-5420| TCGA-05-5420-01 | TCGA-05-5420-01Z-00-DX1    |
| TCGA-05-5423| TCGA-05-5423-01 | TCGA-05-5423-01Z-00-DX1    |
| TCGA-05-5425| TCGA-05-5425-01 | TCGA-05-5425-01Z-00-DX1    |
| TCGA-05-5428| TCGA-05-5428-01 | TCGA-05-5428-01Z-00-DX1    |
| TCGA-05-5429| TCGA-05-5429-01 | TCGA-05-5429-01Z-00-DX1    |
| TCGA-05-5715| TCGA-05-5715-01 | TCGA-05-5715-01Z-00-DX1    |
| TCGA-44-7661| TCGA-44-7661-01 | TCGA-44-7661-01Z-00-DX1    |


3. In GitHub version, 7 out of the Google Drive's 11 patients with their 7 cases and 7 slides were exluded. The remaining 4 patients with 4 cases and 4 slides were not excluded.

| patient_id   | case_id          | slide_id_short              |
|--------------|------------------|-----------------------------|
| TCGA-05-4384| TCGA-05-4384-01 | TCGA-05-4384-01Z-00-DX1    |
| TCGA-05-4410| TCGA-05-4410-01 | TCGA-05-4410-01Z-00-DX1    |
| TCGA-05-4425| TCGA-05-4425-01 | TCGA-05-4425-01Z-00-DX1    |
| TCGA-05-5420| TCGA-05-5420-01 | TCGA-05-5420-01Z-00-DX1    |
| TCGA-05-5423| TCGA-05-5423-01 | TCGA-05-5423-01Z-00-DX1    |
| TCGA-05-5425| TCGA-05-5425-01 | TCGA-05-5425-01Z-00-DX1    |
| TCGA-05-5715| TCGA-05-5715-01 | TCGA-05-5715-01Z-00-DX1    |

4. [Test set form google drive](./dsmil-split/google-drive/TEST_ID.csv) has 1 slide that is also in the [excluded set from google drive](./dsmil-split/google-drive/EX_ID.csv): `TCGA-05-4390-01Z-00-DX1`. However, all slides from the [test set on google drive](./dsmil-split/google-drive/TEST_ID.csv) are included in the [slides on GitHub](./dsmil-split/repository-download-TCGA-lung-ms/TCGA-lung-ms.csv).

**Decision:** I will use the GitHub version of the dataset (excludes the 7 patients with 7 cases and 7 slides). I will use the [test set from google drive](./dsmil-split/google-drive/TEST_ID.csv) as the test set to be able to make a direct comparison to the [DSMIL-WSI results](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Dual-Stream_Multiple_Instance_Learning_Network_for_Whole_Slide_Image_Classification_CVPR_2021_paper.html) since this test set is fully included in the [slides on GitHub](./dsmil-split/repository-download-TCGA-lung-ms/TCGA-lung-ms.csv).
