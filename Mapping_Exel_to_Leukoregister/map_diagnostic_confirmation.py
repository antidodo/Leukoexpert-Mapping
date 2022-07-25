import pandas as pd
from utils import map_data

def mapping_diagnostic_confirmation(exel_file_path: str,output_df: pd.DataFrame) -> pd.DataFrame:
    """
    Maps the data from the excel file to the leukoregister for the diagnostic confirmation felds.
    :return: pd.DataFrame, the mapped data for the leukoregister project (rows=patients, cols=fields)
    """
    #TODO find the places that are needed and create the mapping csv
    # get the data from the excel file
    exel_ueberblick_df = pd.read_excel(exel_file_path, sheet_name="???", usecols="???")
    # get the mapping rules from the maping csv
    mapping_df = pd.read_csv("mapping_csvs/diagnostic_confirmation.csv")
    # map the data
    output_df = map_data(mapping_df, exel_ueberblick_df, output_df)

    return output_df