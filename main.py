import case1
import unicodedata
import re


def remove_control_characters(s):
    """
    со stackoverflow: удаление управляющих символов
    :param s:
    :return:
    """
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")


def str_to_dict_if_possible(str_data):
    """
    преобразование строки в словарь если возможно
    :param str_data:
    :return:
    """
    dict_data = dict()

    # удалим либо заменим неподходящие символы
    str_data = remove_control_characters(str_data)
    str_data = re.sub(r' {2}', ' ', str_data)
    str_data = re.sub(r'[:;,]', ',', str_data)

    # находим в строке шаблоны ключей-значений для формирования массива
    list_of_dict_el = re.findall(r'\w+=[-\w\'\" ]+', str_data)

    for dict_el in list_of_dict_el:
        key_and_value = dict_el.strip().split("=")
        if len(key_and_value) == 2:
            dict_data[key_and_value[0].strip()] = key_and_value[1].strip()

    if len(dict_data) == 0:
        return None
    else:
        return dict_data


# вариант со строкой введенной пользователем
str_param = input('input arguments (example: aaa=1, sum1=1, sum2=2.1, bbb="bbb", sum3=100, sum4="one hundred"): ')
dict_param = str_to_dict_if_possible(str_param)
if dict_param is None:
    print("unable to get values from string")
else:
    print(case1.case1_func(**dict_param))

# вариант с прямым вызовом функции
dict_param = {
    'aaa': 1,
    'sum1': 1,
    'sum2': 2.1,
    'bbb': 'bbb',
    'sum3': 100,
    'sum4': 'one hundred',
    'sum5': {
        'sum6': -1000,
        'sum7': '2000',
        'ccc': 3000,
        'sum1': 20,
        'sum200': {
            'sum201': 100,
            'sum202': '100',
        },
    },
}
print(case1.case1_func(**dict_param))
