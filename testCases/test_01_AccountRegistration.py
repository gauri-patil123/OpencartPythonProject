import os.path
import time

import pytest

from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig

@pytest.mark.regression
class Test_01_AccountReg:
    baseURL = ReadConfig.getApplicationURL()

    def test_account_reg(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        time.sleep(20)
        self.hp.clickMyAccount()
        time.sleep(25)
        self.hp.clickMyAccount()
        time.sleep(2)
        self.hp.clickOnRegister()
        time.sleep(20)

        self.regpage = AccountRegistrationPage(self.driver)
        time.sleep(2)
        self.regpage.setFirstName("Sanjana")
        self.regpage.setLastName("Patil")
        self.regpage.enterEmail(ReadConfig.getUserName())
        self.regpage.enterPassword(ReadConfig.getPassword())
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        self.regpage.chcekPrivacyPolicyBtn()
        self.regpage.clickOnContinueBtn()
        time.sleep(5)
        self.confirmMsg= self.regpage.verifyMsgAccountCreated()
        if self.confirmMsg == "Your Account Has Been Created!" :
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" +"accountreg.png")
            assert False
        self.driver.close()



