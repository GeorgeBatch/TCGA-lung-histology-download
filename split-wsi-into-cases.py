import os
import glob


def extract_case_id(slide_id: str):
    return slide_id[:15]

def wsi_file_name_2_cases_path(wsi_file_name: str):
    """
    Input: '0b3cff7b-bbe2-40ab-aee6-cb0554940eaa/TCGA-05-4244-01Z-00-DX1.d4ff32cd-38cf-40ea-8213-45c2b100ac01.svs'
    Output: 'TCGA-05-4244-01/TCGA-05-4244-01Z-00-DX1.d4ff32cd-38cf-40ea-8213-45c2b100ac01.svs'
    """
    slide_name = os.path.basename(wsi_file_name)
    case_id = extract_case_id(slide_name)
    return case_id + "/" + slide_name


# original download place
TCGA_LUNG_DOWNLOAD_FOLDER = './WSI'
# move files to this folder
TCGA_LUNG_CASES_FOLDER = '../../cases'


if __name__ == "__main__":
    print(os.getcwd())
    print("TCGA_LUNG_DOWNLOAD_FOLDER contents:", os.listdir(TCGA_LUNG_DOWNLOAD_FOLDER))
    print("TCGA_LUNG_CASES_FOLDER contents:", os.listdir(TCGA_LUNG_CASES_FOLDER))


    # move all slides from TCGA_LUNG_DOWNLOAD_FOLDER to TCGA_LUNG_CASES_FOLDER
    # use the function wsi_file_name_2_cases_path to get the destination path from the source path within the TCGA_LUNG_DOWNLOAD_FOLDER
    for wsi_path in glob.glob(os.path.join(TCGA_LUNG_DOWNLOAD_FOLDER, "**/*.svs"), recursive=True):
        print(wsi_path)
        wsi_file_name = os.path.basename(wsi_path)
        new_wsi_file_name = wsi_file_name_2_cases_path(wsi_file_name)
        new_wsi_path = os.path.join(TCGA_LUNG_CASES_FOLDER, new_wsi_file_name)
        
        print(new_wsi_path)

        new_wsi_dirpath = os.path.dirname(new_wsi_path)
        os.makedirs(new_wsi_dirpath, exist_ok=True)

        # move file to a new location
        os.rename(wsi_path, new_wsi_path)