from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
import smtplib

search_url = "https://www.coinbase.com/price/bitcoin"

#Install Driver
driver = webdriver.Chrome(ChromeDriverManager().install())

#Specify search URL
search_url = "https://www.coinbase.com/price/bitcoin"
driver.get(search_url)

#Locate the images to be scraped from the current page 
element = driver.find_element_by_xpath('.//span[@class = "AssetChartAmount__Number-sc-1b4douf-1 foyTCz"]')
price = str(element.text)
price = price.replace(" €", "")
driver.close()

# set up the SMTP server
USER = getpass("E-mail: ")
PASS = getpass("Password: ")
data = "The bitcoin price is " + price
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(USER, PASS)
s.sendmail(USER, USER, data)
print("Please check your e-mail box!")
s.quit()




