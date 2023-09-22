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


# print(load_data('../data/operations.json'))

def sort_data_date(data):
    """
    Sort data by date
    """
    sorted_list = sorted(data, key=lambda data_: data_['date'], reverse=True)

    return sorted_list
