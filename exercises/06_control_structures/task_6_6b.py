# -*- coding: utf-8 -*-
"""
Завдання 6.6b

Зробити копію скрипта завдання 6.6a.
Доповнити скрипт: якщо адреса була введена неправильно, запитати адресу знову.

Якщо адреса неправильна, виводьте повідомлення: 'Wrong IP address'.
Повідомлення "Wrong IP address" має виводитися лише один раз після кожного
введення адреси, навіть якщо кілька пунктів перевірки адреси не виконано
(приклад виведення нижче).

Приклад виконання скрипту:
$ python task_6_6b.py
Enter IP address: 10.1.1.1
unicast

$ python task_6_6b.py
Enter IP address: a.a.a
Wrong IP address
Enter IP address: 10.1.1.1.1
Wrong IP address
Enter IP address: 500.1.1.1
Wrong IP address
Enter IP address: a.1.1.1
Wrong IP address
Enter IP address: 50.1.1.1
unicast

$ python task_6_6b.py
Enter IP address: 10.a.1.1.1
Wrong IP address
Enter IP address: 255.255.255.255
local broadcast

"""


import netutils.ip


def ip_check(ip):
    if not netutils.ip.is_ip(ip):
        print('Wrong IP address')
    elif ip == '255.255.255.255':
        print('local broadcast')
    elif ip == '0.0.0.0':
        print('unassigned')
    elif 1 <= int(ip.split('.')[0]) <= 223:
        print('unicast')
    elif 224 <= int(ip.split('.')[0]) <= 239:
        print('multicast')
    else:
        print('unused')


while True:
    ip = input('Enter IP address: ')
    if not netutils.ip.is_ip(ip):
        print('Wrong IP address')
    else:
        break

ip_check(ip)
