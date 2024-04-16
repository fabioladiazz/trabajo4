import random
import string
def generar_contrasena(l=10):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(l))
    return contrasena

def contadorNumeros():
    numero = int(input("Ingrese su numero:"))
    for valor in range(1,numero+1):
        print(valor)

def calculadora_basica():
    operacion = input("Ingrese la operación a realizar (+, -, *, /): ")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = "Error: División por cero." if num2 == 0 else num1 / num2
    else:
        resultado = "Operación no válida"
    return resultado

def saludo():
    name = str(input("Ingrese su nombre:"))
    print(f"Hola {name}")

if __name__ == '__main__':
    print(generar_contrasena())
    print(contadorNumeros())
    print (calculadora_basica())
    print(saludo())


