import unittest
import re

fileh = "/home/dini/Projet-application/app/files/so_files/dini/TP_miniglibc/src/mini_lib.h"

def search_expression(file, struct_pattern):
    with open(file, "r") as fileh:
        content = fileh.read()
        match = re.search(struct_pattern, content)
        if match:
            return True
    return False

class PrototypesTestCase(unittest.TestCase):
    # def __init__(self, methodName='runTest', fileh=None):
    #     super(PrototypesTestCase, self).__init__(methodName)
    #     fileh = fileh

    def test_prototype_mini_calloc(self):    
        # Vérifier si les prototypes sont définis
        self.assertTrue(search_expression(fileh, r"void\s*\*\s+mini_calloc\s*\(\s*int\s*,\s*int\s*\)\s*;"), "Error in declaration of mini_calloc prototype")

    def test_prototype_mini_free(self): 
        self.assertTrue(search_expression(fileh, r"void\s+mini_free\s*\(\s*void\s*\*\s*\)\s*;"), "Error in declaration of mini_free prototype")

    def test_prototype_mini_exit(self): 
        self.assertTrue(search_expression(fileh, r"void\s+mini_exit\s*\(\s*\)\s*;"), "Error in declaration of mini_exit prototype")

    def test_prototype_mini_printf(self):    
        self.assertTrue(search_expression(fileh, r"void\s+mini_printf\s*\(\s*char\s*\*\s*\)\s*;"), "Error in declaration of mini_printf prototype")

    def test_prototype_mini_scanf(self): 
        self.assertTrue(search_expression(fileh, r"int\s+mini_scanf\s*\(\s*char\s*\*\s*,\s*int\s*\)\s*;"), "Error in declaration of mini_scanf prototype")

    def test_prototype_mini_strlen(self): 
        self.assertTrue(search_expression(fileh, r"int\s+mini_strlen\s*\(\s*char\s*\*\s*\)\s*;"), "Error in declaration of mini_strlen prototype")

    def test_prototype_mini_strcpy(self): 
        self.assertTrue(search_expression(fileh, r"int\s+mini_strcpy\s*\(\s*char\s*\*\s*,\s*char\s*\*\s*\)\s*;"), "Error in declaration of mini_strcpy prototype")

    def test_prototype_mini_strcmp(self): 
        self.assertTrue(search_expression(fileh, r"int\s+mini_strcmp\s*\(\s*char\s*\*\s*,\s*char\s*\*\s*\)\s*;"), "Error in declaration of mini_strcmp prototype")

    def test_prototype_mini_fopen(self):    
        self.assertTrue(search_expression(fileh, r"MYFILE\s*\*\s+mini_fopen\s*\(\s*char\s*\*\s*,\s*char\s*\)\s*;"), "Error in declaration of mini_fopen prototype")

    def test_prototype_mini_fread(self): 
        self.assertTrue(search_expression(fileh, r"int\s+mini_fread\s*\(\s*void\s*\*\s*,\s*int\s*,\s*int\s*,\s*MYFILE\s*\*\s*\)\s*;"), "Error in declaration of mini_fread prototype")

    def test_prototype_mini_fwrite(self): 
        self.assertTrue(search_expression(fileh, r"int\s+mini_fwrite\s*\(\s*void\s*\*\s*,\s*int\s*,\s*int\s*,\s*MYFILE\s*\*\s*\)\s*;"), "Error in declaration of mini_fwrite prototype")

    def test_prototype_mini_fflush(self):    
        self.assertTrue(search_expression(fileh, r"int\s+mini_fflush\s*\(\s*MYFILE\s*\*\s*\)\s*;"), "Error in declaration of mini_fflush prototype")

    def test_prototype_mini_fgetc(self): 
        self.assertTrue(search_expression(fileh, r"int\s+mini_fgetc\s*\(\s*MYFILE\s*\*\s*\)\s*;"), "Error in declaration of mini_fgetc prototype")

    def test_prototype_mini_fputc(self): 
        self.assertTrue(search_expression(fileh, r"int\s+mini_fputc\s*\(\s*MYFILE\s*\*\s*,\s*char\s*\)\s*;"), "Error in declaration of mini_fputc prototype")

class StructsTestCase(unittest.TestCase):
    # def __init__(self, methodName='runTest', fileh=None):
    #     super(StructsTestCase, self).__init__(methodName)
    #     fileh = fileh
    
    def test_struct_malloc_element(self):    
        self.assertTrue(search_expression(fileh, r"typedef\s+struct\s+malloc_element\s*{[^}]+}\s*malloc_element;"), "Missing declaration of malloc_elemet")

    def test_struct_myfile(self):    
        self.assertTrue(search_expression(fileh, r"typedef\s+struct\s+MYFILE\s*{[^}]+}\s*MYFILE;"), "Missing declaration of MYFILE structure")