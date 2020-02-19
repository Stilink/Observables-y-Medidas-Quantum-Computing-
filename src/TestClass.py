from sys import stdin
import MatrixComplexCalculator

def isDeterminism(M):
    flag = True
    n = len(M); m = len(M[0])
    #for i in range(n):
        # if(sum(M[i])>=2):
            # flag = False
    # if(not flag):
        # return flag
    for j in range(m):
        variable = 0
        for i in range(n):
            variable += M[i][j][0]
        if(variable>=2):
            flag = False
    return flag


# Clase que calcula el estado de un sistema, dado el sistema y el número de 'click' que se desean.
def move(M,t, state):
    # Confirmación para confirmar que la matriz tiene la lógica de una matriz determinista
    if(not isDeterminism(M)):
        raise Exception("La matriz no cumple con las condiciones de ser determinista.")
    for i in range(t):
        state = MatrixComplexCalculator.actionMatrixVector(M, state)
    return state


def move2(M1,M2,state1,state2,t):
    state1 = move(M1,t,state1)
    state2 = move(M2,t,state2)
    state1 = MatrixComplexCalculator.transposeMatrix([state1])
    state2 = MatrixComplexCalculator.transposeMatrix([state2])
    result = MatrixComplexCalculator.tensorProduct(state1,state2)
    result = MatrixComplexCalculator.transposeMatrix(result)[0]
    return result










def main():
    
    system_1 = [
        [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
        [(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)],
        [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(0,0),(0,0),(1,0),(0,0)],
        [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    ]
    # Primer test
    """
    print("Inserte la posición de la marble[0-5]:")
    position = int(stdin.readline())
    state = [(0,0) for x in range(6)]
    state[position] = (1,0)
    print("Inserte el numero de clicks a calcular:")
    t = int(stdin.readline())
    print(move(system_1, t, state))
    """

    # Segundo test
    """
    state = [(6,0),(0,0),(3,0),(5,0),(3,0),(8,0)]
    print("Inserte el numero de clicks a calcular:")
    t = int(stdin.readline())
    print(move(system, t, state))
    """

    # Tercer test
    """
    state = [(6,0),(5,0),(4,0),(3,0),(2,0),(1,0)]
    print("Inserte el numero de clicks a calcular:")
    t = int(stdin.readline())
    print(move(system, t, state))
    """





    #Segundo ejercicio - Dos sistemas Posición y personalidad

    system_2_position = [
        [(0,0),(1/6,0),(5/6,0)],
        [(1/3,0),(1/2,0),(1/6,0)],
        [(2/3,0),(1/3,0),(0,0)]
    ]

    system_2_personality = [
        [(1/3,0),(2/3,0)],
        [(2/3,0),(1/3,0)],
    ]

    # Primer Test
    # Calculado a mano

    # Segundo test
    state_position = [(1,0),(0,0),(0,0)]
    state_personality = [(0.8,0),(0.2,0)]

    # t=0
    print(move2(system_2_position,system_2_personality,state_position,state_personality,0))
    

    # t=1
    print(move2(system_2_position,system_2_personality,state_position,state_personality,1))
    

    # t=2
    print(move2(system_2_position,system_2_personality,state_position,state_personality,2))

    # t=3
    print(move2(system_2_position,system_2_personality,state_position,state_personality,3))

    # t=4
    print(move2(system_2_position,system_2_personality,state_position,state_personality,4))

    # t=5
    print(move2(system_2_position,system_2_personality,state_position,state_personality,5))
    



main()