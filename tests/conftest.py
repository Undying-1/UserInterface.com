import pytest
import time
from selenium import webdriver
from utils import ReadConfiguration








@pytest.fixture
def setup_and_teardown(request):
    browser = ReadConfiguration.read_configuration('basic info', 'browser')
    global driver
    driver = None
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = ReadConfiguration.read_configuration('basic info', 'url')
    driver.get(url)
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()