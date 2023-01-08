import unicodedata

# со stackoverflow: удаляем управляющие символы
def remove_control_characters(s):

    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")

# преобразуем строку в число если возможно
def str_to_int_if_possible(value):

    value_is_float = False

    for s in value:
        if (s == "-" or s == '.' or s.isdigit()) != True:
            return value
        if s == '.':
            value_is_float = True
    if value_is_float:
        return float(value)
    else:
        return int(value)

# преобразуем строку в словарь если возможно
def str_to_dict_if_possible(str_data):

    dict_data = dict()

    # удалим либо заменим неподходящие символы
    str_data = remove_control_characters(str_data)
    str_data = str_data.replace("  ", " ")
    str_data = str_data.replace("\"", "")
    str_data = str_data.replace("\'", "")
    str_data = str_data.replace(":", ",")
    str_data = str_data.replace(";", ",")

    # со stackoverflow: превращаем строку в словарь
    # по красоте не подходит т.к. с неподходящей строкой валится в ошибку
    # dict_data = dict((a.strip(), str_to_int_if_possible(b.strip()))
    #                  for a, b in (element.split('=')
    #                               for element in str_data.split(', ')))

    # свое поделие для превращения строки в словарь
    list_of_dict_el = str_data.split(',')
    for dict_el in list_of_dict_el:
        key_and_value = dict_el.strip().split("=")
        if len(key_and_value) == 2:
            dict_data[key_and_value[0].strip()] = str_to_int_if_possible(key_and_value[1].strip())

    print(str_data)
    # print(type(dict_data))
    print(dict_data)

    if len(dict_data) == 0:
        print("не удалось получить значения из строки")
        return None
    else:
        return dict_data


# собственно, функция кейса
def case1_func(string_data):

    dict_data = str_to_dict_if_possible(string_data)
    if dict_data == None:
        return

    result = 0
    for key, value in dict_data.items():
        if key.find("sum") != -1:
            typevalue = type(value)
            if typevalue == int or typevalue == float:
                print(key, value)
                result += value
            else:
                print(key, value, "(value is not a number ", typevalue, ")")
    print("sum =", result)
