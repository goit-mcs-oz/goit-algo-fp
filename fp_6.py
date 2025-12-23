'''Завдання 6. Жадібні алгоритми та динамічне програмування
Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.'''


items = {
    "🍕 pizza": {"cost": 50, "calories": 300},
    "🍔 hamburger": {"cost": 40, "calories": 250},
    "🌭 hot-dog": {"cost": 30, "calories": 200},
    "🥤 pepsi": {"cost": 10, "calories": 100},
    "🥤 cola": {"cost": 15, "calories": 220},
    "🥔 potato": {"cost": 25, "calories": 350}
}


class Food:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost

    def __repr__(self):
        return f'Food({self.name}, cost:{self.cost}, calories:{self.calories}, ratio:{self.ratio})'


# Жадібний алгоритм
def greedy_algorithm(budget, food_items):
    result = []
    items = [Food(k, v['cost'], v['calories']) for k, v in food_items.items()]
    items.sort(key=lambda item: item.ratio, reverse=True)

    for item in items:
        new_budget = budget - item.cost
        if new_budget >= 0:
            result.append(item.name)
            budget = new_budget

    return result


# Динамічне програмування
def make_selection(items, budget, calories=0):
    if not items:
        return (calories, [])

    item = items.pop()
    result_include = (0, [])
    result_not_include = (0, [])

    # Берем item
    if budget - item.cost >= 0:
        result_include = make_selection(
            items.copy(), budget - item.cost, calories + item.calories)
    # Не берем item
    result_not_include = make_selection(items.copy(), budget, calories)

    if result_include[0] > result_not_include[0]:
        result_include[1].append(item.name)
        return result_include
    else:
        return result_not_include


def dynamic_programming(budget, food_items):
    result = []
    items = [Food(k, v['cost'], v['calories']) for k, v in food_items.items()]
    result = make_selection(items, budget)
    return result


budget = 100  # бюджет
print('Бюджет:', budget)

result = greedy_algorithm(budget, items)
print('Жадібний алгоритм. Результат:', result)

result = dynamic_programming(budget, items)
print('Динамічне програмування. Результат:', result)
