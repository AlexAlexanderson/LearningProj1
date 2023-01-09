def str_to_int_if_possible(value):
    """
    преобразование строки в число если возможно
    :param value:
    :return:
    """

    value_is_float = False

    for s in value:
        if not (s == "-" or s == '.' or s.isdigit()):
            return value
        if s == '.':
            value_is_float = True
    if value_is_float:
        return float(value)
    else:
        return int(value)


def case1_func(**dict_data):
    """
    ТЗ Кейса:
    Написать функцию, которая принимает на вход сколько угодно параметров.
    Находит среди этих параметров те, которые начинаются со слова "sum".
    На выход возвращает все найденные параметры, а также сумму значений этих параметров.
    Требования к решению:
    Вашу функцию нельзя сломать из вне. Передаю ей всё что угодно, она не вызывает ошибок.
    А лишь выводит уведомление о том что она не понимает что я от неё хочу.
    Бороться с ошибками в данном кейсе нужно используя только условные конструкции (без try).
    :param dict_data:
    :return:
    """

    result = dict(sum=0, )

    for key, value in dict_data.items():
        if key.find('sum') != -1:
            if value is int or value is float:  # если значение число - просто просуммируем
                # print(key, value)
                result['sum'] += value
                result[key] = value
            elif value is str:  # если значение строка - преобразуем в число и просуммируем
                value_is_float = False
                for s in value:
                    if not (s == "-" or s == '.' or s.isdigit()):
                        return value
                    if s == '.':
                        value_is_float = True
                if value_is_float:
                    value = float(value)
                    result['sum'] += value
                    result[key] = value
                else:
                    value = int(value)
                    result['sum'] += value
                    result[key] = value
            elif type(value) == dict:  # если значение словарь - вызовем рекурсивно
                rec_result = case1_func(sum=value)
                """
                так сложно потому что нужно из рекурсивного результата sum просуммировать к основному результату, 
                а остальные ключи добавить
                """
                for r_key, r_value in rec_result.items():
                    if r_key == 'sum':
                        result['sum'] += r_value
                    else:
                        result[r_key] = r_value
            else:
                print(key, value, "(value is not a number ", type(value), ")")

    return result
