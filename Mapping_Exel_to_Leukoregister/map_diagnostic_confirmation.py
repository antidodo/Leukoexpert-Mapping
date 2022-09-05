import pandas as pd
from utils import map_data ,add_df_name_to_column_names

def mapping_diagnostic_confirmation(exel_file_path: str,output_df: pd.DataFrame) -> pd.DataFrame:
    """
    Maps the data from the excel file to the leukoregister for the diagnostic confirmation felds.
    :return: pd.DataFrame, the mapped data for the leukoregister project (rows=patients, cols=fields)
    """
    #TODO find the places that are needed and create the mapping csv
    # get the data from the excel file

    exel_ueberblick_df = pd.read_excel(exel_file_path, sheet_name="Überblick", usecols="A:X")
    exel_ueberblick_df =add_df_name_to_column_names(exel_ueberblick_df, "Überblick")

    exel_genetik_df = pd.read_excel(exel_file_path, sheet_name="Genetik", usecols="A:W")
    exel_genetik_df = add_df_name_to_column_names(exel_genetik_df, "Genetik")

    exel_biochemie_df = pd.read_excel(exel_file_path, sheet_name="Biochemie", usecols="A:H")
    exel_biochemie_df = add_df_name_to_column_names(exel_biochemie_df, "Biochemie")

    exel_combind_df = pd.merge(exel_ueberblick_df, exel_genetik_df, how='right', left_on='Überblick/ID', right_on='Genetik/ID')
    exel_combind_df = pd.merge(exel_combind_df, exel_biochemie_df, how='right', left_on='Überblick/ID', right_on='Biochemie/ID')
    # get the mapping rules from the maping csv
    mapping_df = pd.read_csv("mapping_csvs/diagnostic_confirmation.csv")
    # map the data
    output_df = map_data(mapping_df, exel_combind_df, output_df)

    return output_df