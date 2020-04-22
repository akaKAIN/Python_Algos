"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой,
проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0

k = (y1-y2) / (x1-x2)
b = y2-k*x2
"""
import sys

POINT_X_A = 0
POINT_Y_A = 0
POINT_X_B = 0
POINT_Y_B = 0
K_VAL, B_VAL = 0, 0

try:
    POINT_X_A = int(input("Enter X-coordinate of point A: "))
    POINT_Y_A = int(input("Enter Y-coordinate of point A: "))
    POINT_X_B = int(input("Enter X-coordinate of point B: "))
    POINT_Y_B = int(input("Enter Y-coordinate of point B: "))
except ValueError:
    print("Wrong coordinate of point")
    sys.exit(1)

try:
    K_VAL = (POINT_X_A - POINT_X_B) / (POINT_Y_A - POINT_Y_B)
except ZeroDivisionError:
    print("Wrong coordinate of point")
    sys.exit(1)

B_VAL = POINT_Y_B - K_VAL * POINT_X_B
print(f'equation: y = {K_VAL}x{B_VAL:+}')
