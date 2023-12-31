# -*- coding: utf-8 -*-
"""
Завдання 5.4b

Все, як у завданні 5.4a, але, якщо користувач ввів адресу хоста, а не адресу
мережі, треба перетворити адресу хоста на адресу мережі та вивести адресу
мережі та маску, як у завданні 5.4a.

Приклад адреси мережі (усі біти хостової частини дорівнюють нулю):
* 10.0.1.0 255.255.255.0
* 190.1.0.0 255.255.0.0

Приклад адреси хоста:
* 10.0.1.1 255.255.255.0 - хост із мережі 10.0.1.0 255.255.255.0
* 10.0.5.195 255.255.255.240 - хост із мережі 10.0.5.192 255.255.255.240

Приклад роботи завдання якщо користувач ввів адресу 10.0.1.1 255.255.255.0,

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Перевірити роботу скрипту на різних комбінаціях хост/маска, наприклад:
    10.0.5.195 255.255.255.240, 10.0.1.1 255.255.255.0

Вивід має бути впорядкований як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

Підказка: наприклад є адреса хоста у двійковому форматі та маска мережі 28.
Адреса мережі це перші 28 біт адреси хоста + 4 нуля. Тобто, наприклад, адреса
хоста 10.1.1.195/28 у двійковому форматі буде
bin_ip = "0000101000000001000000111000011"

А адреса мережі буде перших 28 символів з bin_ip + 0000 (4 тому що всього в
адресі може бути 32 біти, а 32 - 28 = 4)
00001010000000010000000111000000
"""


addresses = input('Enter ip address (format 10.1.1.0 255.255.255.0): ')
ip = addresses.split()[0].split('.')
mask = addresses.split()[1].split('.')
oct1, oct2, oct3, oct4 = [
    int(ip[0]),
    int(ip[1]),
    int(ip[2]),
    int(ip[3])
]
m1, m2, m3, m4 = [
    int(mask[0]),
    int(mask[1]),
    int(mask[2]),
    int(mask[3])
]
mask_short = str('{:b}{:b}{:b}{:b}'.format(m1, m2, m3, m4).count('1'))
template = '''{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:0>8b}  {1:0>8b}  {2:0>8b}  {3:0>8b}'''
forward = '0' * (32 - int(mask_short))
network_ip_bin = '{0:0>8b}{1:0>8b}{2:0>8b}{3:0>8b}'.format(oct1, oct2, oct3, oct4)[
    :int(mask_short)] + forward
network_ip = f"{int(network_ip_bin[:8], 2)}.{int(network_ip_bin[8:16], 2)}.{int(network_ip_bin[16:24], 2)}.{int(network_ip_bin[24:], 2)}"

print('\nNetwork:')
print(template.format(int(network_ip_bin[:8], 2), int(network_ip_bin[8:16], 2), int(network_ip_bin[16:24], 2), int(network_ip_bin[24:], 2)))
print('\nMask:')
print('/' + mask_short)
print(template.format(m1, m2, m3, m4))



