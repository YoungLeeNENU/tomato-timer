# -*- coding:utf-8 -*-
## 番茄工作法的计时器
import sys
import threading
import gtk, pygtk
import pyaudio, wave
from time import sleep
from Tkinter import *

table = {'work_trigger': 15, 'rest_trigger': 3}
work_str = 'Work time(min):'
rest_str = 'Rest time(min):'
work_notice = 'Go to Rest!'
rest_notice = 'Back to work!'

def question(hello_str, trigger):
	while 1:
		buf = raw_input(hello_str)
		try:
			if int(buf) > 0:
				table[trigger] = buf
				break
			else:
				print "Error! Again."
				question(hello_str, trigger)
				break
		except:
			print "input must be integer."
			question(hello_str, trigger)
			break

def play_audio(wav_file):
	wf = wave.open(wav_file, 'rb')
	p = pyaudio.PyAudio()
	stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
					channels = wf.getnchannels(),
					rate = wf.getframerate(),
					output = True)
	data = wf.readframes(2048)
	while data != '':
		stream.write(data)
		data = wf.readframes(2048)
	stream.stop_stream()
	stream.close()
	p.terminate()

def createWindow(notice):
	play_audio("./sounds/Old Phone.wav")
	window = gtk.Window()
	window.set_default_size(300, 300)
	window.connect('destroy', gtk.main_quit)
	label = gtk.Label(notice)
	window.add(label)
	label.show()
	window.show()

if __name__ == '__main__':
	question(work_str, 'work_trigger')
	question(rest_str, 'rest_trigger')
	work_sec, rest_sec = int(table['work_trigger']) * 60, int(table['rest_trigger']) * 60

	print "Running..."

	def loop(loop_type, notice_type):
		while 1:
			loop_type = loop_type - 1
			sleep(1)
			if loop_type <= 0:
				createWindow(notice_type)
				gtk.main()
				break

	while 1:
		loop(work_sec, work_notice)
		loop(rest_sec, rest_notice)

		work_sec, rest_sec = int(table['work_trigger']) * 60, int(table['rest_trigger']) * 60
