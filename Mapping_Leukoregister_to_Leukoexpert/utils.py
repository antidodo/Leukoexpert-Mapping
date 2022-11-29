import pandas as pd
import numpy as np
from numpy import int64
import functools
import datetime
from dateutil.relativedelta import relativedelta

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
        requierd_data_rows = row["leukoregister"].split(";")
        mapped = mapping_operation(row["operation"], input_df[requierd_data_rows])
        #print("mapped: {}".format(mapped))
        output_df[row["leukoexpert"]] = mapped
    return output_df


def mapping_operation(operation: str, data):
    """
    This function selects the mapping operation to be performed on the data.
    :param operation:
    :param data:
    :return:
    """
    operation_total = operation.split("{")
    if len(operation_total) == 2:
        operation = operation_total[0]
        mapping_instruction = operation_total[1]
    if operation == "copy_int":
        return pd.DataFrame(list(map(copy_int, data.values))).astype('Int64')
    if operation == "copy_str":
        return pd.DataFrame(list(map(copy_str, data.values)))
    elif operation == "months_to_year":
        return pd.DataFrame(list(map(month_to_year, data.values)))
    elif operation == "encoding_diagnose":
        return pd.DataFrame(list(map(encoding_diagnose, data.values))).astype('Int64')
    elif operation == "date_to_year":
        return pd.DataFrame(list(map(date_to_year, data.values))).astype('Int64')
    elif operation == "check":
        return pd.DataFrame(list(map(check, data.values))).astype('Int64')
    elif operation == "check_int":
        return pd.DataFrame(list(map(check_int, data.values))).astype('Int64')
    elif operation == "check_str":
        return pd.DataFrame(list(map(check_str, data.values))).astype('Int64')
    elif operation == "encoding_gender":
        return pd.DataFrame(list(map(encoding_gender, data.values))).astype('Int64')
    elif operation == "date_to_age":
        return pd.DataFrame(list(map(date_to_age, data.values)))
    elif operation == "to_tow_decimal":
        return pd.DataFrame(list(map(to_tow_decimal, data.values)))
    elif operation == "floor":
        return pd.DataFrame(list(map(data_floor, data.values))).astype('Int64')
    elif operation == "months_to_date_year":
        return pd.DataFrame(list(map(months_to_date_year, data.values))).astype('Int64')
    elif operation == "precision":
        return pd.DataFrame(list(map(precision, data.values))).astype('Int64')
    elif operation == "precision_months":
        return pd.DataFrame(list(map(precision_months, data.values))).astype('Int64')
    elif operation == "precision_data_and_months":
        return pd.DataFrame(list(map(precision_data_and_months, data.values))).astype('Int64')
    elif operation == "map":
        return pd.DataFrame(list(map(functools.partial(mapping, mapping_instruction=mapping_instruction), data.values)))
    elif operation == "copy_with_condition":
        return pd.DataFrame(
            list(map(functools.partial(copy_with_condition, conditions=mapping_instruction), data.values)))
    elif operation == "compair_first_if_identical_second_else":
        return pd.DataFrame(list(
            map(functools.partial(compair_first_if_identical_second_else, choses=mapping_instruction), data.values)))
    elif operation == "date_to_year_with_condition":
        return pd.DataFrame(list(map(functools.partial(date_to_year_with_condition, conditions=mapping_instruction), data.values))).astype('Int64')
    elif operation == "yob_and_age_to_date":
        return pd.DataFrame(list(map(functools.partial(yob_and_age_to_date), data.values))).astype('Int64')
    else:
        raise ValueError("Unknown operation: {}".format(operation))
def yob_and_age_to_date(data):
    """
    This function returns the date day month year from the date of birth and age.
    :param data:
    :return:
    """
    #TODO
    raise ValueError("not implemented yet")


def date_to_year_with_condition(data, conditions):
    """
    This function copies the data[0]  if the condition is the same as data[1].
    :param data:
    :param mapping_instruction:
    :return:
    """
    if pd.isnull(data).any():
        return None
    conditions = conditions.split(",")
    for condition in conditions:
        if str(data[1]) == condition:
            re =pd.to_datetime(data[0]).year
            return re

    return None

def compair_first_if_identical_second_else(data, choses):
    """
    This function cpares the tow elemets in data if they are identical it returns the first element of choses eles it retruns the socond one
    :param data:
    :param mapping_instruction:
    :return:
    """
    if pd.isnull(data).any():
        return None
    choses = choses.split(",")
    if data[0] == data[1]:
        return choses[0]
    else:
        return choses[1]


def copy_with_condition(data, conditions):
    """
    This function copies the data[0]  if the condition is the same as data[1].
    :param data:
    :param mapping_instruction:
    :return:
    """
    if pd.isnull(data).any():
        return None
    for condition in conditions.split(","):
        if data[1] == condition:
            return data[0]

    return None


def mapping(data, mapping_instruction):
    """
    This function maps the data to the leukoregister.
    :param data:
    :param mapping_instruction:
    :return:
    """

    if pd.isnull(data):
        return None
    list_instructions = mapping_instruction.split(",")
    default = list_instructions[-1]

    for instruction in list_instructions[:-1]:
        split_instruction = instruction.split(":")
        if split_instruction[0] == data:
            return split_instruction[1]
    return default


def precision_data_and_months(data):
    """
    This function returns the precision of the data and months.
    :param data:
    :return:
    """
    if pd.isnull(data).any():
        return None
    if data.size == 2 and isinstance(data[0], datetime.datetime) and isinstance(data[1],
                                                                                (int, float, np.int64)) and 0 <= data[
        1] <= 1440:
        return 1
    else:
        return 2


def to_tow_decimal(data):
    """
    This function returns the data to two decimal places.
    :param data:
    :return:
    """
    if pd.isnull(data):
        return None
    return round(data[0], 2)


def precision_months(data):
    """
    This function returns the precision of the months.
    :param data:
    :return:
    """
    if pd.isnull(data):
        return None
    if isinstance(data, (int, float, np.int64)) and 0 <= data <= 1440:
        return 1
    else:
        return 2


def precision(data):
    """
    This function returns a 1 when the age was calculated and 2 when one of the dates was nan.
    :param data:
    :return:
    """
    if pd.isnull(data).any():
        return None
    if data.size == 2 and data.dtype == 'datetime64[ns]':
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
    assert isinstance(data, (int64, int, float))

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
    # TODO
    if pd.isnull(data).any():
        return None
    res = (pd.to_datetime(data[0]) + relativedelta(months=data[1])).year
    return res


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


def check_int(data):
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


def check_str(data):
    """
    This function checks if the data is a str or nan
    :param data:
    :return:
    """
    data = data[0]
    if pd.isnull(data):
        return 99
    assert isinstance(data, str)
    return 1


def check(data):
    """
    This function checks if ther is a value in the date.
    :param data:
    :return:
    """
    data = data[0]
    if pd.isnull(data):
        return 99
    assert isinstance(data, (int, float, str))
    return 1


def add_df_name_to_column_names(df, name):
    """
    This function adds a name to all of the columns.
    :param df:
    :return:
    """
    df = df.rename(columns=lambda x: name + "/" + x)
    return df
