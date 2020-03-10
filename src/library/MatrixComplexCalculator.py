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

""" ERROR
# Declaración de la norma de una matriz
def normalMatrix(A):
    result = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            result += (A[i][j][0]**2)+(A[i][j][1]**2)
    result = result**0.5
    return result
"""

""" ERROR
# Declaración de la distancia entre matrices
def distanceMatrix(A,B):
    if(len(A)!=len(B) or len(A[0])!=len(B[0])):
        raise Exception("Las matrices deben tener el mismo tamaño - Distancia")
    inverse_B = inverseMatrix(B)
    difference = addMatrix(A,inverse_B)
    result = normalMatrix(difference) 
    return result
"""

# Declaración de la función que determina si una matriz es unitaria
def isUnitary(A):
    isUnitary = True
    adjoint_A = adjointMatrix(A)
    matrix_result = multiplyMatrix(A, adjoint_A)
    for i in range(len(matrix_result)):
        for j in range(len(matrix_result[0])):
            validator = ComplexCalculator.difference(matrix_result[i][j],(1,0))
            if(i==j and (abs(validator[0])>0.00001 or abs(validator[1])>0.00001)):
                isUnitary = False
                break
            if(i!=j and (abs(matrix_result[i][j][0])>0.00001 or abs(matrix_result[i][j][1])>0.00001)):
                isUnitary = False
                break
    return isUnitary

# Declaración de la función que determina si una matriz es hermitiana
def isHermitian(A):
    isHermitian = True
    matrix_result = transposeMatrix(conjugateMatrix(A))
    for i in range(len(A)):
        for j in range(len(A[0])):
            validator = ComplexCalculator.difference(A[i][j],matrix_result[i][j])
            if(abs(validator[0])>0.00001 or abs(validator[1])>0.00001):
                isHermitian=False
                break
    return isHermitian

# Declaración del producto tensor entre dos matrices
"""Este código hace la operación de multiplicar todos los elementos de la primera matriz por los elementos de la segunda.
Las matrices resultantes de cada multiplicación son enviadas a la función de llenado fill, 
la cual se encargará de acomodar en las posiciones adecuadas la información."""
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
"""Esta función simplemente se encarga de acomodar en las posiciones adecuadas, cada una de las matrices que recibe.
Teniendo en cuenta las posiciones del elemento que esta multiplicando, esta información
nos da una posición desde donde iniciar a llenar y donde debería terminar cada uno de los llenados."""

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
    # matrixTest = [[(1,0), (2,0)],[(3,0), (4,0)]]
    # MatrixVector = [[(1,1),(2,2)]]
    # matrixTest2 = [[(5,0), (6,0)],[(7,0), (8,0)]]




    # Esta variable Y es el real 1/sqrt(2)
    y = ((1/(2**0.5)),0)
    # Usando la variable anterior obtenemos la matriz H que es resultado de multiplica Y por la matriz que se ve abajo
    H=scalarMatrix(y,[
        [(1,0),(1,0)],
        [(1,0),(-1,0)]
    ])
    # Compuerta lógica X, representada por esta matriz
    X = [
        [(0,0),(1,0)],
        [(1,0),(0,0)]
    ]
    # Estado inicial del qbit 0
    q0 = [
        [(1,0)],
        [(0,0)]
    ]
    # Estado inicial del qbit 1
    q1 = [
        [(1,0)],
        [(0,0)]
    ]
    # Por ende las 'matrices' a operar saldrán de aquí
    q0_1 = tensorProduct(q0,q1) # Como matriz que representa el estado inicial de los Qbits
    M1 = tensorProduct(H,H) # Este es el primer producto tensor, resultado de tensor(H,H)=M1
    M2 = tensorProduct(H,X) # Este es el segundo producto tensor, resultado de tensor(H,X)=M2
    # Haremos entonces un M2*M1*estado_inicial
    answer = multiplyMatrix(multiplyMatrix(M2,M1),q0_1)
    for i in answer:
        print(i)
# main()