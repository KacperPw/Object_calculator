class Calculator():
    def plus(self, a, b):
        result = a+b
        print(result)
    def minus(self, a, b):
        result = a - b
        print(result)
calc = Calculator()

operation = input("Wybierz działanie: \n Dodawanie: \n Odejmowanie: ")
if operation == "Dodawanie":
    calc.plus(int(input("Podaj 1 liczbę: ")), int(input("Podaj 2 liczbę: ")))
elif operation == "Odejmowanie":
    calc.minus(int(input("Podaj 1 liczbę: ")), int(input("Podaj 2 liczbę: ")))
else:
    print("Nieprawidłowy operator")
    