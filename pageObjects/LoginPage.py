import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    text_email_address ="input-email"
    text_pwd = "input-password"
    btn_login = "//button[text()='Login']"
    my_account_text = "//h2[text()='My Account']"
    my_orders_text = "My Orders"
    my_affiliate_account_text = "My Affiliate Account"
    link_edit_acc_info = "Edit your account information"
    id_firstname = "//input[@id= 'input-firstname']"
    id_lastname = "//input[@id= 'input-lastname']"
    id_email = "//input[@id= 'input-email']"
    btn_continue = "//button[text()='Continue']"
    acc_update_msg = "//div[@class='alert alert-success alert-dismissible']"
    # Success: Your account has been successfully updated
    link_change_pwd = "//a[text()='Change your password']"
    id_password = "input-password"
    id_confirm_password = "input-confirm"
    lnk_modify_address_book = "Modify your address book entries"
    btn_new_address = "New Address"
    id_company = "input-company"
    id_address = "input-address-1"
    id_city = "input-city"
    id_postcode = "input-postcode"
    id_default_value_yes = "input-default-yes"
    logout = "//a[@class='dropdown-item' and text()='Logout']"




    def __init__(self, driver):
        self.driver = driver

    def enterEmailAddress(self, mail):
        self.driver.find_element(By.ID, self.text_email_address).send_keys(mail)

    def enterPassword(self, pwd):
        self.driver.find_element(By.ID, self.text_pwd).send_keys(pwd)

    def clickOnLoginBtn(self):
        self.driver.find_element(By.XPATH, self.btn_login).click()

    def checkTheText(self):
        return self.driver.find_element(By.XPATH, self.my_account_text).is_displayed()

        #       and
        #       self.driver.find_element(By.LINK_TEXT, self.my_orders_text).is_displayed() and
        #        self.driver.find_element(By.LINK_TEXT, self.my_affiliate_account_text).is_displayed()


    def editAccountInfo(self):
        self.driver.find_element(By.LINK_TEXT, self.link_edit_acc_info).click()
        """
        return (self.driver.find_element(By.ID, self.id_firstname).text() and
                self.driver.find_element(By.ID, self.id_lastname).text() and
                self.driver.find_element(By.ID, self.id_email).text())
                
        """
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.id_firstname)))
        wait.until(EC.presence_of_element_located((By.XPATH, self.id_lastname)))
        wait.until(EC.presence_of_element_located((By.XPATH, self.id_email)))

        self.fname = self.driver.find_element(By.XPATH, self.id_firstname).get_attribute("value")
        self.lname= self.driver.find_element(By.XPATH, self.id_lastname).get_attribute("value")
        self.mail = self.driver.find_element(By.XPATH, self.id_email).get_attribute("value")
        self.driver.find_element(By.XPATH, self.btn_continue).click()
        return self.fname, self.lname, self.mail

    def verifyUpdatedMsg(self):
        return self.driver.find_element(By.XPATH, self.acc_update_msg).is_displayed()

    def changePassword(self, pwd, confpwd):
        self.driver.find_element(By.XPATH, self.link_change_pwd).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.id_password).send_keys(pwd)
        self.driver.find_element(By.ID, self.id_confirm_password).send_keys(confpwd)
        self.driver.find_element(By.XPATH, self.btn_continue).click()

    def modifyAddressBookEntries(self,fname,lname,companyname,add,city,code,country):
        self.driver.find_element(By.LINK_TEXT, self.lnk_modify_address_book).click()
        self.driver.find_element(By.LINK_TEXT, self.btn_new_address).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.id_firstname).send_keys(fname)
        self.driver.find_element(By.XPATH, self.id_lastname).send_keys(lname)
        self.driver.find_element(By.ID, self.id_company).send_keys(companyname)
        self.driver.find_element(By.ID, self.id_address).send_keys(add)
        self.driver.find_element(By.ID, self.id_city).send_keys(city)
        self.driver.find_element(By.ID, self.id_postcode).send_keys(code)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)

        select= Select(self.driver.find_element(By.XPATH, "//select[@id='input-country']"))
        select.select_by_visible_text(country)

        self.driver.find_element(By.ID, self.id_default_value_yes).click()

        select1 =Select(self.driver.find_element(By.XPATH, "//select[@id='input-zone']"))
        self.driver.find_element(By.XPATH, self.btn_continue).click()

    def editAccountInfo1(self):
        self.driver.find_element(By.LINK_TEXT, self.link_edit_acc_info).click()

        # Get current values (use get_attribute for input fields)
        fname = self.driver.find_element(By.XPATH, self.id_firstname).get_attribute("value")
        lname = self.driver.find_element(By.XPATH, self.id_lastname).get_attribute("value")
        mail = self.driver.find_element(By.XPATH, self.id_email).get_attribute("value")

        try:
            # Click the "Continue" button
            self.driver.find_element(By.XPATH, self.btn_continue).click()
        except NoSuchElementException:
            print("Error: 'Continue' button not found.")  # Handle gracefully

        return fname, lname, mail

    def clickOnLogOut(self):
        self.driver.find_element(By.XPATH, self.logout).click()










