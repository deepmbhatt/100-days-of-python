import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.amazon.in/Samsung-Powered-Real-Time-Interpreter-Battery/dp/B0D7M34JXY/ref=sr_1_1_sspa?crid=XSPV32P3SIGD&dib=eyJ2IjoiMSJ9.IA4V3rYHsDf0IWn--OyoS9H5Lax_1l1anKcHezz-cJFntDNZp9Vaa_ZLdSDKSNqr3RNmGOPazWGyNTEUGwsOj6EgbTbicgrSa-wh2svuZ9QzRiGZctR3Kb8mj7Qe5vttNmsCd-t4Gsn67-Kb_R3Mb-YiBNvBmVm6MWA5SUsBVPPr7MYKb4QDbjx997YwyYf8Ny7_x9FVbnlwOR8VVp47ZaK9QakKwAoDR14bbpQK-ps.72h5VFMKmxu69FXcLhQ-27WIfoa1ixPiArOB0M0z23Q&dib_tag=se&keywords=samsung%2Bbuds&qid=1723987763&sprefix=samsing%2Bbuds%2Caps%2C252&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
header = {
        "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8,it-IT;q=0.7,it;q=0.6",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
response = requests.get(url, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")
#print(soup.prettify())
integer = soup.find("span", class_="a-offscreen").get_text()
# Remove the dollar sign using split
price= integer.replace(",","").replace("₹","")
price_to_float = float(price)

# Convert to floating point number
print(price_to_float)