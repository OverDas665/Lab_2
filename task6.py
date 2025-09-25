print("=== Задача 6: Количество гласных букв ===")

text = input("Введите строку: ")

glasnie = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"
count = 0

for bukva in text:
    if bukva in glasnie:
        count = count + 1

print("Количество гласных букв:", count)

