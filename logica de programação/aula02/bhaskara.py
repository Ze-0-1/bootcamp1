import math
#x=(-b+-rais -4a*c)/2a      x²-1x-3=0



a = float(input("Digite o valor de a"))
b = float(input("Digite o valor de b"))
c = float(input("Digite o valor de c"))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('raiz real não existente')
if delta == 0:
    x1 = (-b) / (2 * a)
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / 2
    x2 = (-b - math.sqrt(delta)) / 2

    print(f"x1={x1}")
    print(f"x2={x2}")
