from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

# Initialize the WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Start the browser and navigate to the URL
url = "https://appbrewery.github.io/Zillow-Clone/"
driver.get(url)
time.sleep(4.2)

# Function to split the string by '/' or '+'
def split_string(input_string):
    parts = re.split(r'[\/+]', input_string)
    return parts[0]

# Get data from the website
price_elements = driver.find_elements(by=By.CLASS_NAME, value='PropertyCardWrapper span')
prices = [split_string(element.text) for element in price_elements]

address_elements = driver.find_elements(by=By.CLASS_NAME, value='StyledPropertyCardDataWrapper address')
addresses = [(element.text).replace('\n', ' ').strip() for element in address_elements]

link_elements = driver.find_elements(by=By.CLASS_NAME, value='StyledPropertyCardDataWrapper a')
links = [element.get_attribute('href') for element in link_elements]

# Fill the form with the data
driver.get("https://forms.gle/vT5jtnKyioJN1dkU6")
time.sleep(4)

for i in range(len(prices)):
    address_bar = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    price_bar = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_bar = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    

    address_bar.send_keys(addresses[i])
    price_bar.send_keys(prices[i])
    link_bar.send_keys(links[i])
    submit_button.click()
    time.sleep(2)
    submit_another = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another.click()
    time.sleep(2)

# Close the browser
driver.quit()
