import datetime
import json
import sys


# Enum for the days of the week
weekday = (
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo"
)


weekday_en = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)


# The time at which Chiaki acts each day of the week
# It contains 7 items for each of the 7 days of the week
# Each item contains 2 items: (hour, minute)
timetable = (
    (7, 00),
    (7, 00),
    (7, 00),
    (7, 00),
    (7, 00),
    (12, 00),
    (12, 00)
)


def Today():
    return weekday[datetime.datetime.now().weekday() % len(weekday)]


def Tomorrow():
    return (datetime.datetime.now().weekday() + 1) % len(weekday)


def Image():
    with open(f"{sys.path[0]}/assets/images.json", "r") as file:
        return json.load(file)[Today()]


def Footer():
    with open(f"{sys.path[0]}/assets/images.json", "r") as file:
        return json.load(file)["Footer"]
