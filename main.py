import random
import string
def generar_contrasena(l=10):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(l))
    return contrasena

if __name__ == '__main__':
    print(generar_contrasena())