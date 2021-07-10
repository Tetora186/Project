<<<<<<< HEAD
print("Witaj w moim kalkulatorze.\nJakie działanie będziesz chciał przeprowadzać?")

while(True):
    znak = input("+ dodawanie, - odejmowanie, * mnożenie, / dzielenie, ** podnieś do potęgi, x zakończ ")

    if (znak == '+'):
        print(float(input("Wprowadź 1. liczbę: ")) + float(input("Wprowadź 2. liczbę: ")))

    elif (znak == '-'):
        print(float(input("Wprowadź 1. liczbę: ")) - float(input("Wprowadź 2. liczbę: ")))

    elif (znak == '*'):
        print(float(input("Wprowadź 1. liczbę: ")) * float(input("Wprowadź 2. liczbę: ")))

    elif (znak == '/'):
        print(float(input("Wprowadź 1. liczbę: ")) / float(input("Wprowadź 2. liczbę: ")))

    elif (znak == '**'):
        print(float(input("Wprowadź liczbę: ")) ** float(input("Do jakiej potęgi podnieść liczbę: ")))

    elif (znak == 'x'):
        break

    else:
=======
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
>>>>>>> e3a2eeaaddce6d61c7d6a1b5c03bc2eabb318a5f
        print("Nierozpoznana funkcja")