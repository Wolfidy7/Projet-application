import unittest
import ctypes

libc = ctypes.CDLL("libc.so.6")

class MemoryTestCase(unittest.TestCase):
    def __init__(self, file=None):
        super().__init__()
        self.file = file
        
    def test_mini_calloc(self): 
        # Définir les arguments et le type de retour de la fonction mini_calloc
        self.file.mini_calloc.argtypes = [ctypes.c_size_t, ctypes.c_size_t]
        self.file.mini_calloc.restype = ctypes.POINTER(ctypes.c_void_p)

        # Taille et nombre d'éléments à allouer
        size = 10
        num = 4

        # Appeler mini_calloc
        result_mini = self.file.mini_calloc(size, num)
        result_libc = libc.calloc(size, num)

        # Vérifier si l'allocation a réussi
        self.assertEqual(result_mini, result_libc)   

    def test_mini_free(self):
        # Définir les arguments et le type de retour de la fonction mini_free
        self.file.mini_free.argtypes = [ctypes.c_void_p]
        self.file.mini_free.restype = None

        # Allouer un bloc de mémoire à l'aide de malloc
        size = ctypes.c_size_t(10)
        pointer = libc.malloc(size)

        # Appeler mini_free sur le bloc de mémoire
        self.file.mini_free(pointer)

        # Appeler free sur le bloc de mémoire
        libc.free(pointer)

        # Vérifier si le contenu du pointeur est égal à 0
        self.assertEqual(pointer.contents.value, 0)

#     def test_mini_exit(self):

class StringTestCase(unittest.TestCase):
    def __init__(self, file=None):
        super().__init__()
        self.file = file

    def test_mini_printf(self):
        # Définir les arguments et le type de retour de la fonction
        self.file.mini_printf.argtypes = [ctypes.c_char_p]
        self.file.mini_printf.restype = None

        # Appeler la fonction
        self.file.mini_printf(b'A')

    def test_mini_scanf(self):  
        self.file.mini_scanf.argtypes = [ctypes.c_char_p, ctypes.c_int]
        self.file.mini_scanf.restype = ctypes.c_int

        self.assertEqual(self.file.mini_scanf(), libc.scanf()) 


    def test_mini_strlen(self):
        self.file.mini_strlen.argtypes = [ctypes.c_char_p]
        self.file.mini_strlen.restype = ctypes.c_int

        # Appeler mini_strlen
        result_mini = self.file.mini_strlen('abc')
        result_libc = libc.strlen('abc')

        self.assertEqual(result_mini, result_libc) 

    def test_mini_strcpy(self): 
        self.file.mini_strcpy.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.file.mini_strcpy.restype = ctypes.c_int

    def test_mini_strcmp(self): 
        self.file.mini_strcmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.file.mini_strcmp.restype = ctypes.c_int 
class IOTestCase(unittest.TestCase):
    def __init__(self, file):
        super().__init__()
        self.file = file

    def test_mini_fopen(self):
        self.file.mini_fopen.argtypes = [ctypes.c_char_p, ctypes.c_char]
        self.file.mini_fopen.restype = ctypes.c_int  

    def test_mini_fread(self):  
        self.file.mini_fread.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.file.mini_fread.restype = ctypes.c_int  

    def test_mini_fwrite(self):
        self.file.mini_fwrite.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.file.mini_fwrite.restype = ctypes.c_int  

    def test_mini_fflush(self): 
        self.file.mini_fflush.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.file.mini_fflush.restype = ctypes.c_int   

    def test_mini_fgetc(self):  
        self.file.mini_fgetc.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.file.mini_fgetc.restype = ctypes.c_int   

    def test_mini_fputc(self):
        self.file.mini_fputc.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.file.mini_fputc.restype = ctypes.c_int 