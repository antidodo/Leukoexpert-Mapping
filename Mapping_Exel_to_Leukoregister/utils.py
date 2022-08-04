import pandas as pd
import numpy as np


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
        output_df[row["leukoregister"]] = mapped
    return output_df


def mapping_operation(operation: str, data):
    """
    This function selects the mapping operation to be performed on the data.
    :param operation:
    :param data:
    :return:
    """
    if operation == "copy_int":
        return pd.DataFrame(list(map(copy_int, data.values))).astype('Int64')
    if operation == "copy_str":
        return pd.DataFrame(list(map(copy_str, data.values)))
    elif operation == "months_to_year":
        return pd.DataFrame(list(map(month_to_year, data.values))).astype('Int64')
    elif operation == "encoding_diagnose":
        return pd.DataFrame(list(map(encoding_diagnose, data.values))).astype('Int64')
    elif operation == "date_to_year":
        return pd.DataFrame(list(map(date_to_year, data.values))).astype('Int64')
    elif operation == "check":
        return pd.DataFrame(list(map(check, data.values))).astype('Int64')
    elif operation == "encoding_gender":
        return pd.DataFrame(list(map(encoding_gender, data.values))).astype('Int64')
    elif operation == "date_to_age":
        return pd.DataFrame(list(map(date_to_age, data.values)))
    elif operation == "floor":
        return pd.DataFrame(list(map(data_floor, data.values))).astype('Int64')
    elif operation == "months_to_date_year":
        return pd.DataFrame(list(map(months_to_date_year, data.values))).astype('Int64')
    elif operation == "precision":
        return pd.DataFrame(list(map(precision, data.values))).astype('Int64')
    else:
        raise ValueError("Unknown operation: {}".format(operation))


def precision(data):
    """
    This function returns a 1 when the age was calculated and 2 when one of the dates was nan.
    :param data:
    :return:
    """
    if pd.isnull(data).any():
        return None
    if data.size==2 and data.dtype=='datetime64[ns]':
        return 1
    else:
        return 2


def copy_int(data):
    """
    This function copies the data to the leukoregister.
    :param data:
    :return:
    """
    data = data[0]
    if pd.isnull(data):
        return None
    assert isinstance(data, (int, float, np.int64))
    return int(data)


def copy_str(data):
    """
    This function copies the data to the leukoregister.
    :param data:
    :return:
    """
    data = data[0]
    if pd.isnull(data):
        return None
    assert isinstance(data, (str))
    return data


def encoding_gender(data):
    """
    This function converts from the exel gender codes to the leukregister codes
    :return:
    """
    if pd.isnull(data):
        return None
    if data[0] == "m":
        return 2
    elif data[0] == "w":
        return 1


def month_to_year(data):
    """
    This function converts the month to year.
    :param data:
    :return:
    """
    data = data[0]
    if pd.isnull(data):
        return None
    assert isinstance(data, (int, float))

    return round(data / 12, 2)


def encoding_diagnose(data):
    """
    This function encodes the diagnose.
    :param data:
    :return:
    """
    data = data[0]
    if pd.isnull(data):
        return None
    if data == 1:
        return 20
    elif data == 2:
        return 9
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
    return pd.to_datetime(data).year.values[0]

def months_to_date_year(data):
    """
    This function gets the one date and months and returns the date year.
    :param data:
    :return:
    """
    #TODO
    if pd.isnull(data):
        return None
    return "TODO"

def date_to_age(data):
    """
    This function converts the 2 dates to age.
    :param data:
    :return:
    """
    if pd.isnull(data).any():
        return None
    # get the age in years
    res = round(((pd.to_datetime(data[1]) - pd.to_datetime(data[0]))).value / 3.154e+16, 2)
    return res


def data_floor(data):
    """
    This function floors the data.
    :param data:
    :return:
    """
    data = data[0]
    if pd.isnull(data):
        return None
    assert isinstance(data, (int, float))
    return int(data)


def check(data):
    """
    This function checks if the data is a number or nan
    :param data:
    :return:
    """
    data = data[0]
    if pd.isnull(data):
        return 99
    assert isinstance(data, (int, float))
    return 1

def add_df_name_to_column_names(df, name):
    """
    This function adds a name to all of the columns.
    :param df:
    :return:
    """
    df = df.rename(columns=lambda x: name + "/" + x)
    return df