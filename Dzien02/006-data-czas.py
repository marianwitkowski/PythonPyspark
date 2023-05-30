
# Data i czas w Pythonie

import datetime
#from datetime import time, date, datetime, timedelta
import dateparser

# biezący date i czas
print(datetime.datetime.now())
print(datetime.datetime.now().time())
print(datetime.datetime.now().date())

# tworzenie obiektu daty
d1 = datetime.date(2023, 5, 30)
print(d1)
d1 = datetime.date.fromtimestamp(3600*26)
print(d1)
d1 = datetime.date.fromisoformat("2023-05-30")
print(d1)
d1 = datetime.datetime.fromisoformat("2023-05-30T12:34:56")
print(d1)

today = datetime.date.today()
print(today.year, today.month, today.day)

t1 = datetime.time()
print(t1)
t1 = datetime.time(12,34,56)
print(t1)
t1 = datetime.time(12,34,56,789)
print(t1, t1.hour, t1.minute, t1.second, t1.microsecond)

dt1 = datetime.datetime(2023, 5, 30, 13, 00, 00, 1234)
print(dir(dt1))

# badanie odległości pomiędzy datami
dt1 = datetime.date(2023, 1, 1)
dt2 = datetime.date(2023, 5, 30)
dt3 = dt2 - dt1
print(type(dt3), dt3.total_seconds())

dt1 = datetime.datetime(2023, 5, 30, 8, 0, 0)
dt2 = datetime.datetime(2023, 5, 30, 13, 1, 10)
dt3 = dt2 - dt1
print(type(dt3), dt3.total_seconds())

dt1 = datetime.datetime(2023, 5, 30, 8, 0, 0)
delta = datetime.timedelta(hours=5, minutes=1, seconds=10)
dt2 = dt1 - delta
print(dt2)

# formatowanie daty/czasu
now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y %H:%M:%S"))

date_str = "5/3/2023 10:22:33"
dt1 = datetime.datetime.strptime(date_str, "%m/%d/%Y %H:%M:%S")
print(type(dt1), dt1)

print(dateparser.parse('30 maja 2023 14:10'))
print(dateparser.parse('za 2 godz 5 min i 30 sek'))
print(dateparser.parse('za 1 miesiąc'))