import unittest
import ctypes, os
from prototype_test import PrototypesTestCase, StructsTestCase
from glibc_test import MemoryTestCase, StringTestCase, IOTestCase

def load_and_test_so_file(path_to_so):

    mini_memory = os.path.join(path_to_so, "mini_memory.so")
    mini_string = os.path.join(path_to_so, "mini_string.so")
    mini_io = os.path.join(path_to_so, "mini_io.so")
    mini_h = os.path.join(path_to_so, "mini_lib.h")

    # Créer la suite de tests
    suite = unittest.TestSuite()

    # Ajouter les classes de tests en fonction de la disponibilité des fichiers
    if os.path.exists(mini_h):
        suite.addTest(unittest.makeSuite(PrototypesTestCase))
        suite.addTest(unittest.makeSuite(StructsTestCase))
    if os.path.exists(mini_memory):
        suite.addTest(unittest.makeSuite(MemoryTestCase))
    if os.path.exists(mini_string):
        suite.addTest(unittest.makeSuite(StringTestCase))
    if os.path.exists(mini_io):
        suite.addTest(unittest.makeSuite(IOTestCase))

    # Exécuter les tests et obtenir les résultats
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Afficher le bilan des tests
    print("\n==== Bilan des tests ====")
    print("Tests exécutés : ", result.testsRun)
    print("Erreurs : ", len(result.errors))
    print("Échecs : ", len(result.failures))
    print("Passés : ", result.testsRun - len(result.errors) - len(result.failures))

load_and_test_so_file("/home/dini/Projet-application/app/files/so_files/dini/TP_miniglibc/src")