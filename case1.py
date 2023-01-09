"""
Кейс 1
"""


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
            # если значение число - просто просуммируем
            if isinstance(value, int) or isinstance(value, float):
                result['sum'] += value
                result[key] = value
            # если значение строка - преобразуем в число и просуммируем
            elif isinstance(value, str):
                value_is_float = False
                value_is_digit = True
                for s in value:
                    if not (s == "-" or s == '.' or s.isdigit()):
                        # в строке есть символы которых не должно быть в числе - значит в число не преобразуется
                        value_is_digit = False
                        break
                    if s == '.':
                        value_is_float = True
                # если строку можно преобразовать в число, то преобразуем в целочисленное или вещественное число,
                # а затем суммируем м добавляем ключ в результат
                if value_is_digit and value_is_float:
                    value = float(value)
                    result['sum'] += value
                    result[key] = value
                elif value_is_digit:
                    value = int(value)
                    result['sum'] += value
                    result[key] = value
                # не получилось преобразовать строку в число - выводим предупреждение и игнорируем
                # помню что никаких print, но здесь разрешено))
                else:
                    print(key, value, "(value is not a number ", type(value), ")")
            elif isinstance(value, dict):  # если значение словарь - вызовем функцию рекурсивно
                recursive_result = case1_func(**value)
                # ключи из рекурсивного результата  надо просуммировать к основному результату
                for r_key, r_value in recursive_result.items():
                    if r_key in result:
                        result[r_key] += r_value
                    else:
                        result[r_key] = r_value
            # на случай прочих типов кроме строк, чисел и словарей - выводим предупреждение и игнорируем
            # помню что никаких print, но здесь разрешено))
            else:
                print(key, value, "(value is not a number ", type(value), ")")

    return result
