from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from constants import name, password
import time
from bs4 import BeautifulSoup
def login(browser):
    browser.get("https://www.fidelity.com/")
    browser.refresh()
    time.sleep(10)
    username = browser.find_element_by_id('userId-input')
    username.send_keys(name)
    pw = browser.find_element_by_id('password')
    pw.send_keys(password)
    browser.find_element_by_id("fs-login-button").click()
    time.sleep(10)
browser = webdriver.Chrome("./chromedriver")
login(browser)
browser.forward()
while "error" in browser.current_url:
    login(browser)
    # to do, when login fails (goes to error page, should run login again)
soup = BeautifulSoup(browser.page_source, 'html.parser')
totals = soup.select('span.ledger--section-total.js-total-balance-value')
for total in totals:
    print(total.getText())
browser.quit()

 