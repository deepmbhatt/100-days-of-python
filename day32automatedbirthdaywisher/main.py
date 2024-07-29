import smtplib
import datetime as dt
import random

my_email = "deeppythonprojects@gmail.com"
password = "ragrptyuhkfzvxqu"

try:
    with open("day32automatedbirthdaywisher/quotes.txt") as file:
        data = file.readlines()
except FileNotFoundError:
    print("File not found")

data = [line.strip() for line in data]
message = random.choice(data)
message = message.split("~")
print(message)
quote = message[0]
author = message[1]
Subject = "Monday Motivation"
body =f"<p>{quote}</p><p>~<i><b>{author}</b></i></p>"
msg = f"Subject: {Subject}\nContent-Type: text/html\n\n{body}"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="deepmanishbhatt@gmail.com", 
            msg = msg)
        connection.close()