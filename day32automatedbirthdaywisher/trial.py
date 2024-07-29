import smtplib

my_email = "[Your Email]"
password = "[Your Password]"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="[Reciever Email]", 
        msg = "Subject:Trial\n\nThis is a trial message")
    connection.close()
