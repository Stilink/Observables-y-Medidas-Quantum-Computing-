from sys import stdin
import unittest
import ComplexCalculator
import cmath
from random import random

"""
Variable de control para los diferentes casos
(Positivos, Negativos, Positivo - Negativo, Negativo - Positivo)
"""
type=None




"""
Metodo generador de numeros complejos, retornandolos como una tupla (a,b) donde "a" representa la parte real y "b" la parte imaginaria
Es capaz de generar valores 0<=|a|<=100
Esto para tener en cuenta los casos negativos y los ceros
"""
def generatorOfComplex():
    complex_to_return = None
    if(type=="Positivos"):
        real = (random()*100)
        imag = (random()*100)
        complex_to_return = (real, imag)
    elif(type=="Negativos"):
        real = (random()*-100)
        imag = (random()*-100)
        complex_to_return = (real, imag)
    elif(type=="Positivo - Negativo"):
        real = (random()*100)
        imag = (random()*-100)
        complex_to_return = (real, imag)
    elif(type=="Negativo - Positivo"):
        real = (random()*-100)
        imag = (random()*100)
        complex_to_return = (real, imag)
    return complex_to_return






# Clase encargada de las pruebas unitarias de la calculadora
class TestComplexCalculator(unittest.TestCase):
    # Test de la suma
    def test_sum(self):
        complexGenerated = generatorOfComplex()
        complex1 = complex(complexGenerated[0], complexGenerated[1])
        complexGenerated = generatorOfComplex()
        complex2 = complex(complexGenerated[0], complexGenerated[1])
        ansOfMethodAdd = ComplexCalculator.add((complex1.real, complex1.imag), (complex2.real, complex2.imag))
        self.assertEqual(complex(ansOfMethodAdd[0], ansOfMethodAdd[1]), complex1+complex2)

    # Test de la multiplicación
    def test_mult(self):
        complexGenerated = generatorOfComplex()
        complex1 = complex(complexGenerated[0], complexGenerated[1])
        complexGenerated = generatorOfComplex()
        complex2 = complex(complexGenerated[0], complexGenerated[1])
        ansOfMethodMult = ComplexCalculator.multiply((complex1.real, complex1.imag), (complex2.real, complex2.imag))
        self.assertEqual(complex(ansOfMethodMult[0], ansOfMethodMult[1]), complex1*complex2)

    # Test de la resta
    def test_dif(self):
        complexGenerated = generatorOfComplex()
        complex1 = complex(complexGenerated[0], complexGenerated[1])
        complexGenerated = generatorOfComplex()
        complex2 = complex(complexGenerated[0], complexGenerated[1])
        ansOfMethodDiff = ComplexCalculator.difference((complex1.real, complex1.imag), (complex2.real, complex2.imag))
        self.assertEqual(complex(ansOfMethodDiff[0], ansOfMethodDiff[1]), complex1-complex2)

    # Test de la división
    def test_div(self):
        complexGenerated = generatorOfComplex()
        complex1 = complex(complexGenerated[0], complexGenerated[1])
        complexGenerated = generatorOfComplex()
        complex2 = complex(complexGenerated[0], complexGenerated[1])
        ansOfMethodDiv = ComplexCalculator.division((complex1.real, complex1.imag), (complex2.real, complex2.imag))
        # self.assertEqual(complex(ansOfMethodDiv[0], ansOfMethodDiv[1]), complex1/complex2) <==== Esto suele fallar por culpa de la presición en las operaciones por lo cual aplicaré la busqueda de un rango tolerable de diferencia con un epsilon e=0.00001
        complexDiv = complex1/complex2
        self.assertTrue(abs(ansOfMethodDiv[0]-complexDiv.real)<=0.00001 and (ansOfMethodDiv[1]-complexDiv.imag) <= 0.00001)

    # Test del modulo
    def test_mod(self):
        complexGenerated = generatorOfComplex()
        complex1 = complex(complexGenerated[0], complexGenerated[1])
        ansOfTheMethodMod = ComplexCalculator.module((complex1.real, complex1.imag))
        self.assertTrue(abs(ansOfTheMethodMod-cmath.polar(complex1)[0]) <= 0.00001)

    # Test del conjugado
    def test_conj(self):
        complexGenerated = generatorOfComplex()
        complex1 = complex(complexGenerated[0], complexGenerated[1])
        ansOfTheMethodConj = ComplexCalculator.conjugate((complex1.real, complex1.imag))
        self.assertEqual(complex(ansOfTheMethodConj[0], ansOfTheMethodConj[1]), complex1.conjugate())

    # Test cartesiano => polar
    def test_cartToPolar(self):
        complexGenerated = generatorOfComplex()
        complex1 = complex(complexGenerated[0], complexGenerated[1])
        ansOfTheMethodCartToPolar = ComplexCalculator.ConvertToPolar((complex1.real, complex1.imag))
        ansOfTheNativeMethod = cmath.polar(complex1)
        self.assertTrue((abs(ansOfTheMethodCartToPolar[0]-ansOfTheNativeMethod[0])<=0.00001) and
        (abs(ansOfTheMethodCartToPolar[1]-ansOfTheNativeMethod[1])<=0.00001))
    
    # Test polar => cartesiano
    def test_polarToCart(self):
        complexGenerated = generatorOfComplex()
        complex1 = complex(complexGenerated[0], complexGenerated[1])
        complexInPolar = cmath.polar(complex1)
        ansOfTheMethodPolarToCart = ComplexCalculator.ConverToCartesian((complexInPolar[0], complexInPolar[1]))
        self.assertTrue((abs(ansOfTheMethodPolarToCart[0]-complex1.real)<=0.00001) and 
        (abs(ansOfTheMethodPolarToCart[1]-complex1.imag))<=0.00001)

    # Test fase
    def test_phase(self):
        complexGenerated = generatorOfComplex()
        complex1 = complex(complexGenerated[0], complexGenerated[1])
        ansOfTheMethodPhase = ComplexCalculator.phase((complex1.real, complex1.imag))
        ansOfTheNativeMethod = cmath.phase(complex1)
        self.assertLessEqual(abs(ansOfTheMethodPhase-ansOfTheNativeMethod),0.00001)

cases = ["Positivos", "Negativos", "Positivo - Negativo", "Negativo - Positivo"]
print("Elija la opción que quiere probar:\n1 - Los complejos serán positivos, así: a+bi (a>=0 ^ b>=0)\n2 - Los complejos serán negativos, así: -a-bi\n3 - Los complejos tendrán su real positivo y su imaginario negativo, así: a-bi\n4 - Los complejos tendrán su real negativo y su imaginario positivo, así: -a+bi")
option = int(stdin.readline().strip())
type=cases[option-1]
unittest.main()