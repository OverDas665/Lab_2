print("=== Задача 8: Максимум в массиве ===")

numbers_input = input("Введите числа через пробел: ")
numbers = numbers_input.split()

chisla = []
for chislo_str in numbers:
    chisla.append(float(chislo_str))

max_chislo = chisla[0]
for chislo in chisla:
    if chislo > max_chislo:
        max_chislo = chislo

print("Массив:", chisla)
print("Максимальное число:", max_chislo)

