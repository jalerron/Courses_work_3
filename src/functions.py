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
        if data_["state"] == "EXECUTED":
            conclusion_list.append(data_)

    return conclusion_list[:last_operation]


def change_number_card(card_number):
    """
    mask number card
    :param card_number: card_number
    :return: mask number card
    """
    number = []
    card_name = []
    for elem in card_number.split(' '):
        if elem.isdigit():
            number.append(elem)
        else:
            card_name.append(elem)

    number = ''.join(number)
    card_name = ' '.join(card_name)

    mask_card = f'{card_name} {number[:4]} {number[4:6]}** **** {number[12:]}'

    return mask_card


def change_check(check):
    """
    mask check
    :param check: number of check
    :return: mask check
    """
    return f'**{check[-4:]}'


def get_formatted_operation(data):
    """
    print operation
    :param data:
    :return: formatted print
    """

    formatted_operations = []

    for data_ in data:
        date_operation = datetime.fromisoformat(data_['date'])
        format_date = datetime.strftime(date_operation, '%d''.''%m''.''%Y')
        changed_check = change_check(data_['to'])
        if data_.get('from', False) != False:
            changed_number_card = change_number_card(data_['from'])
            from_to = f'{changed_number_card} -> {changed_check}'
        else:
            from_to = f'To {changed_check}'
        date = f'{format_date} {data_["description"]}'
        amount = f'{data_["operationAmount"]["amount"]} {data_["operationAmount"]["currency"]["name"]}'
        dict_operation = {'date': date, 'from_to': from_to, 'amount': amount}
        formatted_operations.append(dict_operation)

    return formatted_operations
