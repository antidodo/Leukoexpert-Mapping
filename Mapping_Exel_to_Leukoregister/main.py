import pandas as pd
from map_demographics import mapping_demographics

def mapp_exel_to_leuko_register():
    """
    Maps the data from the excel file to the leukoregister radcap csv and returns the mapped data in the same format as the
    csv that can be uplodat to redcap.
    :return: pd.DataFrame, the mapped data for the leukoregister project (rows=patients, cols=fields)
    """
    # get file name from args
    # curently as hardcoded variables drunig development
    excel_file_path = "../data/Tabelle_MLD_Datenstruktur.xlsx"
    output_template_path = "Mapping_Exel_to_Leukoregister/mapping_csvs/output_template.csv"
    output_file_path = "./data/mapped_data.csv"
    print("Mapping data...")
    mapping_demographics(excel_file_path)


if __name__ == '__main__':
    mapp_exel_to_leuko_register()