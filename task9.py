print("=== Задача 9: Сумма элементов массива ===")

numbers_input = input("Введите числа через пробел: ")
numbers = numbers_input.split()

chisla = []
for chislo_str in numbers:
    chisla.append(float(chislo_str))

summa = 0
for chislo in chisla:
    summa = summa + chislo

print("Массив:", chisla)
print("Сумма элементов:", summa)

