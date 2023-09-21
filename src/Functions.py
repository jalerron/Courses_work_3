import json


def load_data(file):
    """
    Extract data from file
    """
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    operation_data = []

    for data_ in data:
        operation_data.append(data_)

    return operation_data


