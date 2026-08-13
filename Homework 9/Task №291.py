number = input("Ведіть ціле число: ")


def main(num):
    try:
        num = int(num)
    
    except ValueError:
        print("Ведіть ціле число!!!")
        exit()

    list = [int(char) for char in str(number)]
    item = len(list)
    result = 0

    while item != 0:
        result = (result * 10) + list[item - 1]
        item -= 1

    return print(result)

main(number)
