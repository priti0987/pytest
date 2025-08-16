import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--my-browser",action="store",default="chrome",
                     help="Specify the browser or firefox or edge ")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--my-browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    return driver