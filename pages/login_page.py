from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, u: str, p: str):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(u)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(p)
        self.driver.find_element(*self.BTN).click()

    def flash_text(self) -> str:
        return self.driver.find_element(*self.FLASH).text
