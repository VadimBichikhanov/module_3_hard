def convert_to_list(data):
    if isinstance(data, dict):
        return [{convert_to_list(key): convert_to_list(value)} for key, value in data.items()]
    elif isinstance(data, list):
        return [convert_to_list(element) for element in data]
    elif isinstance(data, tuple):
        return [convert_to_list(element) for element in data]
    else:
        return data

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

converted_data_structure = convert_to_list(data_structure)
print(converted_data_structure)

def extract_data(converted_data_structure):
    result = []

    def flatten(element):
        if isinstance(element, list):
            for item in element:
                flatten(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                flatten(key)
                flatten(value)
        else:
            result.append(element)

    flatten(converted_data_structure)
    return result

extracted_data = extract_data(converted_data_structure)
print(extracted_data)

def recursive_sum_and_length(extracted_data):
    total_sum = 0
    total_length = 0

    for item in extracted_data:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            total_length += len(item)
        elif isinstance(item, list):
            sub_sum, sub_length = recursive_sum_and_length(item)
            total_sum += sub_sum
            total_length += sub_length
        elif isinstance(item, tuple):
            sub_sum, sub_length = recursive_sum_and_length(list(item))
            total_sum += sub_sum
            total_length += sub_length
        elif isinstance(item, set):
            sub_sum, sub_length = recursive_sum_and_length(list(item))
            total_sum += sub_sum
            total_length += sub_length

    return total_sum, total_length

result_sum, result_length = recursive_sum_and_length(extracted_data)
print(f"Sum of numbers: {result_sum}")
print(f"Total length of strings: {result_length}")
print(f"resalt sum: {result_sum + result_length}")