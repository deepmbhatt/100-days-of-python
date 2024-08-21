from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

bug_link = driver.find_element(By.XPATH,value = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
# print(bug_link.text)
event_time = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget li a")
events = {}

for i in range(len(event_time)):
    events[i] = {
        "time": event_time[i].text,
        "name": event_name[i].text
    }
# for event in event_time:
#     print(event.text)

print(events)

driver.quit()