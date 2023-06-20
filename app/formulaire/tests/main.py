import unittest
import ctypes, os, tempfile
from .prototype_test import PrototypesTestCase, StructsTestCase

# gcc -shared -o mini_lib.so mini_memory.c mini_string.c mini_io.c -fPIC

def load_and_test_so_file(path_to_so):
# def load_and_test_so_file():


    # mini_memory = os.path.join(path_to_so, "mini_memory.so")
    # mini_string = os.path.join(path_to_so, "mini_string.so")
    # mini_io = os.path.join(path_to_so, "mini_io.so")
    mini_lib = os.path.join(path_to_so, "mini_lib.so")

    libc = ctypes.CDLL("libc.so.6")
    mini_lib = ctypes.CDLL(mini_lib)
    # Définir la structure MYFILE correspondante
    class MYFILE(ctypes.Structure):
        _fields_ = [("fd", ctypes.c_int),
                    ("buffer_read", ctypes.c_void_p),
                    ("buffer_write", ctypes.c_void_p),
                    ("int_read", ctypes.c_int),
                    ("int_write", ctypes.c_int)]
    class MemoryTestCase(unittest.TestCase):
        # def __init__(self, methodName='runTest', file=None):
        #     super(MemoryTestCase, self).__init__(methodName)
        #     file = file
            
        def test_mini_calloc(self): 
            # Définir les arguments et le type de retour de la fonction mini_calloc
            mini_lib.mini_calloc.argtypes = [ctypes.c_int, ctypes.c_int]
            mini_lib.mini_calloc.restype = ctypes.POINTER(ctypes.c_void_p)

            # Taille et nombre d'éléments à allouer
            size = 10
            num = 4

            # Appeler mini_calloc
            ptr = mini_lib.mini_calloc(size, num)
            self.assertIsNotNone(ptr, "La fonction mini_calloc n'a pas alloué correctement la mémoire.")   

        # def test_mini_free(self): 

    class StringTestCase(unittest.TestCase):
        def test_mini_strlen(self):
            mini_lib.mini_strlen.argtypes = [ctypes.c_char_p]
            mini_lib.mini_strlen.restype = ctypes.c_int

            # Chaîne de test
            string = ctypes.c_char_p(b"Hello, world!")

            # Appeler mini_strlen
            result_mini = mini_lib.mini_strlen(string)
            result_libc = libc.strlen(string)

            self.assertEquals(result_mini, result_libc) 

        def test_mini_strcmp(self): 
            mini_lib.mini_strcmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            mini_lib.mini_strcmp.restype = ctypes.c_int

            # Chaîne de test
            string = ctypes.c_char_p(b"Hello, world!")

            result_mini = mini_lib.mini_strcmp(string, string)
            result_libc = libc.strcmp(string, string)

            self.assertEquals(result_mini, result_libc, "test_mini_strcmp n'a pas été implémentée correctement")

        def test_mini_strcmp2(self): 
            mini_lib.mini_strcmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            mini_lib.mini_strcmp.restype = ctypes.c_int

            # Chaîne de test
            string1 = ctypes.c_char_p(b"string1")
            string2 = ctypes.c_char_p(b"string2")

            result_mini = mini_lib.mini_strcmp(string1, string2)
            result_libc = libc.strcmp(string1, string2)

            self.assertEquals(result_mini, result_libc, "test_mini_strcmp n'a pas été implémentée correctement")

        def test_mini_strcpy(self): 
            mini_lib.mini_strcpy.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            mini_lib.mini_strcpy.restype = ctypes.c_int

            # Chaîne de test
            string1 = ctypes.c_char_p(b"string1")
            string2 = ctypes.c_char_p(b"")

            result_mini = mini_lib.mini_strcpy(string1, string2)

            self.assertEquals(result_mini, libc.strlen(string1), "test_mini_strcpy n'a pas été implémentée correctement")

    class IOTestCase(unittest.TestCase):
        def setUp(self):
            # Créer un fichier temporaire pour les tests
            self.file = tempfile.NamedTemporaryFile(delete=False)
            self.file.close()

        def tearDown(self):
            # Supprimer le fichier temporaire après les tests
            os.remove(self.file.name)

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

# load_and_test_so_file("/home/dini/Projet-application/app/files/so_files/dini/TP_miniglibc/src")
# load_and_test_so_file()