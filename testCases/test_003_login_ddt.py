import os
import time

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.CustomLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    path = os.path.abspath(os.curdir) + "\\testData\\opencart_LoginData.xlsx"


    def test_login_ddt(self, setup):
        self.logger.info("Testcase started..")
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(2)

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)

        for r in range(2, self.rows+1):
            self.hp.clickMyAccount()
            time.sleep(25)
            self.hp.clickMyAccount()
            time.sleep(3)
            self.hp.clickOnLogin()

            self.email = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtils.readData(self.path, "Sheet1",r,3)
            self.lp.enterEmailAddress(self.email)
            self.lp.enterPassword(self.password)
            self.lp.clickOnLoginBtn()
            time.sleep(3)
            try:
               self.targetpage =self.lp.checkTheText()

               if self.exp == 'Valid':
                 if self.targetpage == True:
                    lst_status.append('Pass')
                    self.hp.clickMyAccount()
                    time.sleep(2)
                    self.lp.clickOnLogOut()
                 else:
                    lst_status.append('Fail')

               elif self.exp == 'Invalid':
                 if self.targetpage == True:
                    lst_status.append('Fail')
                    self.hp.clickMyAccount()
                    time.sleep(2)
                    self.lp.clickOnLogOut()

                 else:
                    lst_status.append("Pass")
            except Exception:

                if self.targetpage==False:
                    time.sleep(2)
                    self.hp.clickMyAccount()
                    time.sleep(2)
                    self.lp.clickOnLoginBtn()

        self.driver.close()

        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("Data Driven testcase ended..")



