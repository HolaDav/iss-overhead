import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 6.517760
MY_LONG = 3.256870
MY_EMAIL = "devdavdemo@gmail.com"
PASSWORD = "oqwwnjexzrriaeza"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()


iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def iss_position_range():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT+5 and MY_LONG - 5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()

while True:
    time.sleep(60)
    if iss_position_range():
        if sunset <= time_now.hour <= sunrise:
            with smtplib.SMTP(host="smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs="oladejidavid12@gmail.com",
                                    msg="Subject:ISS Location\n\n"
                                        "Look Up, the International Space Station current "
                                        "location is close to you")




