print("Найдём порядковые номера чисел, кратных 3.")
print("Введите числа через пробел:")

# Вводим массив
chisla = list(map(int, input().split()))

# Выбор способа
print("\nКаким способом проверить?")
print("1 — через цикл FOR")
print("2 — через цикл WHILE аналог repeat")

vybor = input("Ваш выбор (1 или 2): ")

print("\nПорядковые номера элементов, кратных 3:")

if vybor == "1":
    # Решение через FOR
    for i in range(len(chisla)):
        if chisla[i] % 3 == 0:
            print(i + 1)

elif vybor == "2":
    # Решение через WHILE
    i = 0
    while i < len(chisla):
        if chisla[i] % 3 == 0:
            print(i + 1)
        i += 1

else:
    print("Неизвестный выбор. Запустите программу снова и введите 1 или 2.")
