# Результаты шахматного турнира
# Каждая строка — один игрок, значения: 1 (победа), 0.5 (ничья), 0 (поражение)

rezultaty = [
    [1, 0.5, 1, 0],      # Иванов
    [0, 1, 0.5, 1],      # Петров
    [0.5, 0, 0, 0.5],    # Сидоров
    [1, 1, 1, 0.5],      # Кузнецов
    [0, 0, 0.5, 0]       # Смирнов
]

imena = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов"]

# Шаг 1: Посчитаем очки и выигрыши
ochki = []
vyigryshi = []
vsego_igr = len(rezultaty[0])  # предполагаем, что у всех одинаковое число игр

for i in range(len(rezultaty)):
    summa = sum(rezultaty[i])
    wins = rezultaty[i].count(1)
    ochki.append(summa)
    vyigryshi.append(wins)

# Шаг 2: Найдём максимальные очки (победитель)
max_ochki = max(ochki)

# Шаг 3: Выводим результаты
print("Результаты турнира:\n")

for i in range(len(imena)):
    imya = imena[i]
    summa = ochki[i]
    wins = vyigryshi[i]
    
    # Победитель?
    pobeditel = "Да" if summa == max_ochki else "Нет"
    
    # Более половины выигрышей?
    bolshe_poloviny = "Да" if wins > vsego_igr / 2 else "Нет"
    
    print(f"{imya}: очков = {summa}, выигрышей = {wins}, победитель = {pobeditel}, >50% выигрышей = {bolshe_poloviny}")

# Дополнительно: покажем только победителя и тех, кто выиграл >50% партий
print("\n--- Итог ---")
print("Победитель(и):")
for i in range(len(imena)):
    if ochki[i] == max_ochki:
        print("  -", imena[i])

print("\nИгроки, выигравшие более половины игр:")
for i in range(len(imena)):
    if vyigryshi[i] > vsego_igr / 2:
        print("  -", imena[i])
