#!/bin/bash

echo "Starting to download LUSC files"
# gdc-client download -m tcga-download/gdc_manifest.2021-11-03-TCGA-LUSC-pilot.txt --config tcga-download/config-LUSC.dtt
gdc-client download -m tcga-download/gdc_manifest.2023-10-03-TCGA-LUSC.txt --config tcga-download/config-LUSC.dtt
echo "Finished downloading LUSC files"

echo "Starting to download LUAD files"
# gdc-client download -m tcga-download/gdc_manifest.2021-11-03-TCGA-LUAD-pilot.txt --config tcga-download/config-LUAD.dtt
gdc-client download -m tcga-download/gdc_manifest.2023-10-03-TCGA-LUAD.txt --config tcga-download/config-LUAD.dtt
echo "Finished downloading LUAD files"
