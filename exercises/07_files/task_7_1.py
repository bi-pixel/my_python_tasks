# -*- coding: utf-8 -*-
"""
Завдання 7.1

Обробити рядки з файлу ospf.txt і вивести інформацію щодо кожного рядка в
такому вигляді на стандартний потік виводу:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

"""
with open('ospf.txt') as file:
    data = file.readlines()

template = '{:22} {}\n' * 5

for line in data:
    prefix = line.split()[1]
    metric = line.split()[2].strip('[]')
    hop = line.split()[4].strip(',')
    update = line.split()[5].strip(',')
    interface = line.split()[6]
    print(template.format(
        'Prefix', prefix,
        'AD/Metric', metric,
        'Next-Hop', hop,
        'Last update', update,
        'Outbound Interface', interface
    ))
