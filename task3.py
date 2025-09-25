print("=== Задача 3: Сумма чисел от 1 до N ===")

n = int(input("Введите число N: "))

summa = 0
i = 1

while i <= n:
    summa = summa + i
    i = i + 1

print("Сумма чисел от 1 до", n, "равна:", summa)

