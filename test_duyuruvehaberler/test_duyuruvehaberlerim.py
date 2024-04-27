from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import openpyxl
from constants.duyuruvehaberlerimConstants import * 
import json
from PIL import Image
from datetime import datetime

class TestDuyuruveHaberlerim:
    
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
        duyuruButton = self.waitForElementVisible((By.XPATH, "/html//button[@id='notification-tab']"))
        duyuruButton.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        dahaFazlaGosterButon = self.waitForElementVisible((By.CSS_SELECTOR, "div#notification-tab-pane  .showMoreBtn"))
        dahaFazlaGosterButon.click()
        sleep(5)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementInvisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.invisibility_of_element_located(locator))
    
    def test_success(self):
        searchBar = self.waitForElementVisible((By.CSS_SELECTOR, ".search-box.searchBox"))
        actions2 = ActionChains(self.driver)
        actions2.click(searchBar)
        actions2.send_keys_to_element(searchBar, "Yeni Gelenler İçin Bilgilendirme")
        actions2.perform()
        result1 = self.waitForElementVisible((By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[2]/div[1]/div[@class='notfy-card notify']/div[@class='d-flex flex-column']/span[.='Yeni Gelenler için Bilgilendirme']"))
        assert result1.text == "Yeni Gelenler için Bilgilendirme"
        result2 = self.waitForElementVisible((By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[2]/div[2]/div[@class='notfy-card notify']//span[.='Yeni Gelenler için Bilgilendirme']"))
        assert result2.text == "Yeni Gelenler için Bilgilendirme"
        result3 = self.waitForElementVisible((By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[2]/div[3]/div[@class='notfy-card notify']//span[.='Yeni Gelenler için Bilgilendirme']"))
        assert result3.text == "Yeni Gelenler için Bilgilendirme"

    def test_blank_results(self):
        searchBar = self.waitForElementVisible((By.CSS_SELECTOR, ".search-box.searchBox"))
        actions2 = ActionChains(self.driver)
        actions2.click(searchBar)
        actions2.send_keys_to_element(searchBar, "x")
        actions2.perform()
        result4 = self.waitForElementVisible((By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']//p[.='Bir duyuru bulunmamaktadır.']"))
        assert result4.text == "Bir duyuru bulunmamaktadır."

    def test_type_listing(self):
        typeBar = self.waitForElementVisible((By.XPATH,"(//button[@type='button'])[4]")) 
        typeBar.click()
        option2 = self.waitForElementVisible((By.ID, "typeAnnouncement"))
        option2.click()
        typeBar.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,100)")
        selectedpage1 = self.waitForElementVisible((By.CSS_SELECTOR, "li:nth-of-type(2) > a[role='button']"))
        assert selectedpage1.text == "1"
        sleep(2)
        listOfResults = self.driver.find_elements(By.CSS_SELECTOR, "div[class='col-md-4 col-12 my-4']")
        assert len(listOfResults) ==9
        sleep(5)

    def test_blank_type_listing(self):
        typeBar = self.waitForElementVisible((By.XPATH,"(//button[@type='button'])[4]")) 
        typeBar.click()
        option1 = self.waitForElementVisible((By.ID, "typeNews"))
        option1.click()
        typeBar.click()
        sleep(2) #bu sleep olmayınca görmüyor
        result5 = self.waitForElementVisible((By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']//p[.='Bir duyuru bulunmamaktadır.']"))
        assert result5.text == "Bir duyuru bulunmamaktadır."
        sleep(5)

    def test_listBy_date(self):
        listBar = self.waitForElementVisible((By.XPATH,"//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[1]/div/div[4]/div[1]/button[@type='button']"))
        listBar.click()
        listByYtoE = self.waitForElementVisible((By.XPATH,"//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[1]/div//ul[@class='dropdown-menu new-filter show']//a[.='Tarihe Göre (Y-E)']"))
        listByYtoE.click()
        sleep(2)
        result6 = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div/div[2]/span[1]"))
        result7 = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/div[2]/div[2]/div[2]/div/div[2]/span[1]"))
        tarih1 = datetime.strptime(result6.text, "%d.%m.%Y")
        tarih2 = datetime.strptime(result7.text, "%d.%m.%Y")
        assert tarih1 > tarih2
        sleep(2)
        listBar = self.waitForElementVisible((By.XPATH,"//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[1]/div/div[4]/div[1]/button[@type='button']"))
        listBar.click()
        listByEtoY = self.waitForElementVisible((By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[1]/div//ul[@class='dropdown-menu new-filter show']//a[.='Tarihe Göre (E-Y)']"))
        listByEtoY.click()
        sleep(2)
        result8 = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div/div[2]/span[1]"))
        result9 = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/div[2]/div[2]/div[2]/div/div[2]/span[1]"))
        tarih3 = datetime.strptime(result8.text, "%d.%m.%Y")
        tarih4 = datetime.strptime(result9.text, "%d.%m.%Y")
        assert tarih3 < tarih4
        sleep(2) 

    def test_hide_news_and_announcementes(self):
        self.test_success()
        readMore = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div/div[2]/span[2]"))
        readMore.click()
        sleep(2)
        closePopUp = self.waitForElementVisible((By.CSS_SELECTOR, "div[role='dialog'] .btn-close"))
        closePopUp.click()
        sleep(2)
        hideRead = self.waitForElementVisible((By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']/div[1]/div//button[@class='read-hide']"))
        hideRead.click()
        sleep(2)
        result10 = self.waitForElementInvisible((By.XPATH,"//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div/div[1]/span"))
        assert result10 #burası bug o yüzden fail

        #bunun sadece constantları vs düzenlenecek

        






        

        




    








