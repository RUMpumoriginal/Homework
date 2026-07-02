input = [int(x) for x in input("Введіть кількість місячних опадів: ").split()]


def main ():
    suma = sum(input)
    mid = suma / len(input)
    maxi = max(input)
    mini = min(input)

    print("Сума опадів:", suma)
    print("Середнє значення опадів:", mid) 
    print("Максимальне значення опадів:", maxi)
    print("Мінімальне значення опадів:", mini)

main()

