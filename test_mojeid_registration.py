import pytest # radšej používam pytest ako unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestMainInit():
    def setup_method(self):
        options = Options()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        # zostane mi okno Chrome otvorené, bez tohoto sa zavrie bez ohľadu na teardown-method

    def test_registration_fail(self):
        self.driver.get('https://mojeid.regtest.nic.cz/registration') # otvorý požadovanú stránku
        # počkám kým sa celá stránka načíta
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '//header/div/nav/div[2]/div[1]')) )
        
        # overím aký je jazyk stránky
        lang = self.driver.find_element(By.XPATH, '//header/div/nav/div[2]/div[1]').text 
        
        # poprípade vykonám prepnutie do požadovaného jazyka
        if lang.__contains__('E'):
            print("jazyk čeština") # informatívny výpis
        else:
            lang = self.driver.find_element(By.XPATH, '//header/div/nav/div[2]/div[1]').click()
            print("jazyk angličtina, prepínam na češtinu") # informatívny výpis

        # opäť pre istotu počkám kým sa načíta potrebný prvok stránky
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '//div/input[1]')) )

        # vložím jednotlivé hodnoty do formulára
        self.driver.find_element(By.XPATH, '//div/input[1]').send_keys('Janko')
        self.driver.find_element(By.XPATH, '//div/input[2]').send_keys('Hraško')
        self.driver.find_element(By.ID, 'email').send_keys('janko.hrasko@liamg.moc')
        self.driver.find_element(By.CLASS_NAME, 'vti__input').send_keys('+421988666555444')

        # nájdem check box a použijem script aby na jeho pozíciu zroloval stránku nadol.
        check_box = self.driver.find_element(By.XPATH, '//div[contains(@class,"p-checkbox-box")]')
        self.driver.execute_script("arguments[0].scrollIntoView()", check_box)

        # nájdem a zaškrtnem chceck box že súhlasím s podmienkami použitia
        self.driver.find_element(By.XPATH, '//div[contains(@class,"p-checkbox-box")]').click()
        
        # stlačím tlačítko na odoslanie formulára
        self.driver.find_element(By.XPATH, '//div/button').click()

        # uložím si text prvku do premennej
        err = self.driver.find_element(By.ID, 'phone-error').text
        
        # overím či je vypísaný text zhodný a textom v jednom alebo druhom jazyku.
        assert err == 'Invalid number format.' or err == 'Formát čísla není správný.'

    # vypnutá metóda na zatvorenie okna pre kontrolu údajov vizuálne
    # def teardown_method(self):
        # self.driver.close()
        # self.driver.quit()

# spustenie testu
if __name__ == "__main__":
    pytest.main([__file__, '-vs'])