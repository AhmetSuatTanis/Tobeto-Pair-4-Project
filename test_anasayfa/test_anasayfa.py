from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from constants.anasayfaConstans import *       # type: ignore
from time import sleep
import pytest

class Test_Homepage():     
          
    def setup_method(self):
       
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window() 
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div/div/form/input[1]")))
        usernameInput.send_keys("kairee.hashir@foodfarms.net")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div/div/form/input[2]")))
        passwordInput.send_keys("123456")
        loginButton = self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div/div/div/div/form/button")
        loginButton.click()
        WebDriverWait(self.driver, 5).until(ec.invisibility_of_element_located((By.CSS_SELECTOR, ".toast-body")))
        WebDriverWait(self.driver, 50).until(ec.invisibility_of_element_located(((By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div"))))
        sleep(5)
        
       
    def waitForElementVisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
           
    def theardown_method(self):
           self.driver.quit()
              
               
        
    def test_anasayfa(self):
           
            profilim_link = self.waitForElementVisible((By.XPATH,profilim_XPATH))
            profilim_link.click()
            sleep(2)
            self.driver.back()
           
            degerlendirmeBtn = self.waitForElementVisible((By.XPATH,degerlendirmeBtn_XPATH))
            degerlendirmeBtn.click()
            sleep(2)
            self.driver.back()
           
           
            katalogBtn = self.waitForElementVisible((By.XPATH,katalogBtn_XPATH))            
            katalogBtn.click()
            sleep(2)
            self.driver.back()
           

            takvimBtn = self.waitForElementVisible((By.XPATH,takvimBtn_XPATH))
            takvimBtn.click()
            sleep(2)
            self.driver.back()

            anasayfaBtn = self.waitForElementVisible((By.XPATH,anasayfaBtn_XPATH))
            anasayfaBtn.click()
            sleep(2)
           
             
            self.driver.execute_script("window.scrollBy(0, 500);")
            sleep(1)
        
            egitimlerimBtn = self.waitForElementVisible((By.ID,egitimlerimBtn_ID))            
            egitimlerimBtn.click()
            sleep(2)
            
           
            duyuruHaberlerimBtn = self.waitForElementVisible((By.ID,duyuruHaberlerimBtn_ID))
            duyuruHaberlerimBtn.click()
            sleep(2)
           

            anketlerimBtn = self.waitForElementVisible((By.ID,anketlerimBtn_ID))
            anketlerimBtn.click()
            sleep(2)
            
            
            basvurularimBtn= self.waitForElementVisible((By.ID,basvurularimBtn_ID))
            basvurularimBtn.click()
            sleep(2)
                        
          
            self.driver.execute_script("window.scrollBy(0, 800);")

            sinavlarimBtn = self.waitForElementVisible((By.XPATH,sinavlarimBtn_XPATH))
            sinavlarimBtn.click()
            sleep(3)
                                   
            logoutButton = self.waitForElementVisible((By.CSS_SELECTOR, logoutButton_CSS_SELECTOR))
            logoutButton.click()    
            sleep(2)
            
            self.driver.execute_script("window.scrollBy(0, 900);")
            sleep(2)
            

            profiliOlusturBtn = self.waitForElementVisible((By.XPATH,profiliOlusturBtn_XPATH))
            profiliOlusturBtn.click()
            sleep(2)
            
            self.driver.back()
            sleep(2)
            
            self.driver.execute_script("window.scrollBy(0, 900);")
            sleep(2)

            kendiniDegerlendirBtn = self.waitForElementVisible((By.XPATH,kendiniDegerlendirBtn_XPATH))
            kendiniDegerlendirBtn.click()
            sleep(2)
           
            self.driver.back()
           
            sleep(2)
            
            self.driver.execute_script("window.scrollBy(0, 900);")
            sleep(2)

            ogrenmeyeBaslaBtn = self.waitForElementVisible((By.XPATH,ogrenmeyeBaslaBtn_XPATH))
            ogrenmeyeBaslaBtn.click()
            sleep(3)

            self.driver.back()
            sleep(2)
            self.driver.quit()        
