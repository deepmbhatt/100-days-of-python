from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
PROMISED_DOWN = 25
PROMISED_UP = 25
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)

        continue_btn = self.driver.find_element(By.ID, value = 'onetrust-accept-btn-handler')
        continue_btn.click()

        go_button = self.driver.find_element(By.CLASS_NAME, value = 'start-text')
        go_button.click()

        time.sleep(60)

        self.down = driver.find_element(By.CLASS_NAME, value='download-speed').text
        self.up = driver.find_element(By.CLASS_NAME, value='upload-speed').text

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(2)

        email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[1]/div/span')
        email.send_keys(TWITTER_EMAIL)

        next = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span')
        next.click()

        time.sleep(2)

        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[1]/div/span')
        password.send_keys(TWITTER_PASSWORD)

        login = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
        login.click()

        time.sleep(5)

        tweet_compose = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()




bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()



driver.quit()