import json
from datetime import datetime


def load_data(file):
    """
    Extract data from file
    """
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    operation_data = []  # list for all data from file

    for data_ in data:
        if data_:
            operation_data.append(data_)

    return operation_data


def sort_data_date(data):
    """
    Sort data by date
    """
    sorted_list = sorted(data, key=lambda data_: data_['date'], reverse=True)

    return sorted_list


def conclusion_data(data, last_operation=5):
    """
    Conclusion last X operation
    :param data: sorted list operation
    :param last_operation: how much last operation need. 5 - default
    :return: list conclusion operation
    """
    conclusion_list = []

    for data_ in data:
        while len(conclusion_list) <= last_operation-1:
            if data_["state"] == "EXECUTED":
                conclusion_list.append(data_)
            print(len(conclusion_list))

    return conclusion_list
