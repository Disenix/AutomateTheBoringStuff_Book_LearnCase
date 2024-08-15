# проект чат GPT на вопрос о методах выравнивания текста
# productsTable.py - практический проект

#список продуктов
items = [
    ["Apple", 10, 0.5],
    ["Banana", 5, 0.3],
    ["Cherry", 50, 0.2],
    ["Date", 100, 1.0]
]
# Создание строки с заголовками для каждого столбца, выровненного по центру
headers = ["Item", "Quantity", "Price"]
headerLine = " | ".join(header.center(10) for header in headers)
print(headerLine)
print("-" * len(headerLine))

# форматируем строки для каждого товара
# выравнивание по левому краю для названия товаров
# по правому для количества и цены
for item in items:
    name = item[0].ljust(10)
    quantity = str(item[1]).rjust(10)
    price = f"${item[2]:.2f}".rjust(10)
    line = f"{name} | {quantity} | {price}"

    print(line)






""" items = [
    ["Apple", 10, 0.5],
    ["Banana", 5, 0.3],
    ["Cherry", 50, 0.2],
    ["Date", 100, 1.0]
]

headers = ["Item", "Quantity", "Price"]
header_line = " | ".join(header.center(10) for header in headers)
print(header_line)
print("-" * len(header_line))  # Линия под заголовками

total_quantity = 0
total_cost = 0.0

for item in items:
    name = item[0].ljust(10)
    quantity = item[1]
    price = item[2]
    cost = quantity * price

    total_quantity += quantity
    total_cost += cost

    line = f"{name} | {str(quantity).rjust(10)} | {f'${cost:.2f}'.rjust(10)}"
    print(line)

# Добавляем итоговую строку "Total"
print("-" * len(header_line))  # Линия под итогами
total_line = f"{'Total'.ljust(10)} | {str(total_quantity).rjust(10)} | {f'${total_cost:.2f}'.rjust(10)}"
print(total_line)
"""
