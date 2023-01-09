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

    result = 0
    for key, value in dict_data.items():
        if key.find("sum") != -1:
            type_value = type(value)
            if type_value == int or type_value == float:
                print(key, value)
                result += value
            else:
                print(key, value, "(value is not a number ", type_value, ")")
    print("sum =", result)
