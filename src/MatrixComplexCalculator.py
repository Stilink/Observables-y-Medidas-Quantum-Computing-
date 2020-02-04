import VectorComplexCalculator
import ComplexCalculator

# Definición de suma de matrices
def addMatrix(A, B):
    if((len(A)!=len(B) or (len(A[0])!=len(B[0])))):
        print("La matrices deben tener igual tamaño para ser sumadas")
        raise Exception("La matrices deben tener igual tamaño para ser sumadas")
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
    
# Declaración de la adjunta de una matriz
def adjointMatrix(A):
    Matrix_result = conjugateMatrix(transposeMatrix(A))
    return Matrix_result

# Declaración de producto de dos matrices
# A x B 
def multiplyMatrix(A,B):
    # Confirmación de los tamaños para permitir la multiplicación
    if(len(A[0])!=len(B)):
        raise Exception("Matrices incompatibles")
    Matrix_result = []
    for i in range(len(A)):
        vector_result = []
        for j in range(len(B[0])):
            add = (0,0)
            for x in range(len(A[0])):
                add = ComplexCalculator.add(add, ComplexCalculator.multiply(A[i][x],B[x][j]))
            vector_result.append(add)
        Matrix_result.append(vector_result)
    return Matrix_result

# Declaración de la "acción de una matriz sobre un vector"
def actionMatrixVector(A, v):
    if len(A)!=len(A[0]) or len(A)!=len(v):
        raise Exception("La matriz y el vector no son compatibles para esta operación")
    vector_result = None;matrix_result = None # Declaramos variables
    matrix_of_vector = [];matrix_of_vector.append(v) # Convertimos el vector a una matriz para que funcione la multiplicación
    matrix_of_vector = transposeMatrix(matrix_of_vector) # Transponemos la matriz para que concuerde con la representación matematica de un vector
    matrix_result = multiplyMatrix(A,matrix_of_vector) # Multiplicamos la matriz por el vector
    vector_result = transposeMatrix(matrix_result)[0] # Primero transponemos el resultado para volver a tener un vector
    return vector_result



# Declaración del main para pruebas internas
def main():
    matrixTest = [[(1,1), (2,2)],[(3,3), (4,4)]]
    MatrixVector = [[(1,1),(2,2)]]
    matrixTest2 = [[(5,5), (6,6)],[(7,7), (8,8)]]
    matrixMultiply1=[[(1,0),(2,0),(3,0)],[(4,0),(5,0),(6,0)]]
    matrixMultiply2 = [[(7,0),(8,0)],[(9,0),(10,0)],[(11,0),(12,0)]]
    vector = [(1,1),(2,2)]

    # print(addMatrix(matrixTest, matrixTest2))
    # print(inverseMatrix(matrixTest))
    # print(scalarMatrix(2,matrixTest))
    # print(transposeMatrix(matrixTest))
    # print(conjugateMatrix(matrixTest))
    # print(adjointMatrix(matrixTest))
    # print(multiplyMatrix(matrixMultiply1, matrixMultiply2))
    print(actionMatrixVector(matrixTest, vector))

main()