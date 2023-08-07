# -*- coding: utf-8 -*-
"""
Завдання 7.3b

Створити копію скрипта завдання 7.3a.

Переробити скрипт:
* запросити користувача ввести номер VLAN
* виводити інформацію лише за вказаним VLAN

Приклад роботи скрипта:
$ python task_7_3b.py
Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

"""
from pprint import pprint

user_vlan = input('Введіть потрібний vlan: ')

with open('CAM_table.txt') as src_file:
    for line in src_file:
        try:
            mac_len = len(line.split()[1])
        except IndexError:
            pass
        else:
            if mac_len == 14:
                vlan, mac, type, port = line.split()
                if vlan == user_vlan:
                    print(f'{vlan:<9} {mac} {port:>10}')
