import math

def calcular_hipotenusa(a, b):
    return math.sqrt(a**2 + b**2)

def calcular_cateto(a, c):
    return math.sqrt(c**2 - a**2)

def calcular_cateto_b(b, c):
    return math.sqrt(c**2 - b**2)

def main():
    opcion = input("¿Qué deseas calcular? (c, a o b): ")

    if opcion == "c":
        a = float(input("Ingresa el valor de a: "))
        b = float(input("Ingresa el valor de b: "))
        hipotenusa = calcular_hipotenusa(a, b)
        print("La hipotenusa es:", hipotenusa)
    elif opcion == "a":
        b = float(input("Ingresa el valor de b: "))
        c = float(input("Ingresa el valor de c: "))
        cateto_a = calcular_cateto(b, c)
        print("El cateto a es:", cateto_a)
    elif opcion == "b":
        a = float(input("Ingresa el valor de a: "))
        c = float(input("Ingresa el valor de c: "))
        cateto_b = calcular_cateto_b(a, c)
        print("El cateto b es:", cateto_b)
