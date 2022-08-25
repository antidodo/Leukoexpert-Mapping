import pandas as pd

def mapping_Leukoregister_to_Leukoexpert():
    pass

if __name__ == '__main__':
    """
    Maps the data from the Leukoregister to the Leukoexpert radcap csv
    """
    mapping_Leukoregister_to_Leukoexpert()

    # get file name from args
    # curently as hardcoded variables drunig development
    leukoregister_file_path = "data/Leukoregister.csv"
    output_template_path = "mapping_csvs/output_template.csv"
    output_path = "output/mapped.csv"
