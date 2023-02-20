"""
Задание №8
    Погружение в Python | Коллекции
    ✔ Три друга взяли вещи в поход. Сформируйте
    словарь, где ключ — имя друга, а значение —
    кортеж вещей. Ответьте на вопросы:
    ✔ Какие вещи взяли все три друга
    ✔ Какие вещи уникальны, есть только у одного друга
    ✔ Какие вещи есть у всех друзей кроме одного
    и имя того, у кого данная вещь отсутствует
    ✔ Для решения используйте операции
    с множествами. Код должен расширяться
    на любое большее количество друзей.
"""

friends = {
    'Первый друг': ('телефон', 'карта', 'яблоко', 'лодка'),
    'Второй друг': ('телефон', 'хлеб', 'карта', 'лодка'),
    'Третий друг': ('телефон', 'хлеб', 'карта', 'шапка'),
}

sets_list = [set(v) for v in friends.values()]

# Какие вещи взяли все три друга
result_set = set.intersection(*sets_list)
print(f'Вещи, которые взяли все три друга: {result_set}')

# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
friends_cnt = len(sets_list)

for item in set.union(*sets_list):
    cnt = 0
    for s in sets_list:
        if item in s:
            cnt += 1
    if cnt == 1:
        print(f'Вещь "{item}" есть только у одного из друзей')
    if cnt == friends_cnt-1:
        for k, v in friends.items():
            if item not in set(v):
                print(f'Вещи "{item}" нет только у {k}')
