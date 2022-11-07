import pandas as pd
import os
import math
from map import mapping

def mapping_Leukoregister_to_Leukoexpert():
    # get file name from args
    # curently as hardcoded variables drunig development
    leukoregister_file_path = "data/Leukoregister.csv"
    output_template_path = "mapping_csvs/output_template.csv"
    output_path = "output/mapped.csv"
    mapping_csvs_path = "mapping_csvs/"

    output_df = pd.read_csv(output_template_path)

    print("Mapping data...")
    # get alle files in the mapping_csvs folder
    mapping_file_paths = [f for f in os.listdir(mapping_csvs_path) if os.path.isfile(os.path.join(mapping_csvs_path, f))]

    for mapping_file_path in mapping_file_paths:
        print("Mapping " + mapping_file_path + "...")
        output_df = mapping(leukoregister_file_path,mapping_file_path,output_df)
    print("Mapping data...done")

if __name__ == '__main__':
    """
    Maps the data from the Leukoregister to the Leukoexpert radcap csv
    """
    #mapping_Leukoregister_to_Leukoexpert()
    print(int(round(math.log(4, 2))))


