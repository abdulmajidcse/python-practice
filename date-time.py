from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

print(today)

date1 = datetime(2024, 11, 2)
date2 = datetime(2020, 10, 15)

diff = date1 - date2

print(diff.days)

import calendar

print(calendar.TextCalendar().formatyear(2024))