from src.functions import load_data, sort_data_date, conclusion_data, \
    change_check, change_number_card, get_formatted_operation

data = load_data('./data/operations.json')
sorted_data = sort_data_date(data)
conclusion_operations = conclusion_data(sorted_data)
formatted_operation = get_formatted_operation(conclusion_operations)
for elem in formatted_operation:
    for value in elem.values():
        print(value)
    print()