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


def change_number_card(card_number):
    """
    mask number card
    :param card_number: card_number
    :return: mask number card
    """
    number = []
    card_name = []
    for elem in card_number.split(' '):
        print(elem)
        if elem.isdigit():
            number.append(elem)
        else:
            card_name.append(elem)

    number = ''.join(number)
    card_name = ' '.join(card_name)

    mask_card = f'{card_name} {number[:4]} {number[4:6]}** **** {number[12:]}'

    return mask_card
