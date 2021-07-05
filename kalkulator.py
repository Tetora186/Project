print("Witaj w moim kalkulatorze.\nJakie działanie będziesz chciał przeprowadzać?")

while(True):
    znak = input("+ dodawanie, - odejmowanie, * mnożenie, / dzielenie, x zakończ ")

    if (znak == '+'):
        print(int(input("Wprowadź 1. liczbę: ")) + int(input("Wprowadź 2. liczbę: ")))

    elif (znak == '-'):
        print(int(input("Wprowadź 1. liczbę: ")) - int(input("Wprowadź 2. liczbę: ")))

    elif (znak == '*'):
        print(int(input("Wprowadź 1. liczbę: ")) * int(input("Wprowadź 2. liczbę: ")))

    elif (znak == '/'):
        print(int(input("Wprowadź 1. liczbę: ")) / int(input("Wprowadź 2. liczbę: ")))
    
    elif (znak == 'x'):
        break

    else:
        print("Nierozpoznana funkcja")