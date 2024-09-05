from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def hover_over_element(self, by, value):
        try:
            element_to_hover_over = self.driver.find_element(by, value)
            hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
            hover.perform()
            print("Najechano na element")
        except Exception as e:
            print(f"Nie udało się najechać na element: {e}")

    def click_element(self, by, value):
        try:
            element_to_click = self.driver.find_element(by, value)
            element_to_click.click()
            print("Kliknięto element")
        except Exception as e:
            print(f"Nie udało się kliknąć elementu: {e}")

    def fill_text_field(self, by, value, text):
        try:
            text_field = self.driver.find_element(by, value)
            text_field.send_keys(text)
            print(f"Wprowadzono tekst '{text}' do pola tekstowego")
        except Exception as e:
            print(f"Nie udało się wprowadzić tekstu do pola tekstowego: {e}")

    def select_radio_button(self, by, value):
        try:
            radio_button = self.driver.find_element(by, value)
            if not radio_button.is_selected():
                radio_button.click()
                print(f"Wybrano przycisk radiowy o XPATH: {value}")
            else:
                print(f"Przycisk radiowy o XPATH: {value} już jest wybrany")
        except Exception as e:
            print(f"Nie udało się wybrać przycisku radiowego: {e}")

    def select_checkbox(self, by, value):
        try:
            checkbox = self.driver.find_element(by, value)
            if not checkbox.is_selected():
                checkbox.click()
                print(f"Zaznaczono checkbox o XPATH: {value}")
            else:
                print(f"Checkbox o XPATH: {value} już jest zaznaczony")
        except Exception as e:
            print(f"Nie udało się zaznaczyć checkboxa: {e}")



    def select_dropdown_option_by_xpath(self, xpath):
        try:
            option = self.driver.find_element(By.XPATH, xpath)
            option.click()
            print(f"Wybrano opcję z listy rozwijanej o XPATH: {xpath}")
        except Exception as e:
            print(f"Nie udało się wybrać opcji z listy rozwijanej: {e}")

    def refresh_page(self, url):
        try:
            self.driver.get(url)
            print(f"Strona została załadowana z adresu: {url}")
        except Exception as e:
            print(f"Nie udało się załadować strony z adresu: {url} - {e}")