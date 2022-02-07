from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
import SendEmail

SEARCH_URL = "https://www.coinbase.com/price/ethereum"

def install_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

def go_to_page(driver):
    driver.get(SEARCH_URL)  

def get_ethereum_price(driver):
    html_element = driver.find_element_by_xpath('.//span[@class = "AssetChartAmount__Number-sc-1b4douf-1 foyTCz"]')
    ethereum_price = html_element.text
    ethereum_price = ethereum_price.replace(" €", "")
    return ethereum_price

def close_browser(driver):
    driver.close()