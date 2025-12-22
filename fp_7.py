'''Завдання 7. Використання методу Монте-Карло
Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.'''


import random


def monte_carlo_simulation(num_experiments):
    sum_count = {x: 0 for x in range(2, 13)}
    for _ in range(num_experiments):
        sum = random.randint(1, 6) + random.randint(1, 6)
        sum_count[sum] = sum_count[sum] + 1

    sum_probability = {k: 100*v/num_experiments for k, v in sum_count.items()}

    print(f'{'Сума':<5} Імовірність')
    for k, v in sum_probability.items():
        print(f'{k:<5} {round(v, 2)}')


monte_carlo_simulation(1000000)
