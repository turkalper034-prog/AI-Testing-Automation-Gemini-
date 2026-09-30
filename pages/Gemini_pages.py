
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage


class Gemini_Page(BasePage):
    input_name = (By.XPATH,"//div[@data-placeholder=\"Gemini'a sorun\"]")
    enter_submit =(By.XPATH,"//button[@aria-label='Mesaj gönder']")
    enter_response = (By.XPATH,"//message-content[starts-with(@id, 'message-content-id')]")
    def enter_prompt(self,prompt):
        input_name = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((self.input_name)))
        input_name.send_keys(prompt)
    def enter_send(self):
        self.driver.find_element(*self.enter_submit).click()

    def get_response(self):
        enter_respone = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((self.enter_response)))
        return enter_respone.text



