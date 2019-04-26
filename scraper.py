# ______________________________________________________________________________________________________
# scrape currency conversion rates 
# ______________________________________________________________________________________________________
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import requests

XE_URL = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=MYR&To=INR'

def get_HTML_page():
    # Start the WebDriver and load the page
    wd = webdriver.Chrome()
    wd.get(XE_URL)

    # Wait for the dynamically loaded elements to show up
    WebDriverWait(wd, 2).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "converterresult-toAmount")))

    # And grab the page HTML source
    html_page = wd.page_source
    wd.quit()
    return html_page


class XE():

    def __init__(self,data):
        self.html_page = data
        self.XE_page = BeautifulSoup(self.html_page, 'html.parser')
        self.To_Value = self.XE_page.find('span',attrs={"class":"converterresult-toAmount"}).text

# invoke main
if __name__ == "__main__":
    XE1 = XE(get_HTML_page())
    print (XE1.To_Value)