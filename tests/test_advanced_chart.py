import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

# Adding path to modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from page_object_pattern_webFIN.pages.base_page import BasePage

@pytest.fixture(scope="module")
def driver():
    # Path to downloaded msedgedriver
    driver_path = "C:/Users/barte/PycharmProjects/selenium_kurs/drivers/msedgedriver.exe"
    service = EdgeService(driver_path)

    # Settings for Edge browser options
    options = EdgeOptions()
    options.add_argument("--inprivate")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")

    # Initialize WebDriver with service and options
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()

def test_nasdaq_search(driver):
    # Open the website
    driver.get("https://www.nasdaq.com/")
    driver.maximize_window()

    # Initialize pages
    base_page = BasePage(driver)
    wait = WebDriverWait(driver, 10)

    try:
        # STEP 1: Accept cookies (ACCEPT button)
        accept_cookies_button_xpath = '//*[@id="onetrust-accept-btn-handler"]'
        base_page.click_element(By.XPATH, accept_cookies_button_xpath)

        # STEP 2: Enter text into the search field
        search_input1_xpath = '/html/body/div[2]/div[1]/div/header/nav/div[2]/input'
        base_page.click_element(By.XPATH, search_input1_xpath)

        # STEP 2A: Fill the search field
        search_input2_xpath = '//*[@id="nasdaq-search-overlay-input"]'
        base_page.fill_text_field(By.XPATH, search_input2_xpath, "META")

        # STEP 3: Press the SEARCH button
        search_button_xpath = '//*[@id="nasdaq-search-overlay-modal"]/div[2]/div/div/div[2]/div/form/button'
        base_page.click_element(By.XPATH, search_button_xpath)

        # STEP 4: Click the VIEW button
        view_button_xpath = '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[1]/h2/a/span'
        base_page.click_element(By.XPATH, view_button_xpath)

        # STEP 5: Switch to advanced charting mode
        advanced_charting_url = "https://www.nasdaq.com/market-activity/stocks/meta/advanced-charting"
        driver.get(advanced_charting_url)

        # STEP 6: Go to the screener
        screener_xpath = '/html/body/div[2]/div/main/div[2]/article/div/div[2]/div/div[4]/nsdq-qd-right-rail-desktop/div/div/div[1]/div/div[1]/form/div/div[1]/a'
        base_page.click_element(By.XPATH, screener_xpath)

        # STEP 7: Select an option from the SELECT dropdown
        select_xpath = '//*[@id="indextype"]'
        auto_select = Select(wait.until(EC.element_to_be_clickable((By.XPATH, select_xpath))))
        auto_select.select_by_visible_text("US")

        # STEP 8: Apply filters, APPLY button
        apply_btn_xpath = 'symbol-screener__apply-button'
        base_page.click_element(By.CLASS_NAME, apply_btn_xpath)

        # If everything passes, the test was successful
        print("TEST CASE COMPLETED SUCCESSFULLY")

    except Exception as e:
        pytest.fail(f"An error occurred: {e}")
