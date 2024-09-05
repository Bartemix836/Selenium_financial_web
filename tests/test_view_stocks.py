import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from page_object_pattern_webFIN.pages.base_page import BasePage

@pytest.fixture(scope="module")
def driver():
    # Path to downloaded msedgedriver
    driver_path = "Add path to driver.exe"
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

def test_nasdaq(driver):
    # Open the website
    driver.get("https://www.nasdaq.com/")
    driver.maximize_window()

    # Initialize pages
    base_page = BasePage(driver)
    wait = WebDriverWait(driver, 10)

    # STEP 1: Accept cookies (ACCEPT button)
    accept_cookies_button_xpath = '//*[@id="onetrust-accept-btn-handler"]'
    wait.until(EC.element_to_be_clickable((By.XPATH, accept_cookies_button_xpath)))
    base_page.click_element(By.XPATH, accept_cookies_button_xpath)

    # STEP 2: Navigate to the screener option
    screener_option_xpath = '/html/body/div[2]/div[1]/main/div[2]/article/div[2]/div[2]/aside/nsdq-right-rail-desktop/div/div[1]/div/div[1]/form/div/div[1]/a'
    wait.until(EC.element_to_be_clickable((By.XPATH, screener_option_xpath)))
    base_page.click_element(By.XPATH, screener_option_xpath)

    # STEP 3: Navigate to the STOCKS tab
    stocks_tab_xpath = '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[1]/div[1]/button[1]'
    wait.until(EC.element_to_be_clickable((By.XPATH, stocks_tab_xpath)))
    base_page.click_element(By.XPATH, stocks_tab_xpath)

    # STEP 4: Select criteria
    global_market_label_xpath = '//*[@id="filterModal"]/div/div[2]/div[1]/div/div/label[1]/span[2]'
    wait.until(EC.element_to_be_clickable((By.XPATH, global_market_label_xpath)))
    base_page.click_element(By.XPATH, global_market_label_xpath)

    market_cap_medium_xpath = '//*[@id="filterModal"]/div/div[2]/div[2]/div/div/label[3]/span[2]'
    wait.until(EC.element_to_be_clickable((By.XPATH, market_cap_medium_xpath)))
    base_page.click_element(By.XPATH, market_cap_medium_xpath)

    sector_financials_xpath = '//*[@id="filterModal"]/div/div[2]/div[4]/div/div/label[4]/span[2]'
    wait.until(EC.element_to_be_clickable((By.XPATH, sector_financials_xpath)))
    base_page.click_element(By.XPATH, sector_financials_xpath)

    # STEP 5: Click the APPLY button
    apply_button_xpath = '//*[@id="filterModal"]/div/div[3]/button[1]'
    wait.until(EC.element_to_be_clickable((By.XPATH, apply_button_xpath)))
    base_page.click_element(By.XPATH, apply_button_xpath)

    # STEP 6: Download the CSV file with stock values
    download_csv_button_xpath = '/html/body/div[2]/div/main/div[2]/article/div[3]/div[1]/div/div/div[3]/div[2]/div[2]/div/button'
    wait.until(EC.element_to_be_clickable((By.XPATH, download_csv_button_xpath)))
    base_page.click_element(By.XPATH, download_csv_button_xpath)

    # STEP 7: Go to the details of the selected MKTX stock
    mktx_stock_xpath = '/html/body/div[2]/div/main/div[2]/article/div[3]/div[1]/div/div/div[3]/div[3]/table/tbody/tr[1]/th/a'
    wait.until(EC.element_to_be_clickable((By.XPATH, mktx_stock_xpath)))
    base_page.click_element(By.XPATH, mktx_stock_xpath)

    print("TEST CASE COMPLETED SUCCESSFULLY")
