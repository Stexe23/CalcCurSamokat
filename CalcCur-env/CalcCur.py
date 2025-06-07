"""В этой функции описывается работа по вычислению заработка за отработанное время,
а так же в зависимоти от доствленных заказов"""

def itog() -> int:

    print('Ставка в час: ')
    ratesHour = int(input())  # Ставка в час

    print('Количество часов: ')
    hours = int(input())    # Количество часов

    print('Ствка SLA15: ')
    SLA15Order = int(input())  # Ствка за заказ SLA15

    print('SLA15: ')
    SLA15 = int(input())  # Количество заказов SLA15

    print('Ствка SLA30: ')
    SLA30Order = int(input())  # Ствка за заказ SLA30

    print('SLA30: ')
    SLA30 = int(input())  # Количество заказов SLA30

    print('Ствка SLA60: ')
    SLA60Order = int(input())  # Ствка за заказ SLA60

    print('SLA60: ')
    SLA60 = int(input())  # Количество заказов SLA60

    print('Ствка тяжёлый: ')
    hardOrder = int(input())  # Ствка за тяжёлый заказ

    print('SLA15: ')
    hard = int(input())  # Количество тяжёлых заказов

    # Итого = "Ставка в час" * "Часы" + "Ставка за заказ" * "Количество заказов"
    s = hours * ratesHour + (SLA15 * SLA15Order + SLA30 * SLA30Order + SLA60 * SLA60Order + hard * hardOrder)

    return s



print('Итого за день: ',itog(),'руб')
