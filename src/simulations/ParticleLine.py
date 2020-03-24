import Simulations
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')) + "\library")
import ComplexCalculator
import VectorComplexCalculator
import MatrixComplexCalculator

def probabilityXi(state, i):
    number = ComplexCalculator.module(state[i])**2
    divisor = VectorComplexCalculator.norm(state)**2
    value = number/divisor
    return value


def transition(state1, state2):
    number = VectorComplexCalculator.innerProduct(state2, state1)
    divisor = VectorComplexCalculator.norm(state1) * VectorComplexCalculator.norm(state2)
    divisor = (divisor, 0)
    result = ComplexCalculator.division(number,divisor)
    return result


def expectedValue(matrix, state):
    action = MatrixComplexCalculator.actionMatrixVector(matrix,state)
    result = VectorComplexCalculator.innerProduct(action, state)
    return result

def variance(matrix, state):
    expected = expectedValue(matrix, state)
    expectedMatrix = []
    for i in range(len(matrix)):
        vector = []
        for j in range(len(matrix[0])):
            if(i==j):
                vector.append(expected)
            else:
                vector.append((0,0))
        expectedMatrix.append(vector)
    invExpectedMatrix = MatrixComplexCalculator.inverseMatrix(expectedMatrix)
    evalMatrix = MatrixComplexCalculator.addMatrix(matrix, invExpectedMatrix)
    evalMatrix = MatrixComplexCalculator.multiplyMatrix(evalMatrix, evalMatrix)
    result = expectedValue(evalMatrix, state)
    return result



def main():
    state =[
        (2,1),
        (-1,2),
        (0,1),
        (1,0),
        (3,-1),
        (2,0),
        (0,-2),
        (-2,1),
        (1,-3),
        (0,-1)
    ]
    print(probabilityXi(state, 7))
    print("-------------------------------")
    for i in range(len(state)):
        print(probabilityXi(state, i), i)

    print("------------------------")
    state2 = [
        (-1,-4),
        (2,-3),
        (-7,6),
        (-1,1),
        (-5,-3),
        (5,0),
        (5,8),
        (4,-4),
        (8,-7),
        (2,-7)
    ]
    c = transition(state, state2)
    print(transition(state, state2))


    x0 = [
        (1,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0)
    ]

    x1 = [
        (0,0),
        (1,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0)
    ]
    print("---------------------------------------------")
    result = transition(x0,x1)
    print(result)
    print("---------------------------------------------")
    state = [
        ((1/(2**0.5)),0),
        (0,(1/(2**0.5)))
    ]
    omega = [
        [(2,0),(1,1)],
        [(1,-1),(3,0)]
    ]

    print(expectedValue(omega, state))
    print("---------------------------------------------")
    print(variance(omega, state))
# main()


m = [
    [(0,0), (0,-1)],
    [(0,1),(0,0)]
]

state = [
    ((1/(2**0.5)),0),
    (0,(1/(2**0.5)))
]

print(expectedValue(m, state))
print(variance(m, state))