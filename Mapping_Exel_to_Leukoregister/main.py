import pandas as pd
from map_demographics import mapping_demographics
from map_diagnostic_confirmation import mapping_diagnostic_confirmation


def mapp_exel_to_leuko_register():
    """
    Maps the data from the excel file to the leukoregister radcap csv and returns the mapped data in the same format as the
    csv that can be uplodat to redcap.
    :return: pd.DataFrame, the mapped data for the leukoregister project (rows=patients, cols=fields)
    """
    # get file name from args
    # curently as hardcoded variables drunig development
    excel_file_path = "../data/Tabelle_MLD_Datenstruktur.xlsx"
    output_template_path = "mapping_csvs/output_template.csv"
    output_df = pd.read_csv(output_template_path)
    print("Mapping data...")

    mapping_demographics(excel_file_path,output_df)
    print("demographics mapped")
    #mapping_diagnostic_confirmation(excel_file_path,output_df)

    #TODO mapping for all the Forms
    #save the mapped data to a csv
    output_file_path = "./data/mapped_data.csv"
    output_df.to_csv(output_df, index=False)



if __name__ == '__main__':
    mapp_exel_to_leuko_register()