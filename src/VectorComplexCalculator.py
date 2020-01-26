import ComplexCalculator

# Comprobación de seguridad
def checkingSize(a,b):
    if(len(a)!=len(b)):
        return False
    else:
        return True
        
# Definición de suma de vectores
def addVectors(a,b):
    if(checkingSize(a,b)):
        n = len(a)
    else:
        print("Aquí debería estallarse y mentarle su madre al de los vectores")
        return
    vector_result = []
    for i in range(n):
        ai = a[i]
        bi = b[i]
        addition=ComplexCalculator.add(ai, bi)
        vector_result.append(addition)
    return vector_result

# Definición de inversa de vectores
def invert(a):
    vector_result = []
    for i in range(len(a)):
        vector_result.append((-1*a[0],-1*a[1]))
    return vector_result

# Definición de la multiplicación por un escalar de vectores
def multiplyScalar(c, vector):
    vector_result = []
    for i in range(len(vector)):
        result = ComplexCalculator.multiply(c, vector[i])
        vector_result.append(result)
    return vector_result

# Definición del main para pruebas internas
def main():
    