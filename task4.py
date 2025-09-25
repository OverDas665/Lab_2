print("=== Задача 4: Таблица умножения ===")

n = int(input("Введите число N: "))

print("Таблица умножения для числа", n)
i = 1
while i <= 10:
    result = n * i
    print(n, "×", i, "=", result)
    i = i + 1
    
    