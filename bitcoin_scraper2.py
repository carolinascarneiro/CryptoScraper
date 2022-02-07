from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass

def install_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

def go_to_page(driver, SEARCH_URL):
    driver.get(SEARCH_URL)  

def get_bitcoin_price(driver):
    html_element = driver.find_element_by_xpath('.//span[@class = "AssetChartAmount__Number-sc-1b4douf-1 foyTCz"]')
    bitcoin_price = html_element.text
    bitcoin_price = bitcoin_price.replace(" €", "")
    return bitcoin_price

def close_browser(driver):
    driver.close()









