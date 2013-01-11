# -*- coding:utf-8 -*-
## 番茄工作法的计时器
## 默认工作15分钟
## 默认休息3分钟
import sys
import gtk
import time
import pygtk
import datetime

def createWindow_work():
        window = gtk.Window()
        window.set_default_size(300, 300)
        window.connect('destroy', gtk.main_quit)

        label = gtk.Label('Go to Rest!')
        window.add(label)

        label.show()
        window.show()

def createWindow_rest():
        window = gtk.Window()
        window.set_default_size(300, 300)
        window.connect('destroy', gtk.main_quit)

        label = gtk.Label('Back to work!')
        window.add(label)

        label.show()
        window.show()

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
		rest = raw_input()
		try:
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

work_sec = int(table['work_trigger']) * 60
rest_sec = int(table['rest_trigger']) * 60

while 1:
	while 1:
		work_sec = work_sec - 1
		time.sleep(1)
		if work_sec <= 0:
			createWindow_work()
			gtk.main()
			break

	while 1:
		rest_sec = rest_sec - 1
		time.sleep(1)
		if rest_sec <= 0:
			createWindow_rest()
			gtk.main()
			break

	work_sec = int(table['work_trigger']) * 60
	rest_sec = int(table['rest_trigger']) * 60
