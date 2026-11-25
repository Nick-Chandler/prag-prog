from collections.abc import Iterable
import re

def parse(time:str) ->tuple[str,str,str]:

	time_no_per,per = (time,None)
	
	per_search = re.search(r"am|pm",time)

	if per_search:
		time_no_per,per = (time[0:per_search.start()],per_search.group())
	
	min_search = re.search(r":",time_no_per)
	
	if min_search:
		h, m = time_no_per.split(":")
		m = m
	else:
		h = time_no_per
		m = "00"

	if per:
		return (str(h),str(m),per)

	# 24 hour time
	hour_24 = int(h) // 12

	if hour_24:
		return (str(int(h)%12), m, "pm")
		
	return (str(h), m, "am")

def output_time(time:str,h:str,m:str,per:str):
	print(f"Input: {time}")
	print(f"Hour: {h}")
	print(f"Minutes: {m}")
	print(f"Period: {per}")
	print(f"Formatted: {h}:{m}{per}\n")

def parse_times(times:Iterable):
	for time_input in times:
		h,m,per = parse(time_input)
		output_time(time_input,h,m,per)

if __name__ == "__main__":
	times = ("4pm","7:38pm","23:42","3:16","3:16am","5:00","5:00pm")
	parse_times(times)
