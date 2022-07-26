import pandas as pd
import datetime


def map_data(mapping_df, input_df, output_df):
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
        # get all the relevant
        requierd_data_rows = row["exel"].split(";")

        mapped = mapping_operation(row["operation"], input_df[requierd_data_rows])
        print("mapped: {}".format(mapped))
        output_df[row["leukoregister"]]  = mapped
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
        return list(map(month_to_year, data))
    elif operation == "encoding_diagnose":
        data = data.values.tolist()
        return list(map(encoding_diagnose, data))
    elif operation == "date_to_year":
        return list(map(date_to_year, data.values))
    elif operation == "check":
        return list(map(check, data))
    elif operation == "encoding_gender":
        return list(map(encoding_gender, data))
    elif operation == "date_to_age":
        return
    else:
        raise ValueError("Unknown operation: {}".format(operation))



def encoding_gender(data):
    """
    This function converts from the exel gender codes to the leukregister codes
    :return:
    """
    if pd.isnull(data):
        return None
    if data == "m":
        return 2
    elif data == "w":
        return 1


def month_to_year(data):
    """
    This function converts the month to year.
    :param data:
    :return:
    """
    if pd.isnull(data):
        return None
    assert isinstance(data, (int, float))

    return data // 12


def encoding_diagnose(data):
    """
    This function encodes the diagnose.
    :param data:
    :return:
    """
    if pd.isnull(data):
        return None
    if data == 1:
        return 20
    elif data == 2:
        return 20
    elif data == 3:
        return 20
    return data


def date_to_year(data):
    """
    This function converts the date to year.
    :param data:
    :return:
    """
    if pd.isnull(data):
        return None
    re =pd.to_datetime(data).year
    return pd.to_datetime(data).year.asi8[0]


def check(data):
    """
    This function checks if the data is a number or nan
    :param data:
    :return:
    """
    if pd.isnull(data):
        return None
    assert isinstance(data, (int, float))
    return 1
