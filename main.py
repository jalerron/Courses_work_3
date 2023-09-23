from src.functions import load_data, sort_data_date, conclusion_data, get_formatted_operation
from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT_PATH, 'data')
OPERATIONS_PATH = Path.joinpath(DATA_PATH, 'operations.json')

data = load_data(OPERATIONS_PATH)
sorted_data = sort_data_date(data)
conclusion_operations = conclusion_data(sorted_data)
formatted_operation = get_formatted_operation(conclusion_operations)
for elem in formatted_operation:
    for value in elem.values():
        print(value)
    print()
