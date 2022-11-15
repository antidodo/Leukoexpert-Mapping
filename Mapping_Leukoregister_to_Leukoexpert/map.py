import pandas as pd
from utils import map_data



def mapping(leukoregister_file_path: str,mapping_file_path,output_df: pd.DataFrame) -> pd.DataFrame:
    """
    Maps the data from the excel file to the leukoregister for the demographics felds.
    :return: pd.DataFrame, the mapped data for the leukoregister project (rows=patients, cols=fields)
    """
    # get the data from the excel file
    exel_ueberblick_df = pd.read_csv(leukoregister_file_path)
    # get the mapping rules from the maping csv
    mapping_df = pd.read_csv(mapping_file_path)
    # map the data
    output_df = map_data(mapping_df, exel_ueberblick_df, output_df)

    return output_df

