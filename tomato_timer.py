# -*- coding:utf-8 -*-
## 番茄工作法的计时器
## 工作15分钟
## 休息3分钟
import os
import sys
import time
import datetime

table = {'work_trigger': 15, 'rest_trigger': 3}

def q1():
	print "Work time(min):"
	while 1:
		work = raw_input()
		try:
			if int(work) > 0:
				table['work_trigger'] = work
				break
			else:
				print "Error! Again."
				q1()
				break
		except:
			print "input must be integer."
			q1()
			break

def q2():
	print "Rest time(min):"
	while 1:
		try:
			rest = raw_input()
			if int(rest) > 0:
				table['rest_trigger'] = rest
				break
			else:
				print "Error! Again."
				q2()
				break
		except:
			print "input must be integer."
			q2()
			break

q1()
q2()

timeA = datetime.datetime.now()
print timeA
