import unittest
import MatrixComplexCalculator
import TestVectorComplex
import VectorComplexCalculator
import cmath

# Casos para los numeros
cases = ["Positivos", "Negativos", "Positivo - Negativo", "Negativo - Positivo"]

# Tamaño por defecto del vector para las pruebas
n = 100
m = 100

# Generador de matrices para las pruebas
def generatorOfMatrix(type, nl, ml):
    matrix_to_return=[]
    for i in range(n):
        matrix_to_return.append(TestVectorComplex.generatorOfVectors(type, m))
    return matrix_to_return


# Clase para realizar las pruebas de la calculadora de matrices complejas
class TestMatrixCalculator(unittest.TestCase):

    # Prueba para la adición de matrices
    def test_add_matrix(self):
        for case in cases:
            matrix1 = generatorOfMatrix(case, n, m)
            matrix2 = generatorOfMatrix(case, n, m)
            matrix_result = MatrixComplexCalculator.addMatrix(matrix1, matrix2)
            matrix_to_compare = []
            for i in range(len(matrix1)):
                matrix_to_compare.append(VectorComplexCalculator.addVectors(matrix1[i], matrix2[i]))
            self.assertEqual(matrix_result, matrix_to_compare)

    # Prueba para confirmar el funcionamiento del inverso aditivo de una matriz
    def test_inverse_matrix(self):
        for case in cases:
            matrix1 = generatorOfMatrix(case, n, m)
            matrix_result = MatrixComplexCalculator.inverseMatrix(matrix1)
            matrix_to_compare = []
            for i in range(len(matrix1)):
                vector = []
                for j in range(len(matrix1[0])):
                    vector.append((-1*matrix1[i][j][0],-1*matrix1[i][j][1]))
                matrix_to_compare.append(vector)
            self.assertEqual(matrix_result, matrix_to_compare)

    # Prueba para multiplicación escalar por una matriz
    def test_scalar_matrix(self):
        for case in cases:
            matrix1 = generatorOfMatrix(case, n, m)
            scalar = TestVectorComplex.generatorRandomNumber(case)
            matrix_result = MatrixComplexCalculator.scalarMatrix(scalar, matrix1)
            matrix_to_compare = []
            for i in range(len(matrix1)):
                vector = []
                for j in range(len(matrix1[0])):
                    scalarT = complex(scalar[0],scalar[1])
                    number = complex(matrix1[i][j][0],matrix1[i][j][1])
                    result = scalarT*number
                    vector.append((result.real,result.imag))
                matrix_to_compare.append(vector)
            self.assertEqual(matrix_result, matrix_to_compare)

    # Prueba para la transpuesta de una matriz
    def test_transpose_matrix(self):
        matrix1 = generatorOfMatrix(cases[0], n, m)
        matrix_result = MatrixComplexCalculator.transposeMatrix(matrix1)
        matrix_to_compare = []
        for j in range(len(matrix1[0])):
            Vector_result = []
            for i in range(len(matrix1)):
                Vector_result.append(matrix1[i][j])
            matrix_to_compare.append(Vector_result)
        self.assertEqual(matrix_result, matrix_to_compare)

    # Prueba de la conjugada de una matriz
    def test_conjugate_matrix(self):
        for case in cases:
            matrix1 = generatorOfMatrix(case, n, m)
            matrix_result = MatrixComplexCalculator.conjugateMatrix(matrix1)
            matrix_to_compare = []
            for i in range(len(matrix1)):
                vector = []
                for j in range(len(matrix1[0])):
                    vector.append((matrix1[i][j][0], -1*matrix1[i][j][1]))
                matrix_to_compare.append(vector)
            self.assertEqual(matrix_result, matrix_to_compare)
    
    # Prueba para el producto tensor
    def test_tensor_product(self):
        return 

if __name__ == "__main__":
    unittest.main()