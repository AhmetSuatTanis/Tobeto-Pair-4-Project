from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import openpyxl
from constants.tobetoanalizConstants import * 
import json
from PIL import Image
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import os


class Test_TobetoAnaliz:
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
        reviewsButton = self.waitForElementVisible((By.CSS_SELECTOR, "li:nth-of-type(3) > .c-gray-3.nav-link"))
        reviewsButton.click()
    
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
    
    def test_view_report(self):
        actions3 = ActionChains(self.driver)
        viewReportButton = self.waitForElementClickable((By.CSS_SELECTOR, ".btn.btn-primary"))
        viewReportButton.click()
        greenDot = self.waitForElementVisible((By.CSS_SELECTOR, ".col-12.col-md-7.my-3 > .chartjs-render-monitor"))
        actions3.move_to_element(greenDot).perform()
        newWorld = self.waitForElementVisible((By.CSS_SELECTOR, "div#accordionExample > div:nth-of-type(1) .fw-bolder.h6.mb-0.text-primary"))
        assert newWorld.text == "Yeni dünyaya hazırlanıyorum"
        newWorld1 = self.waitForElementVisible((By.CSS_SELECTOR, "#heading8 .fw-bolder"))
        actions3.double_click(newWorld1).perform()
        self.driver.implicitly_wait(2)
        newWorld2 = self.waitForElementVisible((By.CSS_SELECTOR, "#heading28 .fw-bolder"))
        actions3.double_click(newWorld2).perform()
        self.driver.implicitly_wait(2)
        newWorld3 = self.waitForElementVisible((By.CSS_SELECTOR, "#hheading8 .fw-bolder"))
        actions3.double_click(newWorld3).perform()
        self.driver.implicitly_wait(2)
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,200)")
        sleep(2)
        professionalStance = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(5) .fw-bolder.h6.mb-0.text-primary"))
        assert professionalStance.text == "Profesyonel duruşumu geliştiriyorum"
        professionalStance1 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(6) > .accordion-header  .fw-bolder"))
        actions3.double_click(professionalStance1).perform()
        self.driver.implicitly_wait(2)
        professionalStance2 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(7) > .accordion-header  .fw-bolder"))
        actions3.double_click(professionalStance2).perform()
        self.driver.implicitly_wait(2)
        professionalStance3 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(8) > .accordion-header  .fw-bolder"))
        actions3.double_click(professionalStance3).perform()
        self.driver.implicitly_wait(2)
        sleep(2)
        #self.driver.execute_script("window.scrollTo(0,100)")
        sleep(2)
        iknowMyself = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(9) .fw-bolder.h6.mb-0.text-primary"))
        assert iknowMyself.text == "Kendimi tanıyor ve yönetiyorum"
        iknowMyself1 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(10) > .accordion-header  .fw-bolder"))
        actions3.double_click(iknowMyself1).perform()
        self.driver.implicitly_wait(2)
        iknowMyself2 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(11) > .accordion-header  .fw-bolder"))
        actions3.double_click(iknowMyself2).perform()
        self.driver.implicitly_wait(2)
        iknowMyself3 = self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(12) > .accordion-header  .fw-bolder"))
        actions3.double_click(iknowMyself3).perform()
        self.driver.implicitly_wait(2)
        sleep(2)

        



