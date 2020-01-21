import VectorComplexCalculator
# Definición de suma de matrices
def addMatrix(A, B):
    if(not (len(A)==len(B) && (len(A[0])==len(B[0])))):
        print("La matrices deben ser iguales para ser sumadas")
        return
    Matrix_result = [[]]
    for i in range(len(A)):
        vector_result = VectorComplexCalculator.addVectors(A[1], B[1])