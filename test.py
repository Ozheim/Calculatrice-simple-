def calculatrice():
    operation = input("Choisis une opération (+, -, *, /): ")
    num1 = float(input("Premier nombre: "))
    num2 = float(input("Deuxième nombre: "))

    if operation == '+':
        print(f"Le résultat est: {num1 + num2}")
    elif operation == '-':
        print(f"Le résultat est: {num1 - num2}")
    elif operation == '*':
        print(f"Le résultat est: {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"Le résultat est: {num1 / num2}")
        else:
            print("Division par zéro n'est pas permise.")
    else:
        print("Opération invalide.")

calculatrice()
