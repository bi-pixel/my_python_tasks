# -*- coding: utf-8 -*-
"""
Завдання 7.3a

Зробити копію скрипта завдання 7.3.

Переробити скрипт: Відсортувати вивід за номером VLAN

В результаті має вийти такий вивід:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Зверніть увагу на vlan 1000 – він повинен виводитися останнім. Правильне
сортування можна досягти, якщо vlan буде числом, а не рядком.

Підказка: Для сортування зручно спочатку створити список списків такого типу, а
потім сортувати (зверніть увагу на те, що VLAN число).

[[100, '01bb.c580.7000', 'Gi0/1'],
 [200, '0a4b.c380.7c00', 'Gi0/2'],
 [300, 'a2ab.c5a0.700e', 'Gi0/3'],
 [10, '0a1b.1c80.7000', 'Gi0/4'],
 [500, '02b1.3c80.7b00', 'Gi0/5'],
 [200, '1a4b.c580.7000', 'Gi0/6'],
 [300, '0a1b.5c80.70f0', 'Gi0/7'],
 [10, '01ab.c5d0.70d0', 'Gi0/8'],
 [1000, '0a4b.c380.7d00', 'Gi0/9']]

Сортування має бути за першим елементом (vlan), і якщо перший елемент
однаковий, то з другого. Так працює за замовчуванням функція sorted та метод
sort, якщо сортувати перелік списків вище.
"""
from pprint import pprint
output = []
# with open('CAM_table.txt') as src_file:
#     for line in src_file:
#         try:
#             mac_len = len(line.split()[1])
#         except IndexError:
#             pass
#         else:
#             if mac_len == 14:
#                 vlan, mac, type, port= line.split()
#                 output.append(f'{int(vlan):9} {mac} {port:>10}')

# output.sort()
# for line in output:
#     line = line.split()
#     print(f'{line[0]:9} {line[1]} {line[2]:>10}')

with open('CAM_table.txt') as src_file:
    for line in src_file:
        try:
            mac_len = len(line.split()[1])
        except IndexError:
            pass
        else:
            if mac_len == 14:
                vlan, mac, type, port = line.split()
                output.append([int(vlan), mac, port])
 
for vlan, mac, port in sorted(output):
    print(f'{vlan:<9} {mac} {port:>10}')

