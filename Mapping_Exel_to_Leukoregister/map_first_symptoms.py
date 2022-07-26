import pandas as pd
from utils import map_data , add_df_name_to_column_names

def mapping_first_symptoms(exel_file_path: str,output_df: pd.DataFrame) -> pd.DataFrame:
    """
    Maps the data from the excel file to the leukoregister for the diagnostic confirmation felds.
    :return: pd.DataFrame, the mapped data for the leukoregister project (rows=patients, cols=fields)
    """
    exel_ueberblick_df = pd.read_excel(exel_file_path, sheet_name="Überblick", usecols="A:X")
    exel_ueberblick_df =add_df_name_to_column_names(exel_ueberblick_df, "Überblick")
    exel_onset_df = pd.read_excel(exel_file_path, sheet_name="Onset", usecols="A:AC")
    exel_onset_df = add_df_name_to_column_names(exel_onset_df, "Onset")
    exel_combind_df = pd.merge(exel_ueberblick_df, exel_onset_df, how='right', left_on='Überblick/ID', right_on='Onset/ID')
    # get the mapping rules from the maping csv
    mapping_df = pd.read_csv("mapping_csvs/first_symptoms.csv")
    # map the data
    output_df = map_data(mapping_df, exel_combind_df, output_df)

    return output_df