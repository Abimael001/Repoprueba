def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No es posible dividir entre cero."

while True:
    print("\n*** Calculadora ***")
    # print("1. Suma")
    print("otras opciones")
    print("2. Resta")
    print("4. División")
    print("5. Salir")
    print("6. esta es una linea de prueba para la opcion salir")
    print("7. otra prueba")

    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = suma(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = resta(num1, num2)
        print("El resultado de la resta es:", resultado)
    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = multiplicacion(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = division(num1, num2)
        print("El resultado de la división es:", resultado)
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
