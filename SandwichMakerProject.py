# SandwichMakerProject.py - проект pyinputplus

import pyinputplus as pyip

# Цены на компоненты сэндвича
prices = {
    'bread': {'wheat': 10, 'white': 8, 'sourdough': 12},
    'protein': {'chicken': 20, 'turkey': 25, 'ham': 15, 'tofu': 18},
    'cheese': {'cheddar': 10, 'swiss': 12, 'mozzarella': 14},
    'extras': {'mayo': 5, 'mustard': 3, 'lettuce': 4, 'tomato': 4},
}

# Запрашиваем у пользователя тип хлеба
bread_choice = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt="Choose your bread type:\n", numbered=True)

# Запрашиваем у пользователя тип белка
protein_choice = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt="Choose your protein type:\n", numbered=True)

# Спрашиваем, хочет ли пользователь сыр
wants_cheese = pyip.inputYesNo("Do you want cheese? (yes/no)\n")

cheese_choice = None
if wants_cheese == 'yes':
    # Запрашиваем тип сыра
    cheese_choice = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], prompt="Choose your cheese type:\n", numbered=True)

# Спрашиваем про дополнительные ингредиенты
extras = []
for extra in ['mayo', 'mustard', 'lettuce', 'tomato']:
    if pyip.inputYesNo(f"Do you want {extra}? (yes/no)\n") == 'yes':
        extras.append(extra)

# Спрашиваем, сколько сэндвичей хочет пользователь
num_sandwiches = pyip.inputInt("How many sandwiches do you want?\n", min=1)

# Подсчет общей стоимости
total_cost = (prices['bread'][bread_choice] + prices['protein'][protein_choice]) * num_sandwiches

if cheese_choice:
    total_cost += prices['cheese'][cheese_choice] * num_sandwiches

for extra in extras:
    total_cost += prices['extras'][extra] * num_sandwiches

# Вывод общей стоимости
print(f"\nYour total cost is: {total_cost} currency units for {num_sandwiches} sandwich(es).")
