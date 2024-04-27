from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import openpyxl
from constants.deneyimlerimConstants import * 
import json
from PIL import Image
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import os

class Test_Deneyimlerim:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        userNameInput = self.waitForElementVisible(user_xpath)
        passwordInput = self.waitForElementVisible((By.XPATH, password_xpath))
        loginButton = self.waitForElementVisible((By.XPATH,login_xpath))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,userName)
        actions.send_keys_to_element(passwordInput,password)
        actions.click(loginButton)
        actions.perform()
        loginVerified = self.waitForElementVisible((By.CSS_SELECTOR, login_css))
        assert loginVerified.text == login_verified_text 
        sleep(5)
        profileButton = self.waitForElementVisible((By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/nav//div[@class='btn-group header-avatar']/button[@type='button']//p[@class='mb-0 name']"))
        profileButton.click()
        sleep(2)
        profileInfo = self.waitForElementVisible((By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/nav//div[@class='btn-group header-avatar']/ul/li[1]/a[@href='#']"))
        profileInfo.click()
        sleep(2)
        myExperiences = self.waitForElementVisible((By.CSS_SELECTOR, "a:nth-of-type(2) > .sidebar-text"))
        myExperiences.click()
        sleep(2)
        #assert myExperiences.text == "Deneyimlerim"
        sleep(2)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=15):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementInvisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.invisibility_of_element_located(locator))
    
    def waitForElementPresent(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
    
    def waitForElementClickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
    
    def test_adding_experiment(self):
        
        corporationName = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input"))
        corporationName.click()
        corporationName.send_keys("Tobeto")
        position = self.waitForElementVisible((By.NAME, "position"))
        position.click()
        position.send_keys("Eğitmen")
        sector = self.waitForElementVisible((By.NAME, "sector"))
        sector.click()
        sector.send_keys("Eğitim")
        city = self.waitForElementVisible((By.NAME, "country"))
        city.click()
        istanbulOption2 = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/select/option[41]"))
        istanbulOption2.click()
        city.click()
        startingDate = self.waitForElementClickable((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input"))
        
        startingDate.click()
        monthDropdown1 = self.waitForElementVisible((By.CSS_SELECTOR, ".react-datepicker__month-select")) #değişmek gerekebilir
        monthDropdown1.click()
        aralikOption = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[12]"))
        aralikOption.click()
        yearDropdown1 = self.waitForElementVisible((By.CSS_SELECTOR, ".react-datepicker__year-select"))
        yearDropdown1.click()
        option2023 = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[50]"))
        option2023.click()
        dayOption1 = self.waitForElementVisible((By.CSS_SELECTOR, ".react-datepicker__day--004:nth-child(4)"))
        dayOption1.click()
        finishDate = self.waitForElementClickable((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input"))
        
        finishDate.click()
        monthDropdown2 = self.waitForElementVisible((By.CSS_SELECTOR, ".react-datepicker__month-select")) #değişmek gerekebilir
        monthDropdown2.click()
        nisanOption = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[4]"))
        nisanOption.click()
        dayOption2 = self.waitForElementVisible((By.CSS_SELECTOR, ".react-datepicker__day--005:nth-child(5)"))
        dayOption2.click()  
        jobDescription = self.waitForElementVisible((By.CSS_SELECTOR, ".col-md-12 > .form-control"))
        jobDescription.click()
        jobDescription.send_keys("Tobeto'da eğitmenlik yaptım")
        saveButton = self.waitForElementVisible((By.CSS_SELECTOR, ".btn-primary"))
        saveButton.click()
        sleep(2)
        threeDot =self.waitForElementClickable((By.CSS_SELECTOR, ".grade-info"))
        threeDot.click()
        expVerified = self.waitForElementVisible((By.XPATH, "//body/div[@role='dialog']/div//span[@class='grade-details-header']"))
        assert expVerified.text == "İş Açıklaması"
        closeButton = self.waitForElementClickable((By.XPATH, "//body/div[@role='dialog']/div//button[@type='button']"))
        saveVerified = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]/div[1]/span[1]"))
        assert saveVerified.text == "Kurum Adı"
        sleep(2)

    def test_add_experiment_without_interaction(self):
        saveButton = self.waitForElementVisible((By.CSS_SELECTOR, ".btn-primary"))
        saveButton.click()
        reqAlert1 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(1) > .text-danger"))
        reqAlert2 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(2) > .text-danger"))
        reqAlert3 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(3) > .text-danger"))
        reqAlert4 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(5) > .text-danger"))
        reqAlert5 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(6) > .text-danger"))
        assert {reqAlert1.text == "Doldurulması zorunlu alan*",
                    reqAlert2.text == "Doldurulması zorunlu alan*",
                    reqAlert3.text == "Doldurulması zorunlu alan*",
                    reqAlert4.text == "Doldurulması zorunlu alan*",
                    reqAlert5.text == "Doldurulması zorunlu alan*"}
        
    def test_experiment_while_working(self):
        corporationName = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input"))
        corporationName.click()
        corporationName.send_keys("Tobeto")
        position = self.waitForElementVisible((By.NAME, "position"))
        position.click()
        position.send_keys("Eğitmen")
        sector = self.waitForElementVisible((By.NAME, "sector"))
        sector.click()
        sector.send_keys("Eğitim")
        city = self.waitForElementVisible((By.NAME, "country"))
        city.click()
        istanbulOption2 = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/select/option[41]"))
        istanbulOption2.click()
        city.click()
        startingDate = self.waitForElementClickable((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input"))
        
        startingDate.click()
        monthDropdown1 = self.waitForElementVisible((By.CSS_SELECTOR, ".react-datepicker__month-select")) #değişmek gerekebilir
        monthDropdown1.click()
        aralikOption = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[12]"))
        aralikOption.click()
        yearDropdown1 = self.waitForElementVisible((By.CSS_SELECTOR, ".react-datepicker__year-select"))
        yearDropdown1.click()
        option2023 = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[50]"))
        option2023.click()
        dayOption1 = self.waitForElementVisible((By.CSS_SELECTOR, ".react-datepicker__day--004:nth-child(4)"))
        dayOption1.click()
        finishDate = self.waitForElementClickable((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input"))

        stillWorkingButton = self.waitForElementClickable((By.NAME, "checkbox"))
        stillWorkingButton.click()
        assert not finishDate.is_enabled()
        saveButton = self.waitForElementVisible((By.CSS_SELECTOR, ".btn-primary"))
        saveButton.click()
        sleep(2)
        threeDot =self.waitForElementClickable((By.CSS_SELECTOR, ".grade-info"))
        threeDot.click()
        expVerified = self.waitForElementVisible((By.XPATH, "//body/div[@role='dialog']/div//span[@class='grade-details-header']"))
        assert expVerified.text == "İş Açıklaması"
        closeButton = self.waitForElementClickable((By.XPATH, "//body/div[@role='dialog']/div//button[@type='button']"))
        saveVerified = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]/div[1]/span[1]"))
        assert saveVerified.text == "Kurum Adı" 

    def test_min_character(self):
        corporationName = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input"))
        corporationName.click()
        corporationName.send_keys("Tobe")
        position = self.waitForElementVisible((By.NAME, "position"))
        position.click()
        position.send_keys("Eğit")
        sector = self.waitForElementVisible((By.NAME, "sector"))
        sector.click()
        sector.send_keys("Eğit")
        saveButton = self.waitForElementVisible((By.CSS_SELECTOR, ".btn-primary"))
        saveButton.click()
        reqAlert6 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(1) > .text-danger"))
        reqAlert7 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(2) > .text-danger"))
        reqAlert8 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(3) > .text-danger"))
        reqAlert9 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(5) > .text-danger"))
        reqAlert10 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(6) > .text-danger"))
        assert {reqAlert6.text == "Doldurulması zorunlu alan*",
                    reqAlert7.text == "Doldurulması zorunlu alan*",
                    reqAlert8.text == "Doldurulması zorunlu alan*",
                    reqAlert9.text == "Doldurulması zorunlu alan*",
                    reqAlert10.text == "Doldurulması zorunlu alan*"}
        
    
    def test_max_character(self):
        corporationName = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input"))
        corporationName.click()
        corporationName.send_keys("tobetotobetotobetotobetotobetotobetotobetotobetotobetotobeto")
        position = self.waitForElementVisible((By.NAME, "position"))
        position.click()
        position.send_keys("EgitmenEgitmenEgitmenEgitmenEgitmenEgitmenEgitmenEgitmen")
        sector = self.waitForElementVisible((By.NAME, "sector"))
        sector.click()
        sector.send_keys("EgitimegitimEgitimegitimEgitimegitimEgitimegitimEgitimegitim")
        jobDescription = self.waitForElementVisible((By.CSS_SELECTOR, ".col-md-12 > .form-control"))
        jobDescription.click()
        jobDescription.send_keys("TobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetotobetotobetoTobetotobetoto")
        saveButton = self.waitForElementVisible((By.CSS_SELECTOR, ".btn-primary"))
        saveButton.click()
        reqAlert11 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(1) > .text-danger"))
        reqAlert12 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(2) > .text-danger"))
        reqAlert13 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(3) > .text-danger"))
        reqAlert14 = self.waitForElementVisible((By.CSS_SELECTOR, ".col-12.col-md-12.mb-6 > .text-danger"))
        assert {reqAlert11.text == "En fazla 50 karakter girebilirsiniz",
                    reqAlert12.text == "En fazla 50 karakter girebilirsiniz",
                    reqAlert13.text == "En fazla 50 karakter girebilirsiniz",
                    reqAlert14.text == "En fazla 300 karakter girebilirsiniz"}
        

    def test_delete_experiment(self):
        deleteFirstExperimentButton = self.waitForElementClickable((By.CSS_SELECTOR, ".grade-delete"))
        deleteFirstExperimentButton.click()
        deleteAlert = self.waitForElementVisible((By.CSS_SELECTOR, ".alert-message.mx-3"))
        assert deleteAlert.text == "Seçilen deneyimi silmek istediğinize emin misiniz ?"
        noButton = self.waitForElementClickable((By.CSS_SELECTOR, ".btn.btn-no.my-3"))
        noButton.click()
        saveVerified = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]/div[1]/span[1]"))
        assert saveVerified.text == "Kurum Adı"
        deleteFirstExperimentButton.click()
        yesButton = self.waitForElementClickable((By.CSS_SELECTOR, ".btn.btn-yes.my-3"))
        yesButton.click()
        sleep(2)
        deleteVerified = self.waitForElementVisible((By.CSS_SELECTOR, "div[role='alert'] > .toast-body"))
        assert deleteVerified.text == "• Deneyim kaldırıldı."
        
