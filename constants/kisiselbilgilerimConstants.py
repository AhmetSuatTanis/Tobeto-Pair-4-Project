from selenium.webdriver.common.by import By

BASE_URL = "https://tobeto.com/giris"
user_xpath = (By.XPATH,"/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='email']")
password_xpath = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='password']"
login_xpath = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/button[.='Giriş Yap']"
userName = "recepkizil7834@gmail.com"
password = "Recep732."
login_verified_text = "• Giriş başarılı."
login_css = "div[role='alert'] > .toast-body"


