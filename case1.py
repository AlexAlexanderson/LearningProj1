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
            if isinstance(value, int) or isinstance(value, float):  # если значение число - просто просуммируем
                result['sum'] += value
                result[key] = value
            elif isinstance(value, str):  # если значение строка - преобразуем в число и просуммируем
                value_is_float = False
                value_is_digit = True
                for s in value:
                    if not (s == "-" or s == '.' or s.isdigit()):
                        value_is_digit = False
                        break
                    if s == '.':
                        value_is_float = True
                if value_is_digit and value_is_float:
                    value = float(value)
                    result['sum'] += value
                    result[key] = value
                elif value_is_digit:
                    value = int(value)
                    result['sum'] += value
                    result[key] = value
                else: # не получилось преобразовать в число - выводим предупреждение и игнорируем
                    print(key, value, "(value is not a number ", type(value), ")")
            elif isinstance(value, dict):  # если значение словарь - вызовем функцию рекурсивно
                rec_result = case1_func(**value)
                """
                так сложно потому что нужно из рекурсивного результата sum просуммировать к основному результату, 
                а остальные ключи просто добавить, но учесть что если в рекурсивном результате есть ключи уже
                присутствующие в основном, то их тоже нужно просуммировать а не переписать
                 """
                for r_key, r_value in rec_result.items():
                    if r_key == 'sum':
                        result['sum'] += r_value
                    elif r_key in result:
                        result[r_key] += r_value
                    else:
                        result[r_key] = r_value
            else: # на случай прочих типов кроме строк, чисел и словарей
                print(key, value, "(value is not a number ", type(value), ")")

    return result
