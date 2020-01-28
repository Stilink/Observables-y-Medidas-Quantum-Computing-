from sys import stdin
import math

# En este caso las tuplas representarán a los complejos.
# La primera parte de la tupla representará la parte Real del complejo
# mientras que la segunda parte de la tupla hará las veces de la parte imaginaria.

# Definición de la suma
def add(a, b):
    real_result = (a[0]+b[0])
    imaginary_result = (a[1]+b[1])
    return (real_result, imaginary_result)

# Definición de la resta
# Pensado de manera que al primero se le restará el segundo valor.
# Es decir: difference(a, b) ===> (a-b)
def difference(a, b):
    real_result = (a[0]-b[0])
    imaginary_result = (a[1]-b[1])
    return (real_result, imaginary_result)

# Definición de la multiplicación
def multiply(a, b):
    real_result = ((a[0]*b[0])-(a[1]*b[1]))
    imaginary_result = ((a[0]*b[1])+(a[1]*b[0]))
    return (real_result, imaginary_result)

# Definición de la división
def division(a, b):
    real_result = ((a[0]*b[0])+(a[1]*b[1]))/((b[0]**2)+(b[1]**2))
    imaginary_result = ((b[0]*a[1])-(a[0]*b[1]))/((b[0]**2)+(b[1]**2))
    return (real_result, imaginary_result)

# Definición del conjugado
def conjugate(a):
    return (a[0], a[1]*-1)

# Definición del modulo
def module(a):
    return ((a[0]**2)+(a[1]**2))**(1/2)

# Conversión a coordenadas polares. Cartesiano ===> Polares
def ConvertToPolar(a):
    r = module(a)
    ang = math.atan2(a[1], a[0])
    return (r, ang)

# Conversión de forma cartesiana a coordenadas polares. Polares ===> Cartesiano
def ConverToCartesian(a):
    r = a[0]
    ang = a[1]
    real_result = r*math.cos(ang)
    imaginary_result = r*math.sin(ang)
    return (real_result, imaginary_result)

# Metodo para obtener la fase de un complejo
def phase(a):
    result = ConvertToPolar(a)[1]
    return result

# Declaración del main para pruebas internas.
def main():
    complex_1 = (int(stdin.readline()), int(stdin.readline()))
    complex_2 = (int(stdin.readline()), int(stdin.readline()))
    print(add(complex_1, complex_2))
    print(difference(complex_1, complex_2))

# main()