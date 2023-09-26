# TCGA Lung Dataset

This repository contains the instructions of how to download the diagnostic slides for the lung portion of the TCGA dataset. It will require ~800GB of space.

## Instructions

0. Make sure you have enough disk space: ~800**GB**.
1. Download the `gdc-client` Data Transfer Tool binaries from
https://gdc.cancer.gov/access-data/gdc-data-transfer-tool and add it to your
PATH or into `/usr/local/bin` if you have this directory (it's usually already
added to the PATH). I did not have any problems with it on Linux, however on Apple
devices you can ran into "MacOS cannot verify app is free from malware" which can be
solved as described here:
https://gadgetstouse.com/blog/2021/04/08/fix-macos-cannot-verify-app-is-free-from-malware/
2. Clone this repository and `cd` into it.
3. Create `./WSI/LUSC/` and `./WSI/LUAD` folders.
4. If you choose to change the folder structure, make changes to
   1. `./tcga-download/config-LUSC.dtt`
   2. `./tcga-download/config-LUAD.dtt`
5. Run:

```shell
bash ./download-LUSC-and-LUAD.sh
```
to download the files. It will take a
while. Restarting the download is not advisable. I am not sure, but I think the
manifest file will need to be modified: already downloaded files fill need to be
excluded.

**Tip:** I used `tmux` for the process to continue on a remote surver after I
closed the connection. See this
[how-to](https://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session)
on StackExchange.

6. Check that the downloaded slides were not currupted during the download:

```shell
md5sum ./WSI/*/*.svs > downloaded_md5sum_hashes.txt
```

The hashes should match the ones in `./tcga_download/` manifest files for LUAD and LUSC.

The code to parse the manifest files and downloaded_md5sum_hashes.txt and check the matches is in [check-names.ipynb](check-names.ipynb).

## Contents

* `./tcga-download/` folder was originally copied from [here](binli-tcga-download).
Some names present in the manifest files were not available for download with the
`gdc-client`. So new manifest files were downloaded from these web pages on 
on 03/11/2021 (date is in the names)
  * [TCGA-LUAD manifest](TCGA-LUAD-manifest) (541 slides from 478 cases)
  * [TCGA-LUSC manifest](TCGA-LUSC-manifest) (512 slides from 478 cases)
* `./download-LUSC-and-LUAD.sh` contains commands to download
**3 diagnostic slides (check that everything is fine first)** from both the
LUAD (https://portal.gdc.cancer.gov/projects/TCGA-LUAD) and the
LUSC (https://portal.gdc.cancer.gov/projects/TCGA-LUSC) sets of the TCGA
into `./WSI/LUSC/` and `./WSI/LUAD/` respectively. To download all files, remove
"-pilot" from the commands in `./download-LUSC-and-LUAD.sh`. The destinations
can be changed in the configuration files:
  * `./tcga-download/config-LUSC.dtt`
  * `./tcga-download/config-LUAD.dtt`
* `./WSI/` folder contains 2 subfolders `./WSI/LUSC/` and `./WSI/LUAD`, which in
turn contain the diagnostic slides. These folders are not present in this
repository and will have to be made.

## Note

There seem to be some corrupted files that other groups excluded from the dataset, see [issue](https://github.com/binli123/dsmil-wsi/issues/16) that gives a [Google Drive Link](https://drive.google.com/drive/folders/1UobMSqJEqINX2izxrwbgprugjlTporSQ) to the TCGA-lung dataset. The names of the folders changed, however, the slide names contain the case ID as the first 12 characters - see [classes_extended_info.csv](classes_extended_info.csv). Use [check-names.ipynb](check-names.ipynb) code to investigate and choose which of the slides you want to exclude.


[binli-tcga-download]: https://github.com/binli123/dsmil-wsi/tree/master/tcga-download
[TCGA-LUAD-manifest]: https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-LUAD%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22files.experimental_strategy%22%2C%22value%22%3A%5B%22Diagnostic%20Slide%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D&searchTableTab=files
[TCGA-LUSC-manifest]: https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-LUSC%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22files.experimental_strategy%22%2C%22value%22%3A%5B%22Diagnostic%20Slide%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D&searchTableTab=files 