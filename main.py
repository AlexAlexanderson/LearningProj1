import case1
import unicodedata


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
    str_data = str_data.replace("  ", " ")
    str_data = str_data.replace("\"", "")
    str_data = str_data.replace("\'", "")
    str_data = str_data.replace(":", ",")
    str_data = str_data.replace(";", ",")

    list_of_dict_el = str_data.split(',')
    for dict_el in list_of_dict_el:
        key_and_value = dict_el.strip().split("=")
        if len(key_and_value) == 2:
            dict_data[key_and_value[0].strip()] = key_and_value[1].strip()

    if len(dict_data) == 0:
        return None
    else:
        return dict_data


str_data = input('input arguments (example: aaa=1, sum1=1, sum2=2.1, bbb="bbb", sum3=100, sum4="one hundred"): ')
dict_data = str_to_dict_if_possible(str_data)
if dict_data is None:
    print("unable to get values from string")
else:
    print(case1.case1_func(sum=dict_data))
