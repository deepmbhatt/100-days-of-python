from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

ACCOUNT_EMAIL = "YOUR_EMAIL_HERE"
ACCOUNT_PASSWORD = 'YOUR_PW_HERE'
PHONE = 'YOUR PHONE HERE'

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102713980&keywords=python%20developer&location=India")

time.sleep(2)

sign_in = driver.find_element(By.CLASS_NAME, value = 'nav__button-secondary')
sign_in.click()

time.sleep(2)

email = driver.find_element(By.ID, value = 'username')
email.send_keys(ACCOUNT_EMAIL)

password = driver.find_element(By.ID, value = 'password')
password.send_keys(ACCOUNT_PASSWORD)

sign_in_button = driver.find_element(By.CSS_SELECTOR, value = '.login__form_action_container button')
sign_in_button.click()

time.sleep(5)

job_list = driver.find_elements(By.CSS_SELECTOR, value = '.job-card-container--clickable')

for job in job_list:
    job.click()
    time.sleep(2)
    try:
        apply = driver.find_element(By.CSS_SELECTOR, value = '.jobs-s-apply button')
        apply.click()

        time.sleep(2)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)
        
        submit = driver.find_element(By.CSS_SELECTOR, value = 'footer button')
        submit.click()
    except:
        pass

    time.sleep(2)
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

time.sleep(5)

driver.quit()

