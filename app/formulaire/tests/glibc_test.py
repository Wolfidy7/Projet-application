import unittest
import ctypes
from .prototype_test import PrototypesTestCase, StructsTestCase

a ="/home/dini/Projet-application/app/files/so_files/dini/TP_miniglibc/src/mini_memory.so"
b = "/home/dini/Projet-application/app/files/so_files/dini/TP_miniglibc/src/mini_memory.so"
c = "/home/dini/Projet-application/app/files/so_files/dini/TP_miniglibc/src/mini_memory.so"

def load_and_test_so_file(path):

    # Importez la bibliothèque C
    libc = ctypes.CDLL("libc.so.6")
    mini_memory = ctypes.CDLL(path + "mini_memory.so")
    mini_string = ctypes.CDLL(path + "mini_string.so")
    mini_io = ctypes.CDLL(path + "mini_io.so")

    class MemoryTestCase(unittest.TestCase):
        def test_mini_calloc(self): 
            # Définir les arguments et le type de retour de la fonction mini_calloc
            mini_memory.mini_calloc.argtypes = [ctypes.c_size_t, ctypes.c_size_t]
            mini_memory.mini_calloc.restype = ctypes.POINTER(ctypes.c_void_p)

            # Taille et nombre d'éléments à allouer
            size = 10
            num = 4

            # Appeler mini_calloc
            result_mini = mini_memory.mini_calloc(size, num)
            result_libc = libc.calloc(size, num)

            # Vérifier si l'allocation a réussi
            self.assertEqual(result_mini, result_libc)   

        # def test_mini_free(self):
        #     # Définir les arguments et le type de retour de la fonction mini_free
        #     mini_memory.mini_free.argtypes = [ctypes.c_void_p]
        #     mini_memory.mini_free.restype = None

        #     # Allouer un bloc de mémoire à l'aide de malloc
        #     size = ctypes.c_size_t(10)
        #     pointer = libc.malloc(size)

        #     # Appeler mini_free sur le bloc de mémoire
        #     mini_memory.mini_free(pointer)

        #     # Appeler free sur le bloc de mémoire
        #     libc.free(pointer)

        #     # Vérifier si le contenu du pointeur est égal à 0
        #     self.assertEqual(pointer.contents.value, 0)

    #     def test_mini_exit(self):

    class StringTestCase(unittest.TestCase):
        def test_mini_printf(self):
            # Définir les arguments et le type de retour de la fonction
            mini_string.mini_printf.argtypes = [ctypes.c_char_p]
            mini_string.mini_printf.restype = None

            # Appeler la fonction
            mini_string.mini_printf(b'A')

        def test_mini_scanf(self):  
            mini_string.mini_scanf.argtypes = [ctypes.c_char_p, ctypes.c_int]
            mini_string.mini_scanf.restype = ctypes.c_int

            self.assertEqual(mini_string.mini_scanf(), libc.scanf()) 


        def test_mini_strlen(self):
            mini_string.mini_strlen.argtypes = [ctypes.c_char_p]
            mini_string.mini_strlen.restype = ctypes.c_int

            # Appeler mini_strlen
            result_mini = mini_memory.mini_strlen('abc')
            result_libc = libc.strlen('abc')

            self.assertEqual(result_mini, result_libc) 

        def test_mini_strcpy(self): 
            mini_string.mini_strcpy.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            mini_string.mini_strcpy.restype = ctypes.c_int

        def test_mini_strcmp(self): 
            mini_string.mini_strcmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            mini_string.mini_strcmp.restype = ctypes.c_int  

    class IOTestCase(unittest.TestCase):
        def test_mini_fopen(self):
            mini_io.mini_fopen.argtypes = [ctypes.c_char_p, ctypes.c_char]
            mini_io.mini_fopen.restype = ctypes.c_int  

        def test_mini_fread(self):  
            mini_io.mini_fread.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            mini_io.mini_fread.restype = ctypes.c_int  

        def test_mini_fwrite(self):
            mini_io.mini_fwrite.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            mini_io.mini_fwrite.restype = ctypes.c_int  

        def test_mini_fflush(self): 
            mini_io.mini_fflush.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            mini_io.mini_fflush.restype = ctypes.c_int   

        def test_mini_fgetc(self):  
            mini_io.mini_fgetc.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            mini_io.mini_fgetc.restype = ctypes.c_int   

        def test_mini_fputc(self):
            mini_io.mini_fputc.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            mini_io.mini_fputc.restype = ctypes.c_int 

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