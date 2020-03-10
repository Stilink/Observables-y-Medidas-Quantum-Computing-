import sys
from os.path import dirname, join, abspath
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(0, abspath(join(dirname(__file__), '..')) + "\library")
import ComplexCalculator


# Metodo para graficar un estado con sus respectivos labels
def graph(state, labels):
    if(len(state)!=len(labels)):
        Exception("Los labels deben corresponder al tamaño del vector de estado")
    vector = []
    for i in range(len(state)):
        number = ComplexCalculator.module(state[i])**2
        vector.append(number)
    vectorX = np.array(labels)
    vectorY = np.array(vector)
    plt.bar(vectorX, vectorY)
    plt.show()