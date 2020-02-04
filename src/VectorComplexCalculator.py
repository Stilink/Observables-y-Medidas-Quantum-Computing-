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
        print("Los vectores deben tener tamaños iguales si se desea sumarlos")
        return
    vector_result = []
    for i in range(n):
        ai = a[i]
        bi = b[i]
        addition=ComplexCalculator.add(ai, bi)
        vector_result.append(addition)
    return vector_result

# Definición de inversa de vectores
def inverse(a):
    vector_result = []
    for i in range(len(a)):
        vector_result.append((-1*a[i][0],-1*a[i][1]))
    return vector_result

# Definición de la multiplicación por un escalar de vectores
def multiplyScalar(c, vector):
    vector_result = []
    for i in range(len(vector)):
        result = ComplexCalculator.multiply(c, vector[i])
        vector_result.append(result)
    return vector_result

# Declaración del conjugado de un vector
def conjugateVector(a):
    vector_result = []
    for i in a:
        result = ComplexCalculator.conjugate(i)
        vector_result.append(result)
    return vector_result

# Declaración del producto interno de dos vectores
def innerProduct(a,b):
    if(len(a)!=len(b)):
        raise Exception("Los vectores deben tener el mismo tamaño para poder calcular el producto interno")
    complex_result = None
    a = conjugateVector(a)
    add = (0,0)
    for i in range(len(a)):
        add = ComplexCalculator.add(add, ComplexCalculator.multiply(a[i],b[i]))
    return add
    

# Definición del main para pruebas internas
def main():
    vectorTest=[(1,1),(2,2),(3,3)]
    vectorTest2=[(4,4),(5,5),(6,6)]
    # print(addVectors(vectorTest, vectorTest2))
    # print(inverse(vectorTest))
    # print(multiplyScalar(2, vectorTest))
    # print(conjugateVector(vectorTest))
    print(innerProduct(vectorTest, vectorTest2))
# main()
    