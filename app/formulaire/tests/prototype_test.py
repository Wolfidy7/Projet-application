import unittest
import re

def search_expression(file, struct_pattern):
    with open(file, "r") as file:
        content = file.read()
        match = re.search(struct_pattern, content)
        if match:
            return True
    return False

class PrototypesTestCase(unittest.TestCase):
    def __init__(self, file):
        super().__init__()
        self.file = file

    def test_prototype_mini_calloc(self):    
        # Vérifier si les prototypes sont définis
        self.assertTrue(search_expression(self.file, r"void\s*\*\s+mini_calloc\s*\(\s*int\s*,\s*int\s*\)\s*;"))

    def test_prototype_mini_free(self): 
        self.assertTrue(search_expression(self.file, r"void\s+mini_free\s*\(\s*void\s*\*\s*\)\s*;"))

    def test_prototype_mini_exit(self): 
        self.assertTrue(search_expression(self.file, r"void\s+mini_exit\s*\(\s*\)\s*;"))

    def test_prototype_mini_printf(self):    
        self.assertTrue(search_expression(self.file, r"void\s+mini_printf\s*\(\s*char\s*\*\s*\)\s*;"))

    def test_prototype_mini_scanf(self): 
        self.assertTrue(search_expression(self.file, r"int\s+mini_scanf\s*\(\s*char\s*\*\s*,\s*int\s*\)\s*;"))

    def test_prototype_mini_strlen(self): 
        self.assertTrue(search_expression(self.file, r"int\s+mini_strlen\s*\(\s*char\s*\*\s*\)\s*;"))

    def test_prototype_mini_strcpy(self): 
        self.assertTrue(search_expression(self.file, r"int\s+mini_strcpy\s*\(\s*char\s*\*\s*,\s*char\s*\*\s*\)\s*;"))

    def test_prototype_mini_strcmp(self): 
        self.assertTrue(search_expression(self.file, r"int\s+mini_strcmp\s*\(\s*char\s*\*\s*,\s*char\s*\*\s*\)\s*;"))

    def test_prototype_mini_fopen(self):    
        self.assertTrue(search_expression(self.file, r"MYself.file\s*\*\s+mini_fopen\s*\(\s*char\s*\*\s*,\s*char\s*\)\s*;"))

    def test_prototype_mini_fread(self): 
        self.assertTrue(search_expression(self.file, r"int\s+mini_fread\s*\(\s*void\s*\*\s*,\s*int\s*,\s*int\s*,\s*MYself.file\s*\*\s*\)\s*;"))

    def test_prototype_mini_fwrite(self): 
        self.assertTrue(search_expression(self.file, r"int\s+mini_fwrite\s*\(\s*void\s*\*\s*,\s*int\s*,\s*int\s*,\s*MYself.file\s*\*\s*\)\s*;"))

    def test_prototype_mini_fflush(self):    
        self.assertTrue(search_expression(self.file, r"int\s+mini_fflush\s*\(\s*MYself.file\s*\*\s*\)\s*;"))

    def test_prototype_mini_fgetc(self): 
        self.assertTrue(search_expression(self.file, r"int\s+mini_fgetc\s*\(\s*MYself.file\s*\*\s*\)\s*;"))

    def test_prototype_mini_fputc(self): 
        self.assertTrue(search_expression(self.file, r"int\s+mini_fputc\s*\(\s*MYself.file\s*\*\s*,\s*char\s*\)\s*;"))

class StructsTestCase(unittest.TestCase):
    def __init__(self, file):
        super().__init__()
        self.file = file
    
    def test_struct_malloc_element(self):    
        self.assertTrue(search_expression(self.file, r"typedef\s+struct\s+malloc_element\s*{[^}]+}\s*malloc_element;"))

    def test_struct_myfile(self):    
        self.assertTrue(search_expression(self.file, r"typedef\s+struct\s+MYself.file\s*{[^}]+}\s*MYself.file;"))