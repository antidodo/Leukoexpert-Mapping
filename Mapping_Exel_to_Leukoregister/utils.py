import pandas as pd

def map_data(mapping_df, input_df,output_df):
    """
    This takes the mapping_df and interates ofer them and  performs the operations, then save it to the output df
    :param mapping_df:
    :param input_df:
    :param output_df:
    :return:
    """
    for index, row in mapping_df.iterrows():
        # get the column name from the mapping csv
        row["exel"]
        row["leukoregister"]
        row["operation"]

def mapping_operation(operation: str, data) -> str:
    """
    This function selects the mapping operation to be performed on the data.
    :param operation:
    :param data:
    :return:
    """
    if operation == "map":
        return map_data
    else:
        raise ""