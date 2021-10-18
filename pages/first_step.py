from selenium.webdriver.common.by import By
import logging


class FirstStepPage:
    """The class responsible for the Contact tab."""

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.first_name_input_by_id = 'id_first_name'
        self.last_name_input_by_id = 'id_last_name'
        self.email_input_by_id = 'id_email'
        self.phone_input_by_id = 'id_phone'
        self.pesel_input_by_id = 'id_pesel'
        self.id_number_input_by_id = 'id_id_numer'
        self.date_input_by_id = 'id_date'
        self.next_button_by_id = 'form_button_next'

    def complete_first_step(self, first_name, last_name, email, phone, pesel, id_number, date):
        """Filling in the first step of the form."""
        self.logger.info('Filling in the first step of the form.')
        self.driver.find_element(By.ID, self.first_name_input_by_id).send_keys(first_name)
        self.driver.find_element(By.ID, self.last_name_input_by_id).send_keys(last_name)
        self.driver.find_element(By.ID, self.email_input_by_id).send_keys(email)
        self.driver.find_element(By.ID, self.phone_input_by_id).send_keys(phone)
        self.driver.find_element(By.ID, self.pesel_input_by_id).send_keys(pesel)
        self.driver.find_element(By.ID, self.id_number_input_by_id).send_keys(id_number)
        self.driver.find_element(By.ID, self.date_input_by_id).send_keys(date)
        self.driver.find_element(By.ID, self.first_name_input_by_id).click()
        self.driver.find_element(By.ID, self.next_button_by_id).click()