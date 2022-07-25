import pandas as pd
import datetime

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
        # check if ther is nan in pandas datframe
        if pd.isnull(row["operation"]):
            continue

        mapped = mapping_operation(row["operation"], input_df[row["exel"]])
        print(mapped)
        print(row)
        #output_df[row["leukoregister"]] = mapping_operation(row["operation"], input_df[row["exel"]])
    return output_df


def mapping_operation(operation: str, data):
    """
    This function selects the mapping operation to be performed on the data.
    :param operation:
    :param data:
    :return:
    """
    if operation == "copy":
        return data
    elif operation == "month_to_year":
        return map(month_to_year,data)
    elif operation == "encoding_diagnose":
        return map(encoding_diagnose,data)
    elif operation == "date_to_year":
        return map(date_to_year,data)
    elif operation == "check":
        return map(check,data)
    else:
        return []

def month_to_year(data):
    """
    This function converts the month to year.
    :param data:
    :return:
    """
    assert isinstance(data, int)
    return data // 12

def encoding_diagnose(data):
    """
    This function encodes the diagnose.
    :param data:
    :return:
    """
    #tODO: implement this

    return data

def date_to_year(data):
    """
    This function converts the date to year.
    :param data:
    :return:
    """
    assert isinstance(data, datetime.date)
    return int(data.year)

def check(data):
    """
    This function checks if the data is valid.
    :param data:
    :return:
    """
    assert isinstance(data, str)
    if data is not None:
        return 1
    else:
        return 0