import VectorComplexCalculator
import ComplexCalculator

# Definición de suma de matrices
def addMatrix(A, B):
    if((len(A)!=len(B) or (len(A[0])!=len(B[0])))):
        print("La matrices deben tener igual tamaño para ser sumadas")
        return
    Matrix_result = []
    for i in range(len(A)):
        vector_result = VectorComplexCalculator.addVectors(A[i], B[i])
        Matrix_result.append(vector_result)
    return Matrix_result

# Declaración de la inversa de matrices complejas
def inverseMatrix(A):
    Matrix_result = []
    for i in range(len(A)):
        vector_result = VectorComplexCalculator.inverse(A[i])
        Matrix_result.append(vector_result)
    return Matrix_result

# Declaración de multiplicación de escalar por matriz
def scalarMatrix(a, A):
    Matrix_result = []
    for i in range(len(A)):
        vector_result = VectorComplexCalculator.multiplyScalar(a, A[i])
        Matrix_result.append(vector_result)
    return Matrix_result

# Declaración de matriz transpuesta
def transposeMatrix(A):
    m = len(A)
    n = len(A[0])
    Matrix_result = []
    for j in range(n):
        Vector_result = []
        for i in range(m):
            Vector_result.append(A[i][j])
        Matrix_result.append(Vector_result)
    return Matrix_result

# Declaración de la conjugada de una matriz
def conjugateMatrix(A):
    Matrix_result = []
    for i in range(len(A)):
        vector_result = VectorComplexCalculator.conjugateVector(A[i])
        Matrix_result.append(vector_result)
    return Matrix_result

# Declaración del main para pruebas internas
def main():
    matrixTest = [[(1,1), (2,2)],[(3,3), (4,4)]]
    MatrixVector = [[(1,1),(2,2)]]
    matrixTest2 = [[(5,5), (6,6)],[(7,7), (8,8)]]
    # print(addMatrix(matrixTest, matrixTest2))
    # print(inverseMatrix(matrixTest))
    # print(scalarMatrix(2,matrixTest))
    print(transposeMatrix(matrixTest))
    print(conjugateMatrix(matrixTest))

# main()