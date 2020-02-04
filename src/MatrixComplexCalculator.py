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

# Declaración de la norma de una matriz
def normalMatrix(A):
    result = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            result += (A[i][j][0]**2)+(A[i][j][1]**2)
    result = result**0.5
    return result

# Declaración de la distancia entre matrices
def distanceMatrix(A,B):
    return 

# Declaración de la función que determina si una matriz es unitaria
def isUnitary(A):
    return False

# Declaración de la función que determina si una matriz es hermitiana
def isHermitian(A):
    return False

# Declaración del producto tensor entre dos matrices
def tensorProduct(A,B):
    n = len(A)*len(B)
    m = len(A[0])*len(B[0])
    matrix_result = [[0 for x in range(m)] for y in range(n)]
    for i in range(len(A)):
        for j in range(len(A[0])):
            matrix_temp = scalarMatrix(A[i][j],B)
            fill(matrix_temp, matrix_result, i, j)
    return matrix_result

# Función auxiliar para el producto tensor
def fill(A, matrix_result, x, y):
    n = len(A)
    m = len(A[0])
    ii=0;jj=0
    for i in range((n*x),n*(x+1)):
        for j in range((m*y),m*(y+1)):
            matrix_result[i][j]=A[ii][jj]
            jj+=1
        jj=0
        ii+=1
    
# Declaración del main para pruebas internas
def main():
    """
    matrixTest = [[(1,0), (2,0)],[(3,0), (4,0)]]
    MatrixVector = [[(1,1),(2,2)]]
    matrixTest2 = [[(5,0), (6,0)],[(7,0), (8,0)]]
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
    # print(actionMatrixVector(matrixTest, vector))
    # print(normalMatrix(matrixTest))
    print(tensorProduct(matrixTest, matrixTest2))
    """
    y = ((1/(2**0.5)),0)
    H=scalarMatrix(y,[
        [(1,0),(1,0)],
        [(1,0),(-1,0)]
    ])
    X = [
        [(0,0),(1,0)],
        [(1,0),(0,0)]
    ]
    q0 = [
        [(1,0)],
        [(0,0)]
    ]
    q1 = [
        [(1,0)],
        [(0,0)]
    ]
    q0_1 = tensorProduct(q0,q1)
    print(q0_1)
    M1 = tensorProduct(H,H)
    for i in M1:
        print(i)
    M2 = tensorProduct(H,X)
    for i in M2:
        print(i)
    # Haremos entonces un M2*M1*estado_inicial
    answer = multiplyMatrix(multiplyMatrix(M2,M1),q0_1)
    for i in answer:
        print(i)

main()