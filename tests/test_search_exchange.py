import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

# Logging configuration
logging.basicConfig(filename='test_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Adding path to modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from page_object_pattern_webFIN.pages.base_page import BasePage


@pytest.fixture(scope="module")
def driver():
    # Path to downloaded msedgedriver
    driver_path = ""Add path to driver.exe""
    service = EdgeService(driver_path)

    # Settings for Edge browser options
    options = EdgeOptions()
    options.add_argument("--inprivate")  # Launch browser in private mode
    options.add_argument("--disable-notifications")  # Disable notifications
    options.add_argument("--disable-popup-blocking")  # Disable popup blocking
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")  # Resolves issues with some versions of Edge

    # Initialize WebDriver with service and options
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()


def test_nasdaq_search(driver):
    logging.info('Test started: test_nasdaq_search')

    try:
        # Open the website
        driver.get("https://www.nasdaq.com/")
        driver.maximize_window()

        # Initialize pages
        base_page = BasePage(driver)
        wait = WebDriverWait(driver, 10)

        # STEP 1: Accept cookies
        accept_cookies_button_xpath = '//*[@id="onetrust-accept-btn-handler"]'
        wait.until(EC.element_to_be_clickable((By.XPATH, accept_cookies_button_xpath)))
        base_page.click_element(By.XPATH, accept_cookies_button_xpath)

        # STEP 2: Enter text into the search field
        search_input1_xpath = '/html/body/div[2]/div[1]/div/header/nav/div[2]/input'
        wait.until(EC.element_to_be_clickable((By.XPATH, search_input1_xpath)))
        base_page.click_element(By.XPATH, search_input1_xpath)

        # STEP 2A: Fill the search field
        search_input2_xpath = '//*[@id="nasdaq-search-overlay-input"]'
        wait.until(EC.visibility_of_element_located((By.XPATH, search_input2_xpath)))
        base_page.fill_text_field(By.XPATH, search_input2_xpath, 'META')

        # STEP 3: Press the SEARCH button
        search_button_xpath = '//*[@id="nasdaq-search-overlay-modal"]/div[2]/div/div/div[2]/div/form/button'
        wait.until(EC.element_to_be_clickable((By.XPATH, search_button_xpath)))
        base_page.click_element(By.XPATH, search_button_xpath)

        # STEP 4: Click the VIEW button
        view_button_xpath = '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[1]/h2/a/span'
        wait.until(EC.element_to_be_clickable((By.XPATH, view_button_xpath)))
        base_page.click_element(By.XPATH, view_button_xpath)

        logging.info('Test successfully completed: test_nasdaq_search')
        assert True  # Test should pass without errors

    except Exception as e:
        logging.error(f'Error in test: {e}')
        assert False  # Test failed
