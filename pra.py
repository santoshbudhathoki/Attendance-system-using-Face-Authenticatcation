# with open('users.txt') as f:
#     data = f.read()
#     print(data)
# if os.path.exists("sample.txt"):
# os.remove("sample.txt")

import datetime

e = datetime.datetime.now()
date = "%s/%s/%s" % (e.day, e.month, e.year)
print(date)
# print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
print ("Current date and time = %s" % e)
print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))
time = "%s:%s:%s" % (e.hour, e.minute, e.second)
print(time)