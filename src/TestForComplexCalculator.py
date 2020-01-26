import unittest
import ComplexCalculator
import cmath
from random import random

# Clase encargada de las pruebas unitarias de la calculadora
class TestComplexCalculator(unittest.TestCase):
    # Test de la suma
    def test_sum(self):
        complex1 = complex((random()*100), (random()*100))
        complex2 = complex((random()*100), (random()*100))
        ansOfMethodAdd = ComplexCalculator.add((complex1.real, complex1.imag), (complex2.real, complex2.imag))
        self.assertEqual(complex(ansOfMethodAdd[0], ansOfMethodAdd[1]), complex1+complex2)

    # Test de la multiplicación
    def test_mult(self):
        complex1 = complex((random()*100), (random()*100))
        complex2 = complex((random()*100), (random()*100))
        ansOfMethodMult = ComplexCalculator.multiply((complex1.real, complex1.imag), (complex2.real, complex2.imag))
        self.assertEqual(complex(ansOfMethodMult[0], ansOfMethodMult[1]), complex1*complex2)

    # Test de la resta
    def test_dif(self):
        complex1 = complex((random()*100), (random()*100))
        complex2 = complex((random()*100), (random()*100))
        ansOfMethodDiff = ComplexCalculator.difference((complex1.real, complex1.imag), (complex2.real, complex2.imag))
        self.assertEqual(complex(ansOfMethodDiff[0], ansOfMethodDiff[1]), complex1-complex2)

    # Test de la división
    def test_div(self):
        complex1 = complex((random()*100), (random()*100))
        complex2 = complex((random()*100), (random()*100))
        ansOfMethodDiv = ComplexCalculator.division((complex1.real, complex1.imag), (complex2.real, complex2.imag))
        # self.assertEqual(complex(ansOfMethodDiv[0], ansOfMethodDiv[1]), complex1/complex2) <==== Esto suele fallar por culpa de la presición en las operaciones por lo cual aplicaré la busqueda de un rango tolerable de diferencia con un epsilon e=0.00001
        complexDiv = complex1/complex2
        self.assertTrue(abs(ansOfMethodDiv[0]-complexDiv.real)<=0.00001 and (ansOfMethodDiv[1]-complexDiv.imag) <= 0.00001)

    # Test del modulo
    def test_mod(self):
        complex1 = complex((random()*100), (random()*100))
        ansOfTheMethodMod = ComplexCalculator.module((complex1.real, complex1.imag))
        self.assertTrue(abs(ansOfTheMethodMod-cmath.polar(complex1)[0]) <= 0.00001)

    # Test del conjugado
    def test_conj(self):
        complex1 = complex((random()*100), (random()*100))
        ansOfTheMethodConj = ComplexCalculator.conjugate((complex1.real, complex1.imag))
        self.assertEqual(complex(ansOfTheMethodConj[0], ansOfTheMethodConj[1]), complex1.conjugate())

    # Test cartesiano => polar
    def test_cartToPolar(self):
        complex1 = complex((random()*100), (random()*100))
        ansOfTheMethodCartToPolar = ComplexCalculator.ConvertToPolar((complex1.real, complex1.imag))
        ansOfTheNativeMethod = cmath.polar(complex1)
        self.assertTrue((abs(ansOfTheMethodCartToPolar[0]-ansOfTheNativeMethod[0])<=0.00001) and
        (abs(ansOfTheMethodCartToPolar[1]-ansOfTheNativeMethod[1])<=0.00001))
    
    # Test polar => cartesiano
    def test_polarToCart(self):
        complex1 = complex((random()*100), (random()*100))
        complexInPolar = cmath.polar(complex1)
        ansOfTheMethodPolarToCart = ComplexCalculator.ConverToCartesian((complexInPolar[0], complexInPolar[1]))
        self.assertTrue((abs(ansOfTheMethodPolarToCart[0]-complex1.real)<=0.00001) and 
        (abs(ansOfTheMethodPolarToCart[1]-complex1.imag))<=0.00001)

    # Test fase
    def test_phase(self):
        complex1 = complex((random()*100), (random()*100))
        ansOfTheMethodPhase = ComplexCalculator.phase((complex1.real, complex1.imag))
        ansOfTheNativeMethod = cmath.phase(complex1)
        self.assertLessEqual(abs(ansOfTheMethodPhase-ansOfTheNativeMethod),0.00001)


if __name__ == "__main__":
    unittest.main()
