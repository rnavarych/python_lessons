import datetime
import time

print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)

print(datetime.date.isoformat(datetime.date.today()))
print('-------------------------------------------------')

print(time.strftime("%I:%M"))
print(time.strftime("%A %p"))
