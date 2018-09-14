# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    # Умножаем number на 10^ndigits
    big_number = number*10**ndigits
    # Проверяем остаток и округляем через отбрасывание остатка
    if (big_number%1 >= 0.5):
        big_number = big_number - big_number%1 + 1
    else:
        big_number -= big_number%1
    # Делим big_number на 10^ndigits
    number_round = big_number/10**ndigits
    return number_round

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    str_ticket_number=str(ticket_number)
    a,b=0,0
    for i in range(len(str_ticket_number)//2):
        a += int(str_ticket_number[i])
        b += int(str_ticket_number[-1-i])
    return 'lucky' if a==b else 'not lucky'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))