import requests
import pprint
import datetime
import calendar

the_ip_time = datetime.datetime.now()

timezoneURL = "https://worldtimeapi.org/api/timezone"

IPtimeresponse = requests.get(f"https://worldtimeapi.org/api/ip")
IPtimeresponse.raise_for_status()
IPtimeresponse = IPtimeresponse.json()
IPtime_now = IPtimeresponse["datetime"]

timezoneresponse = requests.get(timezoneURL)
timezoneresponse.raise_for_status()
timezoneresponse = timezoneresponse.json()


def daterange(year, month):
    date = calendar.monthrange(year, month)
    range_date = []
    for i in range(1, date[1] + 1):
        range_date.append(i)
    return range_date


noneOptions = []
Africa = []
America = []
Antarctica = []
Asia = []
Atlantic = []
Australia = []
Europe = []
Indian = []
Pacific = []
Others = []
for i in timezoneresponse:
    if i[:2] == "Af":
        dash = i.find("/")
        Africa.append(i[dash + 1:])

    elif i[:2] == "Am":
        dash = i.find("/")
        America.append(i[dash + 1:])

    elif i[:2] == "An":
        dash = i.find("/")
        Antarctica.append(i[dash + 1:])

    elif i[:2] == "As":
        dash = i.find("/")
        Asia.append(i[dash + 1:])
    elif i[:2] == "At":
        dash = i.find("/")
        Atlantic.append(i[dash + 1:])
    elif i[:2] == "Au":
        dash = i.find("/")
        Australia.append(i[dash + 1:])
    elif i[:2] == "Eu":
        dash = i.find("/")
        Europe.append(i[dash + 1:])
    elif i[:2] == "In":
        dash = i.find("/")
        Indian.append(i[dash + 1:])
    elif i[:2] == "Pa":
        dash = i.find("/")
        Pacific.append(i[dash + 1:])

    else:
        Others.append(i)

select_timezone = {
    "Africa": Africa,
    "America": America,
    "Atlantic": Atlantic,
    "Asia": Asia,
    "Australia": Australia,
    "Antarctica": Antarctica,
    "Europe": Europe,
    "Indian": Indian,
    "Pacific": Pacific
}
category = {"Continent/Ocean": select_timezone, "Others": Others}

# print(Asia)


def current_time(area, location):
    timeresponse = requests.get(f"{timezoneURL}/{area}/{location}")
    timeresponse.raise_for_status()
    timeresponse = timeresponse.json()
    time_now = timeresponse["datetime"]
    return time_now


def current_time_Special(the_place):
    timeresponse = requests.get(f"{timezoneURL}/{the_place}")
    timeresponse.raise_for_status()
    timeresponse = timeresponse.json()
    time_now = timeresponse["datetime"]
    return time_now


# print(current_time("Asia", "Shanghai"))

the_year = []

for i in range(2018, 2080):
    the_year.append(i)

the_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# date = calendar.monthrange(2020,2)


def time_conversion(year, month, date, hour, minute, former_area,
                    former_location, after_area, after_location):
    d = datetime.datetime(year, month, date, hour, minute)
    timeresponse = requests.get(
        f"{timezoneURL}/{former_area}/{former_location}")
    timeresponse.raise_for_status()
    timeresponse = timeresponse.json()
    utcoffset_1 = timeresponse["utc_offset"]
    timeresponse2 = requests.get(
        f"{timezoneURL}/{after_area}/{after_location}")
    timeresponse2.raise_for_status()
    timeresponse2 = timeresponse2.json()
    utcoffset_2 = timeresponse2["utc_offset"]
    colon_1 = utcoffset_1.find(":")
    first_offset_hour = int(utcoffset_1[:colon_1])
    first_offset_minute = int(utcoffset_1[colon_1 + 1:])
    colon_2 = utcoffset_2.find(":")
    second_offset_hour = int(utcoffset_2[:colon_2])
    second_offset_minute = int(utcoffset_2[colon_2 + 1:])
    delta_hour = second_offset_hour - first_offset_hour
    delta_minute = second_offset_minute - first_offset_minute
    newtime = d + datetime.timedelta(hours=delta_hour) + datetime.timedelta(
        minutes=delta_minute)
    return newtime


def check_whether_work(a, b, c, d, e, f, g, h, i):
    if a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "" or i == "":
        return False
    else:
        return True
