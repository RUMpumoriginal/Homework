number = input("Ведіть чотирьох значне ціле число: ")


def main(num):
    try:
        num = int(num)
    
    except ValueError:
        print("Ведіть чотирьох значне ціле число!!!")
        exit()

    list = [int(char) for char in str(number)]

    if num <= 9999 and len(list) == 4:
        
        return print(len(list) == len(set(list)))
    else:
         return print("Ведіть чотирьох значне ціле число!!!")

main(number)
