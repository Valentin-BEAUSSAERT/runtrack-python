def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  # Vérification pour éviter la division par zéro
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        return num1 % num2
    else:
        return "Opérateur non valide"

print(calcule(1, "+", 1))
print(calcule(2, "*", 2))
print(calcule(3, "/", 3))
print(calcule(4, "/", 0))
print(calcule(5, "%", 5))
print(calcule(6, "i", 6))