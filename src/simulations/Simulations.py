from os.path import dirname, join, abspath
import sys 
from sys import stdin
sys.path.insert(0, abspath(join(dirname(__file__), '..')) + "\library")
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


def moveTwoSystemsw(M1,M2,state1,state2,t):
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
    # print(move2(system_2_position,system_2_personality,state_position,state_personality,0))
    

    # t=1
    # print(move2(system_2_position,system_2_personality,state_position,state_personality,1))
    

    # t=2
    # print(move2(system_2_position,system_2_personality,state_position,state_personality,2))

    # t=3
    # print(move2(system_2_position,system_2_personality,state_position,state_personality,3))

    # t=4
    # print(move2(system_2_position,system_2_personality,state_position,state_personality,4))

    # t=5
    # print(move2(system_2_position,system_2_personality,state_position,state_personality,5))
    
    """ Segunda actividad de clase, para comenzar usamos el mismo sistema 2 de los ejercicios anteriores.
        Por lo cual se reutilizará la matriz del sistema hecha arriba."""
    # Primer sistema de la actividad 2
    system_2_position = [
        [(0,0),(1/6,0),(5/6,0)],
        [(1/3,0),(1/2,0),(1/6,0)],
        [(2/3,0),(1/3,0),(0,0)]
    ]

    system_2_personality = [
        [(1/3,0),(2/3,0)],
        [(2/3,0),(1/3,0)],
    ]


    # Primer ejercicio
    state_position = [(0.01,0),(0.9,0),(0.09,0)]
    state_personality = [(0.05,0),(0.95,0)]

    # print(move2(system_2_position, system_2_personality, state_position, state_personality,2))

    # Segundo ejercicio - Se mantienen los estados iniciales
    # print(move2(system_2_position,system_2_personality,state_position,state_personality,8000))

    """
    M = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [1,0,0,0,1,0],
        [0,0,0,1,0,0],
        [0,1,0,0,0,1],
        [0,0,1,0,0,0]
    ]
    result = MatrixComplexCalculator.multiplyMatrix(MatrixComplexCalculator.adjointMatrix(M),M)
    for x in result:
        print(x)
    # Quiz
    state_initial=[(1/5,0),(7/10,0),(1/10,0)]
    print(move(system_2_position, 4, state_initial))
    x = (1/(2**0.5))
    M = [
        [(x,0),(0,x)],
        [(x,0),(0,-x)]
    ]
    state = [(1,0),(0,0)]
    print(move(M,1,state))
    """
    """
    x = (1/(2**0.5))
    r = (1/(6**0.5))
    M=[
        [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(x,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(x,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(-r,r),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(-r,-r),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
        [(0,0),(r,-r),(-r,r),(0,0),(0,0),(1,0),(0,0),(0,0)],
        [(0,0),(0,0),(-r,-r),(0,0),(0,0),(0,0),(1,0),(0,0)],
        [(0,0),(0,0),(r,-r),(0,0),(0,0),(0,0),(0,0),(1,0)]
    ]
    state = [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    print(move(M,2,state)[5])
    """















    """
    x=1/(2**0.5)
    y = 1/(6**0.5)
    double_slit = [
        [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(x,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(x,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(-y,y),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(-y,-y),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
        [(0,0),(y,-y),(-y,y),(0,0),(0,0),(1,0),(0,0),(0,0)],
        [(0,0),(0,0),(-y,-y),(0,0),(0,0),(0,0),(1,0),(0,0)],
        [(0,0),(0,0),(y,-y),(0,0),(0,0),(0,0),(0,0),(1,0)]        
    ]
    initial_state = [
        (1,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0)
    ]
    state_click_1 = move(double_slit, 1, initial_state)
    state_click_2 = move(double_slit, 2, initial_state)
    print("State in 1 click:")
    for i in state_click_1:
        print(i)
    print("State in 2 clicks:")
    for i in state_click_2:
        print(i)
    """
    
# main()


m = [
    [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
    [(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
    [(0,0),(0,0),(0,0),(0,0),(0,0),(1,0)],
    [(0,0),(0,0),(0,0),(0,0),(1,0),(0,0)],
    [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
    [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
]

s = [
    (4,0),
    (1,0),
    (5,0),
    (3,0),
    (10,0),
    (2,0)
]

#result = move(m, 3, s)
#for i in result:
    #print(i)


m = [
    [(2/15,0),(7/15,0),(6/15,0)],
    [(9/15,0),(5/15,0),(1/15,0)],
    [(4/15,0),(3/15,0),(8/15,0)]
]

s = [
    (0,0),
    (1,0),
    (0,0)
]

# print(move(m,1,s))



m = [
    [(1/(2**0.5),0),(0,1/(2**0.5)),(0,0)],
    [(1/(2**0.5),0),(0,-1/(2**0.5)),(0,0)],
    [(0,0),(0,0),(0,-1)]
]

s=[
    (0,1),
    (0,0),
    (0,0)
]

# print(move(m,2,s))

m = [
    [(0,0),(1/6,0),(5/6)],
    [(1/3,0),(1/2,0),()]
]