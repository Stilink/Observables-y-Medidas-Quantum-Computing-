import Simulations

def booleanMarbles(Matrix, initialState, clicks):
    # Lo primero a hacer es acomodar la matriz a una que podamos manejar
    matrix = convertMatrix(Matrix)
    # Lo siguiente será arreglar el estado inicial, pues del mismo modo que con la matriz probablemente tengamos un vector de booleanos o reales
    vectorInitial = converVector(initialState)
    # Ahora simplemente procedemos a procesar
    result = Simulations.move(matrix,vectorInitial, clicks) 
    return result




# Pasa una matriz de booleanos a una matriz de complejos
# para que pueda ser procesada por la libreria
def convertMatrix(Matrix):
    matrix_result = []
    for i in Matrix:
        vector_result = []
        for j in i:
            number = (j, 0)
            vector_result.append(number)
        matrix_result.append(vector_result)
    return matrix_result

# Pasa un vector de booleanos a un vector de complejos
# con el fin de que puedan ser procesados por la libreria
def converVector(vector):
    vector_result = []
    for i in vector:
        number = (i,0)
        vector_result.append(number)
    return number