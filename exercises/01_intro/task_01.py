"""
Якщо запустити код завдання, на екран буде виведено:
$ python task_01.py
Python is a high-level, interpreted, general-purpose programming language.

Необхідно змінити рядок start_data таким чином, щоб на екран було виведено
$ python task_01.py
Ruby is a high-level, interpreted, general-purpose programming language.

При цьому не можна змінювати рядок start_data вручну, тільки за допомогою Python.
"""
start_data = "Python is a high-level, interpreted, general-purpose programming language."
print(start_data)


def end_zeros(a: int) -> int:
    # your code here
    a = str(a)
    result = 0
    count = len(a) - 1
    while count >= 0:
        if a[count] == '0':
            result += 1
        count -= 1
    return result


print(end_zeros(00))
