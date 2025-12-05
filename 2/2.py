# Программа для вычисления значения по формуле (вариант 11)
import math

print("Вычисление функции y(x) по условиям:")
print("  y = (ln(x) + 0.8)/a,   если x > 1 и a ≠ 0")
print("  y = 1/(x - a),         если x = 2 и a > 2")
print("  y = sqrt(x^2 + a^2),   если x ≤ 0")

x = float(input("\nВведите x: "))
a = float(input("Введите a: "))

if x == 2 and a > 2:
    y = 1 / (x - a)
    print(f"При x=2 и a>2 → y = {y}")
elif x > 1 and a != 0:
    y = (math.log(x) + 0.8) / a
    print(f"При x>1 и a≠0 → y = {y}")
elif x <= 0:
    y = math.sqrt(x**2 + a**2)
    print(f"При x≤0 → y = {y}")
else:
    print("Условия не выполнены. Проверьте значения x и a.")
