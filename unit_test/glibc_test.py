import unittest
import ctypes
import os

libc = ctypes.CDLL("libc.so.6")
mini_lib = ctypes.CDLL("/home/dini/Projet-application/app/files/so_files/dini/TP_miniglibc/src/mini_lib.so")
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
    def test_mini_fopen(self):
        mini_lib.mini_fopen.argtypes = [ctypes.c_char_p, ctypes.c_char]
        mini_lib.mini_fopen.restype = MYFILE

        file = b"README.txt"  # Fichier de test
        mode = b"r"        # Mode de test

        # Appeler la fonction mini_fopen et obtenir la structure MYFILE
        myfile = mini_lib.mini_fopen(file, mode)

        # Vérifier si la structure MYFILE a été correctement créée
        self.assertEqual(myfile.file, os.open(file.decode(), os.O_RDWR))

        # Fermer le fichier
        os.close(myfile.file)  

        

    def test_mini_fread(self):  
        mini_lib.mini_fread.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        mini_lib.mini_fread.restype = ctypes.c_int  



