from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec 
from constants.ayarlarConstans  import *
from time import sleep
import pytest


class Test_setting:
    
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
        #WebDriverWait(self.driver, 5).until(ec.invisibility_of_element_located((By.CSS_SELECTOR, ".toast-body")))
        #WebDriverWait(self.driver, 50).until(ec.invisibility_of_element_located(((By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div"))))
        sleep(5)
        self.driver.execute_script("window.scrollBy(0, 900);")
        sleep(2)
            
        profiliOlusturBtn = self.waitForElementVisible((By.XPATH,profiliOlusturBtn_XPATH))
        profiliOlusturBtn.click()
        sleep(2)
        
        settingBtn=self.waitForElementVisible((By.XPATH,settingBtn_XPATH))
        settingBtn.click()
    
    
    def waitForElementVisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))  
    
    
    def teardown_method(self): 
        self.driver.quit()

    
    
    def test_ayarlar(self):
                           
     
      oldPassword= self.waitForElementVisible(((By.NAME, oldPassword_NAME)))     
      oldPassword.send_keys("123456")
      
      newPassword=self.waitForElementVisible(((By.NAME, newPassword_NAME)))
      newPassword.send_keys("12345")
     
      newPasswordAgain=self.waitForElementVisible(((By.NAME, newPasswordAgain_NAME)))
      newPasswordAgain.send_keys("12345")
      
      self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     
      WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Şifreniz en az 6 karakterden oluşmalıdır."
      sleep(3)
      
      
    
      oldPassword.clear()
      newPassword.clear()
      newPasswordAgain.clear()
      
      sleep(2)
     
     
      oldPassword= self.waitForElementVisible(((By.NAME, oldPassword_NAME)))           
      oldPassword.click()
      oldPassword.send_keys("123456")
      
      newPassword=self.waitForElementVisible(((By.NAME, newPassword_NAME)))
      newPassword.click()   
      newPassword.send_keys("1235466")
      
      newPasswordAgain=self.waitForElementVisible(((By.NAME, newPasswordAgain_NAME)))      
      newPasswordAgain.click()      
      newPasswordAgain.send_keys("125486452")      
    
      self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()      
      WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Girilen şifreler eşleşmiyor kontrol ediniz.."
      sleep(2)
   

      oldPassword.clear()
      newPassword.clear()
      newPasswordAgain.clear()
      sleep(2)
        
      oldPassword= self.waitForElementVisible(((By.NAME, oldPassword_NAME)))                 
      oldPassword.click()
      oldPassword.send_keys("Salimi587")
      
      newPassword=self.waitForElementVisible(((By.NAME, newPassword_NAME)))     
      newPassword.click()
      newPassword.send_keys("7654321")
      
      newPasswordAgain=self.waitForElementVisible(((By.NAME, newPasswordAgain_NAME)))           
      newPasswordAgain.click()
      newPasswordAgain.send_keys("7654321")      
      
      
      self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()            
      WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Mevcut şifre geçersizdir."
      sleep(2)
      
      oldPassword.clear()
      newPassword.clear()
      newPasswordAgain.clear()
      
                                
     
      oldPassword= self.waitForElementVisible(((By.NAME, oldPassword_NAME)))                      
      oldPassword.click()
      oldPassword.send_keys("123456")
      
      
      newPassword=self.waitForElementVisible(((By.NAME, newPassword_NAME)))           
      newPassword.click()
      newPassword.send_keys("123456")
      
      newPasswordAgain=self.waitForElementVisible(((By.NAME, newPasswordAgain_NAME)))                     
      newPasswordAgain.click()
      newPasswordAgain.send_keys("123456")      
      
      self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click() 
           
      oldPassword.clear()
      newPassword.clear()
      newPasswordAgain.clear()
      sleep(2)
    
      self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
      WebDriverWait(self.driver, 50).until(ec.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/span")))              
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/span").text == "Doldurulması zorunlu alan*"
      sleep(2)          
        
    
     
    

    def test_password_update(self):
         
       oldPassword= self.waitForElementVisible(((By.NAME, oldPassword_NAME)))                      
       oldPassword.click()
       oldPassword.send_keys("123456")
      
      
       newPassword=self.waitForElementVisible(((By.NAME, newPassword_NAME)))           
       newPassword.click()
       newPassword.send_keys("654321")
      
       newPasswordAgain=self.waitForElementVisible(((By.NAME, newPasswordAgain_NAME)))                     
       newPasswordAgain.click()
       newPasswordAgain.send_keys("654321")      
      
       self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click() 
       WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
       assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Şifreniz güncellenmiştir."   
  
   

    def test_membership(self):
         self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]/button").click()
         self.driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div/div/div/div[2]/button[2]").click()



