from django.test import TestCase
import unittest
import re
import ctypes

def load_and_test_so_file(so_file_path):
    # Chargez le module partagé
    example = ctypes.CDLL(so_file_path)

    # Définissez le prototype de la fonction
    #example.add.restype = ctypes.c_int
    #example.add.argtypes = [ctypes.c_int, ctypes.c_int]

    # Classe de test pour la fonction "add"
    class AddTestCase(unittest.TestCase):
        def add(self):
            result = example.add(2, 3)
            self.assertEqual(result, 5)

        def test_add_2(self):
            result = example.add(-2, -3)
            self.assertEqual(result, -5)

        def test_add_3(self):
            result = example.add(0, 0)
            self.assertEqual(result, 0)

    # Créez une suite de tests à partir de la classe de test
    test_suite = unittest.TestLoader().loadTestsFromTestCase(AddTestCase)

    # Exécutez les tests
    unittest.TextTestRunner().run(test_suite)


