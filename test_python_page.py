# Import modulov unittestu a selenium webdriver, by a keys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# vytvotenie triedy ktora dedi z unittest modulu
class PythonOrgSearch(unittest.TestCase):
    """
    Trieda obsahuje selenium test pre vyhladavanie na stranke Python.org.

    
    Metody:
        - setUp: inicializacia webdriveru pred kazdym testom
        - test_search_in_python_org: Samotny test a jeho kroky na stranke python.org
        - tearDown: Ukonceni webdriveru po kazdom teste
    """

    def setUp(self):
        """ inicializacia webdrivera """
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome() # ja pouzivam webdriver pre chrome
    
    def test_search_in_python_org(self):
        """ samotny test a jeho operacie """
        driver = self.driver # priradenie webdrivera do premennej
        driver.get("http://www.python.org") # driver prejde na stranku "www.python.org"
        self.assertIn("Python", driver.title) # overenie ci nachadza sa v title slovo "Python"
        elem = driver.find_element(By.NAME, "q") # driver najde prvok s menom a ulozi do premennej
        elem.send_keys("pycon") # driver do najdeneho a ulozeneho pola vlozi text "pypcon"
        elem.send_keys(Keys.RETURN) # driver stlaci ENTER
        assert "No results found." not in driver.page_source # overenie ci sa v zdrojovom kode
        # stranky nenachadza text "No results found.", tak sa overi ze naslo aspon jeden vysledok
    
    def tearDown(self):
        """ ukoncenie webdrivera a zatvorenie stranky """
        self.driver.close()
        self.driver.quit()

# ak je subor spusteny ako subor a nie ako importovany modul, tak vykonaj test
if __name__ == "__main__":
    unittest.main()