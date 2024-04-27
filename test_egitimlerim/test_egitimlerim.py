from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import openpyxl
from constants.egitimlerimConstants import * 
import json
from PIL import Image
from datetime import datetime

class Test_Egitimlerim:

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
        sleep(2)
        self.waitForElementVisible((By.ID, lessons_id)).click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        showMore = self.waitForElementVisible((By.XPATH, show_more_xpath))
        showMore.click()
        sleep(2)
        selectBox = self.waitForElementVisible((By.XPATH,"/html//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[@class='filter-section mt-3']/div/div[2]/div/div[1]/div[1]/div[2]"))
        selectBox.click()
        selectMenu = self.waitForElementVisible((By.ID, "react-select-2-listbox"))
        selectMenu.click()
        sleep(3)
        allLessons = self.waitForElementVisible((By.ID, "all-lessons-tab"))
        assert allLessons.text == "Tüm Eğitimlerim"
        sleep(2)

    def teardown_method(self):
        self.driver.quit()
    
    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
        
    def test_list_by_AtoZ(self):
        listBY = self.waitForElementVisible((By.CSS_SELECTOR, ".css-hlgwow.select__value-container.select__value-container--has-value > .css-19bb58m.select__input-container"))
        listBY.click()
        listByAtoZ = self.waitForElementVisible((By.ID, "react-select-3-option-0"))
        listByAtoZ.click()
        sleep(2)
        lesson1 = self.waitForElementVisible((By.CSS_SELECTOR, "div#all-lessons-tab-pane > .row > div:nth-of-type(1) .d-flex.flex-column > span:nth-of-type(1)"))
        lesson1_text = lesson1.text
        assert lesson1_text[0] == "D", "A'dan Z'ye sıralama hatalıdır"
        lesson2 = self.waitForElementVisible((By.CSS_SELECTOR, "div#all-lessons-tab-pane > .row > div:nth-of-type(2) .d-flex.flex-column > span:nth-of-type(1)"))
        lesson2_text = lesson2.text
        assert lesson2_text[0] == "E", "A'dan Z'ye sıralama hatalıdır"
        sleep(3)

    def test_list_by_ZtoA(self):
        listBYY = self.waitForElementVisible((By.CSS_SELECTOR, ".css-hlgwow.select__value-container.select__value-container--has-value > .css-19bb58m.select__input-container"))
        listBYY.click()
        sleep(3)
        listByZtoA = self.waitForElementVisible((By.ID, "react-select-3-option-1"))
        listByZtoA.click()
        sleep(2)
        lesson1z = self.waitForElementVisible((By.CSS_SELECTOR, "div#all-lessons-tab-pane > .row > div:nth-of-type(1) .d-flex.flex-column > span:nth-of-type(1)"))
        lesson1z_text = lesson1z.text
        assert lesson1z_text[0] == "Y", "Z'den A'ya sıralama hatalıdır"
        lesson3z = self.waitForElementVisible((By.CSS_SELECTOR,"div#all-lessons-tab-pane > .row > div:nth-of-type(3) .d-flex.flex-column > span:nth-of-type(1)" ))
        lesson3z_text = lesson3z.text
        assert lesson3z_text[0] == "S", "Z'den A'ya sıralama hatalıdır"

    def test_list_by_newest(self):
        listBYY = self.waitForElementVisible((By.CSS_SELECTOR, ".css-hlgwow.select__value-container.select__value-container--has-value > .css-19bb58m.select__input-container"))
        listBYY.click()
        sleep(3)
        listByYtoE = self.waitForElementVisible((By.ID, "react-select-3-option-2")) 
        sleep(3)
        listByYtoE.click()
        sleep(2)
        ders1 = self.waitForElementVisible((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[1]/div/div[2]/div/span[2]"))
        ders2 = self.waitForElementVisible((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[2]/div/div[2]/div/span[2]"))
        tarih1 = datetime.strptime(ders1.text, "%d %b %Y %H:%M")
        tarih2 = datetime.strptime(ders2.text, "%d %b %Y %H:%M")
        assert tarih1 < tarih2

    def test_list_by_oldest(self):
        listBY = self.waitForElementVisible((By.CSS_SELECTOR, ".css-hlgwow.select__value-container.select__value-container--has-value > .css-19bb58m.select__input-container"))
        listBY.click()
        sleep(3)
        listByEtoY = self.waitForElementVisible((By.ID, "react-select-3-option-3")) 
        sleep(3)
        listByEtoY.click()
        sleep(2)
        ders3 = self.waitForElementVisible((By.XPATH, "/html//div[@id='all-lessons-tab-pane']/div[@class='row']/div[1]/div[@class='corp-edu-card']/div[@class='card-content']/div[@class='d-flex flex-column']/span[@class='platform-course-date']"))
        sleep(2)
        ders4 = self.waitForElementVisible((By.XPATH, "/html//div[@id='all-lessons-tab-pane']/div[@class='row']/div[2]/div[@class='corp-edu-card']/div[@class='card-content']/div[@class='d-flex flex-column']/span[@class='platform-course-date']"))
        sleep(2)
        tarih3 = datetime.strptime(ders3.text, "%d %B %Y %H:%M")
        sleep(2)
        tarih4 = datetime.strptime(ders4.text, "%d %B %Y %H:%M")
        sleep(2)
        assert tarih3 > tarih4 
        sleep(2) #format hatalarından dolayı son iki def çalışmıyor. 111.satıdaki küçüktür olmalı. normalde büyüktür yapınca test doğru olmalı..

 
        









        


    

     


   
