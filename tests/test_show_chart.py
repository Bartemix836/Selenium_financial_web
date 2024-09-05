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


def test_nasdaq_navigation(driver):
    logging.info('Test started: test_nasdaq_navigation')

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

        # STEP 2: Navigate to the MARKETS tab
        markets_tab_xpath = '/html/body/div[2]/div[1]/main/div[2]/article/div[2]/div[2]/div/div/section[1]/div[2]/div/a[2]'
        wait.until(EC.element_to_be_clickable((By.XPATH, markets_tab_xpath)))
        base_page.click_element(By.XPATH, markets_tab_xpath)

        # STEP 3: Navigate to the COMPANIES tab
        companies_tab_xpath = '//*[@id="nav-id"]/div/ul[2]/li[3]/a'
        wait.until(EC.element_to_be_clickable((By.XPATH, companies_tab_xpath)))
        base_page.click_element(By.XPATH, companies_tab_xpath)

        # STEP 4: Navigate to a detailed chart of a selected company's stock
        company_chart_css = 'a.jupiter22-c-quote-tag.jupiter22-c-quote-tag--down'
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, company_chart_css)))
        base_page.click_element(By.CSS_SELECTOR, company_chart_css)

        # STEP 5: Change the period to 5D
        five_day_button_xpath = '/html/body/div[2]/div/main/div[2]/article/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/button'
        wait.until(EC.element_to_be_clickable((By.XPATH, five_day_button_xpath)))
        base_page.click_element(By.XPATH, five_day_button_xpath)

        logging.info('Test successfully completed: test_nasdaq_navigation')
        assert True  # Test should pass without errors

    except Exception as e:
        logging.error(f'Error in test: {e}')
        assert False  # Test failed
