print("=== Задача 10: Поиск элемента в массиве ===")

numbers_input = input("Введите числа через пробел: ")
numbers = numbers_input.split()

chisla = []
for chislo_str in numbers:
    chisla.append(float(chislo_str))

x = float(input("Введите число для поиска: "))

naideno = False
for chislo in chisla:
    if chislo == x:
        naideno = True
        break

if naideno:
    print("Число", x, "найдено в массиве!")
else:
    print("Число", x, "не найдено в массиве!")

