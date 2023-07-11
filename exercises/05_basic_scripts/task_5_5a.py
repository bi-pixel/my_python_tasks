# -*- coding: utf-8 -*-
"""
Завдання 5.5a

Доповнити скрипт із завдання 5.5 таким чином, щоб, залежно від вибраного
режиму, задавалися різні запитання у запиті про номер VLAN або список VLANів:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter the allowed VLANs:'

Плюсом буде вирішити завдання без використання умови if та циклу for, але
перший варіант рішення краще зробити так, як виходитиме.
"""

access_template = """switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

trunk_template = """switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
"""

questions = {'access': 'Enter VLAN number: ', 'trunk': 'Enter the allowed VLANs: '}

mode = input('режим інтерфейсу (access або trunk): ')
interface = input('інтерфейс (тип та номер, виду Gi0/3): ')
vlan = input(questions[mode])

template = {'access': access_template, 'trunk': trunk_template}
print(f'\ninterface {interface}')
print(template[mode].format(vlan))