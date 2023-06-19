import unittest
from prototype_test import PrototypesTestCase, StructsTestCase
from glibc_test import MemoryTestCase, StringTestCase, IOTestCase
# gcc -shared -o votre_bibliotheque.so mini_memory.c -fPIC
# pour obtenir bilan complet
# python -m unittest discover -s tests -p "test_*.py"

if __name__ == '__main__':
    # Charger les classes de tests
    test_classes = [PrototypesTestCase, StructsTestCase, MemoryTestCase, StringTestCase, IOTestCase]
    
    # Créer un TestSuite
    suite = unittest.TestSuite()
    for test_class in test_classes:
        suite.addTest(unittest.makeSuite(test_class))
    
    # Exécuter les tests et obtenir les résultats
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    # Afficher le bilan des tests
    print("\n==== Bilan des tests ====")
    print("Tests exécutés : ", result.testsRun)
    print("Erreurs : ", len(result.errors))
    print("Échecs : ", len(result.failures))
    print("Passés : ", result.testsRun - len(result.errors) - len(result.failures))
