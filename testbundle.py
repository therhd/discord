import datetime

trigger_times = [9, 12, 14, 16]

while True:

now = datetime.datetime.now()
next_t = None
for time in trigger_times:
    if time > now.hour:
        next_t = datetime.datetime(year=now.year, month=now.month, 
                        day=now.day, hour=time, minute=0, second=0)
        break
if next_t == None:
    tomorrow = datetime.timedelta(1) + now
    next_t = datetime.datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day, hour=trigger_times[0], minute=0, second=0)
sleep_time = (next_t - now).seconds
print(now)
print(next_t)
print(sleep_time)