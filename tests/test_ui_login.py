import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield d
    d.quit()


@pytest.mark.ui
def test_invalid_login_creates_artifacts(driver):
    page = LoginPage(driver)
    page.open()
    page.login("wrong", "wrong")

    # Correct assertion (should PASS)
    assert "Your username is invalid" in page.flash_text()

