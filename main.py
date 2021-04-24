import datetime
import requests
import time
from src import checkDay

url = "" # TOKEN GOES HER

while True:
 currentTime = "{hour}:{minute}:{second}".format(hour=datetime.datetime.now().hour, minute=datetime.datetime.now().minute, second=datetime.datetime.now().second)
 if currentTime == "10:25:0":
    r = requests.post(url, json=checkDay.check())
    time.sleep(1)
       
       ### some stupid stuff here ###
       # message = input()
       # r = requests.post(url, data={"content": message})

