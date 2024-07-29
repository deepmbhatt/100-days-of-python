import smtplib
import datetime as dt
import random
import os
import pandas as pd

my_email = "[Your Email]"
password = "[Your Password]"
wishes_folder = "day32automatedbirthdaywisher/wishes"

# Get a list of files in the wishes folder
def get_files():
    try:
        files = os.listdir(wishes_folder)
        if not files:
            raise FileNotFoundError("No files found in the wishes folder")
    except FileNotFoundError as e:
        print(e)
        files = []
    return files

# Randomly select one file from the wishes folder
def make_message(name):
    files = get_files()
    selected_file = random.choice(files)
    with open(os.path.join(wishes_folder, selected_file)) as file:
        print(file)
        data = file.readlines()
        print(data)
        message = data[0].replace("[Name]", name)
        Subject = "Happy Birthday!!"
        body =f"<p>{message}</p><p>~<i><b>Regards,<br>Deep Bhatt.</b></i></p>"
        msg = f"Subject: {Subject}\nContent-Type: text/html\n\n{body}"
    return msg

# Read the data from the csv file
def read_data():
    try:
        data = pd.read_csv("day32automatedbirthdaywisher/birthdays.csv")
    except FileNotFoundError as e:
        print(e)
        data = pd.DataFrame()
    return data

def is_birthday(day, month):
    now = dt.datetime.now()
    today = now.day
    this_month = now.month
    if today == day and this_month == month:
        return True
    return False


data = read_data()
if not data.empty:
    for index, row in data.iterrows():
        print(row["day"])
        if is_birthday(row["day"], row["month"]):
            msg = make_message(row["Name"])
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email, 
                    to_addrs=row["Email"], 
                    msg = msg)
                connection.close()