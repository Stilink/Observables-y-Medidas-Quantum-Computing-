import ComplexCalculator
import VectorComplexCalculator
import TestComplexCalculator

# Casos para los numeros
cases = ["Positivos", "Negativos", "Positivo - Negativo", "Negativo - Positivo"]


# Generador de vectores usados dentro de las pruebas
def generatorOfVectors(type, n):
    vector_to_return = []
    for i in range(n):
        vector_to_return.append(TestComplexCalculator.generatorOfComplex(type))
    return vector_to_return


# Clase encargada de los test a la calculadora de vectores complejos
class TestVectorComplexCalculator(unittest.TestCase):
