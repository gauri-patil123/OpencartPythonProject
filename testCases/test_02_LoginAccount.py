import os.path
import time
import unittest
from email.headerregistry import Address

import pytest

from selenium import webdriver

import enums
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGen


@pytest.mark.sanity
class Test_02_LoginAccount():
    logger = LogGen.loggen()

    def test_loginaccount(self, setup):
        self.driver = setup
        self.logger.info("open the URL")
        self.driver.get(ReadConfig.getApplicationURL())
        self.driver.maximize_window()
        time.sleep(2)
        self.logger.info("Testcase is started")
        self.hp =HomePage(self.driver)
        time.sleep(2)
        self.hp.clickMyAccount()
        time.sleep(20)
        self.hp.clickMyAccount()
        time.sleep(2)
        self.hp.clickOnLogin()
        time.sleep(2)

        self.lp =LoginPage(self.driver)
        self.lp.enterEmailAddress(ReadConfig.getUserName())
        self.lp.enterPassword((ReadConfig.getPassword()))
        self.lp.clickOnLoginBtn()
        time.sleep(3)
        result = self.lp.checkTheText()
        assert result==True

        first_name, last_name, email = self.lp.editAccountInfo1()
        time.sleep(2)
        assert first_name=="Sanjana",f"Expected {"Sanjana"}, but got {first_name}"
        assert last_name == "Patil", f"Expected {"Patil"}, but got {last_name}"
        assert email == "watch21@gmail.com", f"Expected {"watch21@gmail.com"}, but got {email}"

        time.sleep(3)
        msg=self.lp.verifyUpdatedMsg()
        assert msg==True
        """
        if msg== " Success: Your account has been successfully updated.":
            print("Account is editable")
        else:
            print("Account is not editable")
        """

        self.lp.changePassword(enums.CustomerEnum.CHANGE_PASSWORD.value,enums.CustomerEnum.CONFIRM_PASSWORD.value)
        time.sleep(5)
        self.lp.modifyAddressBookEntries(enums.CustomerEnum.FIRSTNAME.value,enums.CustomerEnum.LASTNAME.value,enums.CustomerEnum.COMPANY.value,enums.CustomerEnum.ADDRESS.value,enums.CustomerEnum.CITY.value,
                                         enums.CustomerEnum.PINCODE.value,enums.CustomerEnum.COUNTRY.value)
        time.sleep(3)
        self.driver.save_screenshot(os.path.abspath(os.curdir) + '\\screenshots\\'+'addressbook.png')
        self.logger.info("Testcase is finished")
        self.driver.close()






