from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(r"E:/ecomm/nopcom/venv/Lib/site-packages/chromedriver_py/91/chromedriver")
        print("chrome browser launched")
    elif browser == 'IE':
        driver = webdriver.Ie(r"E:/ecomm/nopcom/venv/Lib/site-packages/IE_driver/IE/IEDriverServer")
        print("IE browser launched")
    else:
        driver = webdriver.Firefox(r"E:/ecomm/nopcom/venv/Lib/site-packages/firefox/ff/geckodriver")
        print("Firefox browser launched")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

################ pytest html report ###############

## It is hook for adding environment details in the html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nopcom'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Rishi'

## IT is hook for delete/modify environment info into html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)

