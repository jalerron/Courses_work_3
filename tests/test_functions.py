from utils import functions
from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT_PATH, 'data')
DATA_LOAD_PATH = Path.joinpath(DATA_PATH, 'test_load_data.json')
TEST_SORTED_PATH = Path.joinpath(DATA_PATH, 'test_sorted_data.json')
TEST_SORT_PATH = Path.joinpath(DATA_PATH, 'test_sort_data.json')
TEST_CONCLUSION_PATH = Path.joinpath(DATA_PATH, 'test_conclusion_data.json')
TEST_FORMATTED_PATH = Path.joinpath(DATA_PATH, 'test_formatted_operation.json')

sort_data = functions.load_data(TEST_SORT_PATH)
sorted_data = functions.load_data(TEST_SORTED_PATH)
conclusion_data = functions.load_data(TEST_CONCLUSION_PATH)
formatted_data = functions.load_data(TEST_FORMATTED_PATH)


card_number = 'MasterCard 7158300734726758'
check = 'Счет 64686473678894779589'
from_func_card = 'MasterCard 7158 30** **** 6758'
from_func_check = 'Счет **9589'


def test_load_data():
    assert functions.load_data(DATA_LOAD_PATH) == [{"card": "visa"}]


def test_sort_data_date():
    assert functions.sort_data_date(sort_data) == sorted_data


def test_conclusion_data():
    assert functions.conclusion_data(sort_data) == conclusion_data


def test_change_number_card():
    assert functions.change_number_card(card_number) == from_func_card


def test_change_check():
    assert functions.change_check(check) == from_func_check


def test_get_formatted_operation():
    assert functions.get_formatted_operation(conclusion_data) == formatted_data
