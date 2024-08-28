from selenium.webdriver.common.by import By

class AccountRegistrationPage():
    text_First_Name_Id = "input-firstname"
    text_Last_Name_Id = "input-lastname"
    text_Email_Id = "input-email"
    text_Password_Id = "input-password"
    btn_Privacy_Policy_name = "agree"
    Btn_Continue = "//button[text()='Continue']"
    Message_account_created = "//h1[text()='Your Account Has Been Created!']"


    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.text_First_Name_Id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.text_Last_Name_Id).send_keys(lname)

    def enterEmail(self, mail):
        self.driver.find_element(By.ID, self.text_Email_Id).send_keys(mail)

    def enterPassword(self, pwd):
        self.driver.find_element(By.ID, self.text_Password_Id).send_keys(pwd)

    def chcekPrivacyPolicyBtn(self):
        self.driver.find_element(By.NAME, self.btn_Privacy_Policy_name).click()

    def clickOnContinueBtn(self):
        self.driver.find_element(By.XPATH, self.Btn_Continue).click()

    def verifyMsgAccountCreated(self):
        return self.driver.find_element(By.XPATH, self.Message_account_created).text()