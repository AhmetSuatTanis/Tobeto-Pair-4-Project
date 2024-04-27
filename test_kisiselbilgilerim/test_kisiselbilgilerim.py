from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import openpyxl
from constants.kisiselbilgilerimConstants import * 
import json
from PIL import Image
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import os
import keyboard

class Test_KisiselBilgilerim:
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
        profileInfoVerified = self.waitForElementVisible((By.CSS_SELECTOR, "a:nth-of-type(1) > .sidebar-text"))
        assert profileInfoVerified.text == "Kişisel Bilgilerim"

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=15):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    
    def waitForElementInvisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.invisibility_of_element_located(locator))
    
    def waitForElementPresent(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
    
    def test_edit_personal_info(self):
        sleep(2)
        yourName = self.waitForElementVisible((By.NAME,"name"), 15)
        yourName.click()
        yourName.clear()
        yourName.send_keys("Recep")
        sleep(2)
        yourSurname = self.waitForElementVisible((By.NAME, "surname"),15)
        yourSurname.click()
        yourSurname.clear()
        yourSurname.send_keys("Kızıl")
        sleep(2)
        yourPhoneNumber = self.waitForElementVisible((By.NAME, "phoneNumber"),15)
        yourPhoneNumber.click()
        yourPhoneNumber.send_keys(Keys.CONTROL + "a")
        yourPhoneNumber.send_keys(Keys.DELETE)
        yourPhoneNumber.send_keys("5360731162")
        sleep(2)
        yourBirthDate = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/input"),15)
        yourBirthDate.click()
        yourBirthDate.send_keys(Keys.CONTROL + "a")
        yourBirthDate.send_keys(Keys.DELETE)
        yourBirthDate.send_keys("01.10.2000")
        sleep(2)
        yourTCno = self.waitForElementVisible((By.NAME, "identifier"))
        yourTCno.click()
        yourTCno.send_keys(Keys.CONTROL + "a")
        yourTCno.send_keys(Keys.DELETE)
        yourTCno.send_keys("53767727284")
        sleep(2)
        yourEmail = self.waitForElementVisible((By.NAME, "email"))
        assert not yourEmail.is_enabled() #TC kısmının tıklanabilir olmadığının kontrolü
        sleep(2)
        yourCountry = self.waitForElementVisible((By.NAME, "country"))
        yourCountry.click()
        yourCountry.send_keys(Keys.CONTROL + "a")
        yourCountry.send_keys(Keys.DELETE)
        yourCountry.send_keys("Türkiye")
        sleep(2)
        yourCitydropdown = self.waitForElementVisible((By.NAME, "city"))
        yourCitydropdown.click()
        istanbulOption = self.waitForElementPresent((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/select/option[41]"), 15)
        istanbulOption.click()
        sleep(2)
        yourDistrict = self.waitForElementVisible((By.NAME, "district"))
        yourDistrict.click()
        pendikOption = self.waitForElementPresent((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/select/option[29]"))
        pendikOption.click()
        sleep(4)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(4)
        saveButton = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"))
        yourStreet = self.waitForElementVisible((By.NAME, "address"))
        yourStreet.click()
        yourStreet.send_keys(Keys.CONTROL + "a")
        yourStreet.send_keys(Keys.DELETE)
        yourStreet.send_keys("BatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneşSokakBatıMahallesiGüneş")
        saveButton.click()
        sleep(2)
        yourStreetAlert = self.waitForElementVisible((By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']/div/div[11]/span[@class='text-danger']"))
        assert yourStreetAlert.text == "En fazla 200 karakter girebilirsiniz"
        sleep(2)
        yourStreet.click()
        yourStreet.send_keys(Keys.CONTROL + "a")
        yourStreet.send_keys(Keys.DELETE)
        yourStreet.send_keys("BatıMahallesi")
        sleep(2)

        aboutMe = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[12]/textarea"))
        aboutMe.click()
        aboutMe.send_keys(Keys.CONTROL + "a")
        aboutMe.send_keys(Keys.DELETE)
        aboutMe.send_keys("Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.Merhaba, ben Recep Kızıl.")
        saveButton.click()
        sleep(2)
        aboutMeAlert = self.waitForElementVisible((By.XPATH, "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']/div/div[12]/span[@class='text-danger']"))
        assert aboutMeAlert.text == "En fazla 300 karakter girebilirsiniz"
        sleep(2)
        
        aboutMe.click()
        aboutMe.send_keys(Keys.CONTROL + "a")
        aboutMe.send_keys(Keys.DELETE)
        aboutMe.send_keys("Merhaba, ben Recep Kızıl")
        sleep(2)
        saveButton.click()
        sleep(2)
        profileInfoSavedAlert = self.waitForElementVisible((By.CSS_SELECTOR, "div[role='alert'] > .toast-body"))
        assert profileInfoSavedAlert.text == "• Bilgileriniz başarıyla güncellendi."
        sleep(2)


    def test_required_fields_empty(self):
        yourBirthDate = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/input"),15)
        yourBirthDate.click()
        yourBirthDate.send_keys(Keys.CONTROL + "a")
        yourBirthDate.send_keys(Keys.DELETE)
        sleep(2)
        yourTCno = self.waitForElementVisible((By.NAME, "identifier"))
        yourTCno.click()
        yourTCno.send_keys(Keys.CONTROL + "a")
        yourTCno.send_keys(Keys.DELETE)
        sleep(2)
        yourCountry = self.waitForElementVisible((By.NAME, "country"))
        yourCountry.click()
        yourCountry.send_keys(Keys.CONTROL + "a")
        yourCountry.send_keys(Keys.DELETE)
        sleep(2)
        yourCitydropdown = self.waitForElementVisible((By.NAME, "city"))
        yourCitydropdown.click()
        selectCity = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/select/option[1]"))
        selectCity.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        saveButton = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"))
        saveButton.click()
        sleep(2)
        requiredAlert1 = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/span"))
        requiredAlert2 = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[1]"))
        requiredAlert3 = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/span"))
        requiredAlert4 = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/span"))
        requiredAlert5 = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/span"))
        assert requiredAlert1.text == "Doldurulması zorunlu alan*"
        assert requiredAlert2.text == "*Aboneliklerde fatura için doldurulması zorunlu alan"
        assert requiredAlert3.text == "Doldurulması zorunlu alan*"
        assert requiredAlert4.text == "Doldurulması zorunlu alan*"
        assert requiredAlert5.text == "Doldurulması zorunlu alan*"
        
    def test_edit_yourTCno(self):
        yourTCno = self.waitForElementVisible((By.NAME, "identifier"))
        yourTCno.click()
        yourTCno.send_keys(Keys.CONTROL + "a")
        yourTCno.send_keys(Keys.DELETE)
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        saveButton = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"))
        saveButton.click()
        sleep(2)
        #self.driver.execute_script("window.scrollTo(0,100)")
        sleep(2)
        requiredAlert6 = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[1]"))
        assert requiredAlert6.text == "*Aboneliklerde fatura için doldurulması zorunlu alan"
        sleep(2)
        yourTCno = self.waitForElementVisible((By.NAME, "identifier"))
        yourTCno.click()
        yourTCno.send_keys("123456")
        sleep(2)
        requiredAlert7 = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[2]"))
        assert requiredAlert7.text == "TC Kimlik Numarası 11 Haneden Az olamaz"
        sleep(2)
        yourTCno.click()
        yourTCno.send_keys(Keys.CONTROL + "a")
        yourTCno.send_keys(Keys.DELETE)
        sleep(2)
        yourTCno.send_keys("123456789101112")
        sleep(2)
        requiredAlert8 = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[2]"))
        assert requiredAlert8.text == "TC Kimlik Numarası 11 Haneden Fazla olamaz"
        sleep(2)
        yourTCno.click()
        yourTCno.send_keys(Keys.CONTROL + "a")
        yourTCno.send_keys(Keys.DELETE)
        yourTCno.send_keys("53767727284")
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        saveButton = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"))
        saveButton.click()
        sleep(2)
        yourTCnoVerified = self.waitForElementVisible((By.CSS_SELECTOR, "div[role='alert'] > .toast-body"))
        assert yourTCnoVerified.text == "• Bilgileriniz başarıyla güncellendi."
        sleep(2)

    def test_add_pp_browse(self): #gözat ile profil resmi yükleme
        editButton = self.waitForElementVisible((By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//div[@class='col-12 mb-6 text-center']/div[1]/div[1]"))
        editButton.click()
        sleep(2)
        addFile = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/input[1]").send_keys("C:\\Users\\recep\\Downloads\\profilephoto.jpg")
        sleep(2)
        file_load_button=self.waitForElementVisible((By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//div[@class='uppy-Root']/div/div[@role='dialog']//div[@class='uppy-Dashboard-progressindicators']/div[1]//button[@type='button']")).click()
        sleep(5)

    def test_add_incompatible_pp(self):
        edit_button = self.waitForElementVisible((By.XPATH, "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//div[@class='col-12 mb-6 text-center']/div[1]/div[1]"))
        edit_button.click()
        sleep(2)
        addFile = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/input[1]").send_keys("C:\\Users\\recep\\Downloads\\image.webp")
        incompatibleAlert = self.waitForElementVisible((By.CSS_SELECTOR, ".uppy-Informer-animated > p"))
        sleep(1)
        assert incompatibleAlert.text == "Sadece image/jpeg, image/png yükleyebilirsiniz"
        sleep(2)


    def test_delete_pp(self):
        deleteButton = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[1]/div[2]"))
        deleteButton.click()
        sleep(2)
        areYouSure = self.waitForElementVisible((By.CSS_SELECTOR, "div[role='dialog'] p"))
        assert areYouSure.text == "Profil fotoğrafını kaldırmak istediğinize emin misiniz ?"
        sleep(2)
        noButton = self.waitForElementVisible((By.CSS_SELECTOR, ".modal-footer > .btn:nth-child(2)"))
        noButton.click()
        sleep(2)
        deleteButton.click()
        sleep(2)
        yesButton = self.waitForElementVisible((By.CSS_SELECTOR, ".btn-primary:nth-child(1)"))
        yesButton.click()
        sleep(2)
        ppRemoveVerified = self.waitForElementVisible((By.CSS_SELECTOR, "div[role='alert'] > .toast-body"))
        assert ppRemoveVerified.text == "• Dosya kaldırma işlemi başarılı."
        sleep(2)

        
        #notlar
        # case 5 kopyala yapıştır araştırdım bulamadım tekrar dönerim. case 6 sürükle bırak imkansız. case 7 uyumsuz dosya uyarısı textine erişemiyorum bulduğum cssler, xpathler işe yaramadı.
        #gereksiz sleepleri sil
        #tc yanlış girme kısmını excele ekle ve burda da yap
        #def pp browse kısmını ahmetin yöntemle yap
        #html reporting yapmayı unutmayın
        #genel projenin bug oranını ekleyin
        #smoke test yap