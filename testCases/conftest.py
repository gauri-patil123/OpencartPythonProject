import os.path
from datetime import datetime

import pytest
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from testCases.test_01_AccountRegistration import Test_01_AccountReg


@pytest.fixture()
def setup(browser):
   if browser == 'edge':
       options = webdriver.EdgeOptions()
       driver_manager = EdgeChromiumDriverManager()
       service = Service(driver_manager.install())
       driver = webdriver.Edge(service=service,options=options)
       print("Launching edge browser")

   elif browser == 'firefox':
       options = webdriver.FirefoxOptions()
       driver_manager = GeckoDriverManager()
       service = Service(driver_manager.install())
       driver = webdriver.Firefox(service=service, options=options)
       print("Launching firefox browser")

   else:
       options = webdriver.ChromeOptions()
       driver_manager = ChromeDriverManager()
       service=Service(driver_manager.install())
       driver = webdriver.Chrome(service=service, options=options)
       print("Launching chrome browser")

   return driver
# This will get the value from hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")

## pytest HTML report ###
# It is hook for adding Env info into HTML report
def pytest_configure(config):
    config.metadata['Project Name'] = "Opencart"
    config.metadata['Module Name'] = "CustRegAndLogin"
    config.metadata['Tester'] = "Sanjana Patil"

# It is hook for delete/modify environment onfo to HTML report
@pytest.mark.optinalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"













