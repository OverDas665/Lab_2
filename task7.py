print("=== Задача 7: Разворот строки ===")

text = input("Введите строку: ")

perevernutiy_text = ""
i = len(text) - 1

while i >= 0:
    perevernutiy_text = perevernutiy_text + text[i]
    i = i - 1

print("Перевернутая строка:", perevernutiy_text)

