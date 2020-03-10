import Simulations
import BarGraph


# Simulación del double slit experiment probabilistic, lo que busca recibir es el numero de rendijas
# el numero de targets a la que cada rendija puede acceder, y un vector de triplas que relacione una rendija especifica con un target y una probabilidad
# dicho vector deberá ser así "[ [slit, target, probability] ]"
def slitExperimentProbabilistic(slits, targets, probabilityToTargets):
    matrix = createMatrixProbabilistic(slits, targets, probabilityToTargets)
    vector = [(0,0) for x in range(len(matrix))]
    vector[0] = (1,0)
    print("Estado del sistema en un click de tiempo:")
    for i in Simulations.move(matrix, 1, vector):
        print(i)
    print("________________________________________________")
    print("Estado del sistema en dos clicks de tiempo:")
    result = Simulations.move(matrix, 2, vector)
    for i in result:
        print(i)
    print("________________________________________________")
    return result

def createMatrixProbabilistic(slits, targets, probabilityToTargets):
    # Para calcular el numero de targets a usar en la matriz que representa el estado
    # haremos el siguiente proceso
    nTargets = 0
    ts = set()
    for i in probabilityToTargets:
        if(not i[1] in ts):
            ts.add(i[1])
            nTargets+=1

    matrix_result = makeMatrixFilledWithZeros(slits, nTargets)
    # Una vez conocemos el numero de targets, podemos darnos a la tarea de armar la matriz.
    # Sin embargo, dicho proceso al completo puede resultar complejo así que es mejor armarla por partes
    
    # La primera parte que haremos será llenar la posición 0
    for i in range(1,slits+1):
        number = 1/(slits)
        matrix_result[i][0] = (number, 0)

    # Una vez hecho esto tendremos llenada la sección del origen a las rendijas

    # Ahora queremos llenar la sección de las rendijas a los targets
    # Para esto haremos uso del vector que trae las probabilidades
    for i in probabilityToTargets:
        matrix_result[i[1]][i[0]]=(i[2],0)

    # Para terminar tenemos que llenar la sección de los targets a si mismos
    for i in range(1+slits, 1+slits+nTargets):
        matrix_result[i][i]=(1,0)
    return matrix_result


# Crea la matriz del tamaño indicado por el usuario llena de complejos (0,0)
# Esto con el fin de que sea llenada de acuerdo a necesidades
def makeMatrixFilledWithZeros(slits, nTargets):
    matrix = [[(0,0) for x in range(1+slits+nTargets)] for y in range(1+slits+nTargets)]
    return matrix





# Simulación del double slit experiment probabilistic, lo que busca recibir es el numero de rendijas
# el numero de targets a la que cada rendija puede acceder, y un vector de triplas que relacione una rendija especifica con un target y una probabilidad
# dicho vector deberá ser así "[ [slit, target, probability] ]"
def slitExperimentQuantum(slits, targets, probabilityToTargets):
    matrix = createMatrixQuantum(slits, targets, probabilityToTargets)
    vector = [(0,0) for x in range(len(matrix))]
    vector[0] = (1,0)
    print("Estado del sistema en un click de tiempo:")
    for i in Simulations.move(matrix, 1, vector):
        print(i)
    print("________________________________________________")
    print("Estado del sistema en dos clicks de tiempo:")
    result = Simulations.move(matrix, 2, vector)
    for i in result:
        print(i)
    print("________________________________________________")
    return result

def createMatrixQuantum(slits, targets, probabilityToTargets):
     # Para calcular el numero de targets a usar en la matriz que representa el estado
    # haremos el siguiente proceso
    nTargets = 0
    ts = set()
    for i in probabilityToTargets:
        if(not i[1] in ts):
            ts.add(i[1])
            nTargets+=1

    matrix_result = makeMatrixFilledWithZeros(slits, nTargets)
    # Una vez conocemos el numero de targets, podemos darnos a la tarea de armar la matriz.
    # Sin embargo, dicho proceso al completo puede resultar complejo así que es mejor armarla por partes
    
    # La primera parte que haremos será llenar la posición 0
    for i in range(1,slits+1):
        number = 1/(slits**0.5)
        matrix_result[i][0] = (number, 0)

    # Una vez hecho esto tendremos llenada la sección del origen a las rendijas

    # Ahora queremos llenar la sección de las rendijas a los targets
    # Para esto haremos uso del vector que trae las probabilidades
    for i in probabilityToTargets:
        matrix_result[i[1]][i[0]]= i[2]

    # Para terminar tenemos que llenar la sección de los targets a si mismos
    for i in range(1+slits, 1+slits+nTargets):
        matrix_result[i][i]=(1,0)
    return matrix_result

# defined for testing
def main():
    print("Quantum:")
    print()
    result = slitExperimentQuantum(2,3,[[1,3,(0,1/(3**0.5))],[1,4,(0,1/(3**0.5))],[1,5,(0,1/(3**0.5))],[2,5,(0,1/(3**0.5))],[2,6,(0,1/(3**0.5))],[2,7,(0,1/(3**0.5))]])
    labels = ["0","1","2","3","4","5","6","7"]
    BarGraph.graph(result, labels)
main()