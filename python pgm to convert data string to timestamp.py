import time
import datetime

string = "20/01/2021"
print(time.mktime(datetime.datetime.strptime(string, "%d/%m/%y").timetuple()))
