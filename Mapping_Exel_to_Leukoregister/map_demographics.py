import pandas as pd
from utils import map_data, add_df_name_to_column_names

def mapping_demographics(exel_file_path: str,output_df: pd.DataFrame) -> pd.DataFrame:
    """
    Maps the data from the excel file to the leukoregister for the demographics felds.
    :return: pd.DataFrame, the mapped data for the leukoregister project (rows=patients, cols=fields)
    """
    # get the data from the excel file
    exel_ueberblick_df = pd.read_excel(exel_file_path, sheet_name="Überblick", usecols="A:X")
    exel_ueberblick_df = add_df_name_to_column_names(exel_ueberblick_df, "Überblick")
    # get the mapping rules from the maping csv
    mapping_df = pd.read_csv("mapping_csvs/demographics.csv")
    # map the data
    output_df = map_data(mapping_df, exel_ueberblick_df, output_df)

    return output_df
