import requests

import pytz

import datetime as datetime

#import html2text

url = 'https://www.rbc.ru/finances/02/10/2021/6156fa3a9a794780d46e1ea5'

text = requests.get(url).text

title = text.partition('<meta name="title" content="')

title = title[2].partition(' :: ')

print('Категория -',title[0])

subtitle = text.partition('article_categories: ["')

subtitle = subtitle[2].partition('"]')

print('keywords -', subtitle[0])

tags = text.partition('<meta name="keywords" content="')

tags = tags[2].partition('"/>')

print('Теги -',tags[0])

author = text.partition('article_authors: ["')

author = author[2].partition('"]')

print('Автор -',author[0])

time = text.partition('article_publication_date: "')
time = time[2].partition('",\n')

#Sat, 02 Oct 2021 10:00:26 +0300

timer = datetime.strptime(time[0], "%a, %d %b %Y %H:%M:%S %z")

currentZone = pytz.timezone('Europe/Moscow')

newTime = currentZone.localize(timer, is_dst=None)

timeUTC = newTime.astimezone(pytz.utc)

print(timer.astimezome(utc))
