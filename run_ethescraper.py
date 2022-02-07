import sys
from BitcoinScraper2 import *
import SendEmail
from getpass import getpass
#from time import time, sleep

# while True:
#     sleep(60 - time() % 60)
# 	# thing to run

SEARCH_URL = "https://www.coinbase.com/price/ethereum"

#get info
driver = install_driver()
go_to_page(driver, "https://www.coinbase.com/price/ethereum")
ethereum_price = get_bitcoin_price(driver)
close_browser(driver)

#send info
USER = getpass("E-mail: ")
PASS = getpass("Password: ")
data = "The ethereum price is " + ethereum_price
email = SendEmail.SendEmail(USER, PASS, data)
email.send_email(USER, PASS, data)
print("You should check your e-mail!")
sys.exit(0)
