import os
import requests
from datetime import datetime
import smtplib

API_ENDPOINT = "https://api.quotable.io/random"
TODAY = datetime.now()
MY_GMAIL = os.environ.get("MY_GMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
RECEIVER_GMAIL = os.environ.get("RECEIVER_GMAIL")

response = requests.get(API_ENDPOINT)
response.raise_for_status()
data = response.json()
quote = data["content"]
quote_author = data["author"]
weekday = TODAY.weekday()

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_GMAIL, to_addrs=RECEIVER_GMAIL, msg=f"Subject:Motivational Quote Of Monday\n\n"
                                                                             f"\"{quote}\"\n\t\t - {quote_author}")



















