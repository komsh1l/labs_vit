import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Уравнение имеет два корня:")
    print("x1 = ", x1)
    print("x2 = ", x2)
elif discriminant == 0:
    x = -b / (2 * a)
    print("Уравнение имеет один корень:")
    print("x = ", x)
else:
    print("Уравнение не имеет действительных корней.")