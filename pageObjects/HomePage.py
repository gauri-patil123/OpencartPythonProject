from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage():
    My_account_text = "//span[text()='My Account']"
    Register_text = "Register"
    Login_text = "Login"

    def __init__(self, driver):
      self.driver = driver

    def clickMyAccount(self):
     # self.driver.find_element(By.XPATH, self.My_account_text).click()
      ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.My_account_text)))
      ele.click()
    def clickOnRegister(self):
      self.driver.find_element(By.LINK_TEXT, self.Register_text).click()

    def clickOnLogin(self):
      self.driver.find_element(By.LINK_TEXT, self.Login_text).click()



