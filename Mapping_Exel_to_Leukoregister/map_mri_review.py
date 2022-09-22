import pandas as pd
from utils import map_data , add_df_name_to_column_names

def mapping_mri_review(exel_file_path: str,mrt_database_file_path: str,output_df: pd.DataFrame) -> pd.DataFrame:
    """
    Maps the data from the excel file to the leukoregister for the diagnostic confirmation felds.
    :return: pd.DataFrame, the mapped data for the leukoregister project (rows=patients, cols=fields)
    """
    exel_ueberblick_df = pd.read_excel(exel_file_path, sheet_name="Überblick", usecols="A:X")
    exel_ueberblick_df =add_df_name_to_column_names(exel_ueberblick_df, "Überblick")
    mrt_database_df = pd.read_csv(mrt_database_file_path)
    mrt_database_df = add_df_name_to_column_names(mrt_database_df, "MRT_Datenbank")
    exel_mrt_df = pd.read_excel(exel_file_path, sheet_name="MRT", usecols="A:BH")
    exel_mrt_df = add_df_name_to_column_names(exel_mrt_df, "MRT")
    exel_combind_df = pd.merge(exel_ueberblick_df, exel_mrt_df, how='right', left_on='Überblick/ID', right_on='MRT/ID')
    exel_combind_df = pd.merge(exel_combind_df, mrt_database_df, how='right', left_on='Überblick/ID', right_on='MRT_Datenbank/PCODE')
    # get the mapping rules from the maping csv
    mapping_df = pd.read_csv("mapping_csvs/mri_review.csv")
    # map the data
    output_df = map_data(mapping_df, exel_combind_df, output_df)

    return output_df