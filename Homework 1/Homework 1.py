a = input("Введіть числа через пробіл: ")

d = [int(x) for x in a.split()]
b = max(d)
c = d.index(b)

print("Найбільше число:", b, "Індекс числа:", c)
