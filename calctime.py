import mysql.connector
import requests
import json
from requests.models import Response

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Anuj 2265",
    database = "data"
)

mycursor = mydb.cursor()

def time(lat,long):
    lat = str(lat)
    long = str(long)
    request = requests.get(f"http://api.timezonedb.com/v2.1/get-time-zone?key=9JI50KSYU1BW&format=json&by=position&lat={lat}&lng={long}")
    response = request.json()
    finaltime = response["formatted"]
    Date = finaltime[0:10]
    Time = finaltime[11:18]
    list = [Date, Time]
    return list