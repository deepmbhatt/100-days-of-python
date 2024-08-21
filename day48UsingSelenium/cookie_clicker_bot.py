from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value = 'cookie')   # for cookie.click()



cursor = driver.find_element(By.ID, value = 'buyCursor')    # for cursor.click()
grandma = driver.find_element(By.ID, value = 'buyGrandma')  # for grandma.click()
factory = driver.find_element(By.ID, value = 'buyFactory')  # for factory.click()
mine = driver.find_element(By.ID, value = 'buyMine')    # for mine.click()
shipment = driver.find_element(By.ID, value = 'buyShipment')    # for shipment.click()
alchemy_lab = driver.find_element(By.ID, value = 'buyAlchemy lab')  # for alchemy_lab.click()
portal = driver.find_element(By.ID, value = 'buyPortal')    # for portal.click()
time_machine = driver.find_element(By.ID, value = 'buyTime machine')    # for time_machine.click()

items = [cursor, grandma, factory, mine, shipment, alchemy_lab, portal, time_machine]   # for clicking the highest item
items_id = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTimemachine"] # for clicking the highest item
time_out = time.time() + 5  # for clicking the highest item or upgrades
five_min = time.time() + 5*60   # for total time of 5 minutes
while True:
    time_sec = time.time() + 5
    cookie.click()
    if time.time() > time_out:  # at every 5 seconds
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b") # for getting the prices of the items
        cookie_count = driver.find_element(By.ID, value = 'money')  # for getting the cookie count
        prices = [] # for storing the prices of the items
        for price in all_prices:    
            element_text = price.text
            if element_text != "":  
                cost = int(element_text.split("-")[1].strip().replace(",", "")) # for getting the cost of the items
                prices.append(cost)
        for i in range(len(items)): 
            if int(cookie_count.text) >= prices[i]: # for buying the items highest
                max = i
        highest = items_id[max]
        driver.find_element(By.ID, value = highest).click() # for clicking the highest item

        time_out = time.time() + 5  # for clicking the highest item or upgrades
    if time.time() > five_min:  # for total time of 5 minutes
        cookie_per_sec = driver.find_element(By.ID, value = 'cps')
        print(cookie_per_sec.text)
        break
        
