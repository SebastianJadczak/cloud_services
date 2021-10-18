import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    """Base class that initializes the driver and closes the browser after executing the test."""

    url = 'https://app.bluealert.pl/ba/form/formularz-testowy'
    @pytest.fixture()
    def setup(self):
        """Browser initialization, window maximization delay, and closing the browser window after the test completes"""
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.quit()