from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Samsung-Powered-Real-Time-Interpreter-Battery/dp/B0D7M34JXY/ref=sr_1_1_sspa?crid=XSPV32P3SIGD&dib=eyJ2IjoiMSJ9.IA4V3rYHsDf0IWn--OyoS9H5Lax_1l1anKcHezz-cJFntDNZp9Vaa_ZLdSDKSNqr3RNmGOPazWGyNTEUGwsOj6EgbTbicgrSa-wh2svuZ9QzRiGZctR3Kb8mj7Qe5vttNmsCd-t4Gsn67-Kb_R3Mb-YiBNvBmVm6MWA5SUsBVPPr7MYKb4QDbjx997YwyYf8Ny7_x9FVbnlwOR8VVp47ZaK9QakKwAoDR14bbpQK-ps.72h5VFMKmxu69FXcLhQ-27WIfoa1ixPiArOB0M0z23Q&dib_tag=se&keywords=samsung%2Bbuds&qid=1723987763&sprefix=samsing%2Bbuds%2Caps%2C252&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
print(price)


driver.quit()