from collections.abc import Iterable
import re

def parse(time:str):
	
	num_time = time
	period = None
	
	if match := re.search(r'am|pm',time):
		period = match.group()
		num_time = time[0:match.start()]
	else:
		num_time = time

	hours = num_time
	minutes = 0
	
	if ":" in num_time:
		hours,minutes = re.split(r":",num_time)
		minutes = int(minutes)

	hours = int(hours)

	if period:
		hours %= 12

	if period == "pm":
		hours += 12

	minutes_past_midnight = hours * 60 + minutes

	return minutes_past_midnight

if __name__ == "__main__":
	times = ("4pm","7:38pm","23:42","3:16","3:16am","5:00","5:00pm")
	for t in times:
		print(f"{t} --> {parse(t)}")
