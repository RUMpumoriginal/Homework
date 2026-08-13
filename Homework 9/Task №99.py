k = input("Введіть кількість рядків в одній сторінці: ")
n = input("Введіть ваш номер рядка: ")


def main(k, n):
    try:
        k = int(k)
        n = int(n)

    except ValueError:
       print("Будьласка вводьте цілі числа")
       exit()


    print(f"Page: {(n // k) + 1}, line: {n % k}")

main(k, n)