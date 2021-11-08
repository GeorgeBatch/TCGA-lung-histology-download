# TCGA Lung Dataset

This repository contains the instructions of how to download the diagnostic slides for the lung portion of the TCGA dataset. It will require ~800GB of space.

0. Make sure you have enough disk space: ~800**GB**.
1. Download the `gdc-client` Data Transfer Tool binaries from https://gdc.cancer.gov/access-data/gdc-data-transfer-tool and add it to your path.
2. Clone this repository and `cd` into it.
3. Create `./WSI/LUSC/` and `./WSI/LUAD` folders.
4. If you choose to change the folder structure, make changes to the `./tcga-download/config-LUSC.dtt` and `./tcga-download/config-LUAD.dtt` accordingly.
5. Run: `bash ./download-LUSC-and-LUAD.sh` to download the files. It will take a while. Restarting the download is not advisable. I am not sure, but I think the manifest file will need to be modified: already downloaded files fill need to be excluded.

**Tip:** I used `tmux` for the process to continue on a remote surver after I closed the connedtion. See this [answer](https://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session) on StackExchange.

## Contents

* `./tcga-download/` folder was originally copied from [here](https://github.com/binli123/dsmil-wsi/tree/master/tcga-download). Some names present in the manifest files were not available for download with the `gdc-client`. So new manifest files were downloaded from [TCGA-LUAD](https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-LUAD%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22files.experimental_strategy%22%2C%22value%22%3A%5B%22Diagnostic%20Slide%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D&searchTableTab=files) (541 slides) and [TCGA-LUSC](https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-LUSC%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22files.experimental_strategy%22%2C%22value%22%3A%5B%22Diagnostic%20Slide%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D&searchTableTab=files) (512 slides) web pages on 03/11/2021 (date is in the names).
* `./download-LUSC-and-LUAD.sh` contains commands to download the **diagnostic slides** from both the LUAD (https://portal.gdc.cancer.gov/projects/TCGA-LUAD) and the LUSC (https://portal.gdc.cancer.gov/projects/TCGA-LUSC) sets of the TCGA into `./WSI/LUSC/` and `./WSI/LUAD/` respectively. The distinations can be changed in the configuration files: `./tcga-download/config-LUSC.dtt` and `./tcga-download/config-LUAD.dtt`
* `./WSI/` folder contains 2 subfolders `./WSI/LUSC/` and `./WSI/LUAD`, which in turn contain the diagnostic slides. These folders are not present in this repository and will have to be made.
