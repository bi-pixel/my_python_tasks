# -*- coding: utf-8 -*-
"""
Завдання 7.2b

Скопіювати код із завдання 7.2a та переробити його: замість виведення на стандартний потік виведення, скрипт повинен записати отримані рядки у файл.

Імена файлів потрібно передавати як аргументи скрипту:
1 аргумент ім'я вихідного конфігураційного файлу
2 аргумент ім'я підсумкового файлу конфігурації, в який будуть записані рядки

Приклад роботи завдання:
$ python task_7_2b.py config_sw1.txt new_config.txt

При цьому повинні бути відфільтровані рядки зі словами, які містяться в списку
ignore та рядки, що починаються на '!'.
"""

from sys import argv

ignore = ["duplex", "alias", "configuration", "end", "service"]

if len(argv) > 2:
    src_file, dst_file = argv[1], argv[2]
else:
    print('скрипт має містити 2 аргументи: старий та новий конфіг')
    exit()

config = ''
with open(src_file, 'r') as src, open(dst_file, 'w') as dst:
    for line in src:
        if not any(elem in line for elem in ignore):
            if not line.startswith('!'):
                config += (line.rstrip() + '\n')
    dst.write(config)
