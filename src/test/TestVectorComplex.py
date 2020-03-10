from os.path import dirname, join, abspath
import sys
import unittest
import random
sys.path.insert(0, abspath(join(dirname(__file__), '..')) + "\library")
import ComplexCalculator
import VectorComplexCalculator
import TestComplexCalculator


# Casos para los numeros
cases = ["Positivos", "Negativos", "Positivo - Negativo", "Negativo - Positivo"]


# Tamaño por defecto del vector para las pruebas
n = 100
# Generador de vectores usados dentro de las pruebas
def generatorOfVectors(case, n):
    vector_to_return = []
    for i in range(n):
        vector_to_return.append(TestComplexCalculator.generatorOfComplex(case))
    return vector_to_return

# Generador de un numero aleatorio necesario en algunos metodos
def generatorRandomNumber(case):
    comp = TestComplexCalculator.generatorOfComplex(case)
    return comp


# Clase encargada de los test a la calculadora de vectores complejos
class TestVectorComplexCalculator(unittest.TestCase):
    # Test de la suma de vectores
    def test_add_vector(self) :
        for case in cases:
            vector1 = generatorOfVectors(case,n)
            vector2 = generatorOfVectors(case,n)
            vector_result = VectorComplexCalculator.addVectors(vector1, vector2)
            vector_to_compare = []
            for i in range(n):
                vector_to_compare.append(ComplexCalculator.add(vector1[i],vector2[i]))
            self.assertEqual(vector_result, vector_to_compare)

    # Test del metodo que retorna el inverso aditivo de un vector
    def test_inverse(self):
        for case in cases:
            vector1 = generatorOfVectors(case,n)
            vector_result = VectorComplexCalculator.inverse(vector1)
            vector_to_compare = []
            for i in range(n):
                vector_to_compare.append((-1*vector1[i][0], -1*vector1[i][1]))
            self.assertEqual(vector_result, vector_to_compare)

    # Test de la multiplicación de un escalar por un vector
    def test_scalar_product(self):
        for case in cases:
            number = generatorRandomNumber(random.choice(cases))
            vector1 = generatorOfVectors(case,n)
            vector_result = VectorComplexCalculator.multiplyScalar(number, vector1)
            vector_to_compare =[]
            for i in range(n):
                vector_to_compare.append(ComplexCalculator.multiply(number,vector1[i]))
            self.assertEqual(vector_to_compare, vector_result)
    
    # Test para el conjugado de un vector
    def test_conjugate(self):
        for case  in cases:
            vector1 = generatorOfVectors(case, n)
            vector_result = VectorComplexCalculator.conjugateVector(vector1)
            vector_to_compare = []
            for i in range(n):
                vector_to_compare.append(ComplexCalculator.conjugate(vector1[i]))
            self.assertEqual(vector_result, vector_to_compare)



if __name__ == "__main__":
    unittest.main()
            