# ______________________________________________________________________________________________________
# scrape currency conversion rates 
# ______________________________________________________________________________________________________
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import requests
import datetime
import time

XE_URL = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=MYR&To=INR'
WA_URL = 'https://web.whatsapp.com/'

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

def Call_Watsapp():
    # Start the WebDriver and load the page
    wa = webdriver.Chrome()
    wa.get(WA_URL)

    target = 'Tundey-Kababi'

    wait30 = WebDriverWait(wa, 10)
    wait10 = WebDriverWait(wa, 10)
    wait5  = WebDriverWait(wa, 5)

    x_arg = '//span[contains(@title, Jalal)]'
    try:
        wait10.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    except:
    # If contact not found, then search for it
        searBoxPath = '//*[@id="input-chatlist-search"]'
        wait5.until(EC.presence_of_element_located((By.ID, "input-chatlist-search")))
        inputSearchBox = wa.find_element_by_id("input-chatlist-search")
        time.sleep(0.5)
        # click the search button
        wa.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div/button').click()
        time.sleep(1)
        inputSearchBox.clear()
        inputSearchBox.send_keys(target[1:len(target) - 1])
        print('Target Searched')
        # Increase the time if searching a contact is taking a long time
        time.sleep(4)

    # Select the target
    wa.find_element_by_xpath(x_arg).click()
    print("Target Successfully Selected")
    time.sleep(2)

    # Select the Input Box
    inp_xpath = "//div[@contenteditable='true']"
    input_box = wait10.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    time.sleep(1)

    # Send message
    # taeget is your target Name and msgToSend is you message
    input_box.send_keys("Hello, " + target + "."+ Keys.SHIFT + Keys.ENTER + 'TESTING-script' + Keys.SPACE) # + Keys.ENTER (Uncomment it if your msg doesnt contain '\n')
    # Link Preview Time, Reduce this time, if internet connection is Good
    time.sleep(10)
    input_box.send_keys(Keys.ENTER)
    print("Successfully Send Message to : "+ target + '\n')

    time.sleep(0.5)

    # # Wait for the dynamically loaded elements to show up
    # WebDriverWait(wd, 2).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "converterresult-toAmount")))

    # And grab the page HTML source
    html_page = wa.page_source
    wa.quit()
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

    # Call Watsapp
    WA = Call_Watsapp()
