#!/usr/bin/env python
#-- coding: utf-8 --

from enum import Enum, unique

Month = Enum('Months', ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'))

print(type(Month))

for key, v in Month.__members__.items():
	print("%s->%s, %d" % (key, v, v.value))



@unique
class WeekDay(Enum):
	MONDAY = 1
	TUESDAY = 2
	WEDNESDAY = 3
	THUSDAY = 4
	FRIDAY = 5
	SATURDAY = 6
	SUNDAY = 7

day1 = WeekDay.MONDAY

print(WeekDay.TUESDAY)
print(day1 == WeekDay.MONDAY)
print(WeekDay(3))
print(day1 == WeekDay(1))
print(WeekDay.FRIDAY.value)

