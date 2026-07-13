raw_input = [x for x in input("Введіть кількість місячних опадів: ").split()]
months = ["січень", "лютий", "березень", "квітень", "травень", "червень", "липень", "серпень", "вересень", "жовтень", "листопад", "грудень"]

try:
    input = [int(x) for x in raw_input]

except ValueError:
    print("Будь ласка, введіть числа через пробіл.")
    exit()

def main ():
    suma = sum(input)
    mid = suma / len(input)
    maxi = str(max(input)) + " - " + months[input.index(max(input))]
    mini = str(min(input)) + " - " + months[input.index(min(input))]

    print("Сума опадів:", suma)
    print("Середнє значення опадів:", mid) 
    print("Максимальне значення опадів:", maxi)
    print("Мінімальне значення опадів:", mini)

main()

