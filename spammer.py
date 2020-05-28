#Copyright © 2020 - Rodrigo de Lorenzo
from pynput.keyboard import Key, Controller
import time
import urllib.request
import itertools

keyboard = Controller()

f = urllib.request.urlopen("https://gist.githubusercontent.com/ttt5600/f6d7b07d602e192ae809115d62cb7d5f/raw/7eaad360a218644f35156e4dfd0bd31f405a148b/gistfile1.txt")
script = f.read()

scriptlines = script.decode().splitlines()

lines = []
for line in scriptlines:
	lines.append(line.split())

lines = itertools.chain.from_iterable(lines)

time.sleep(3)

for line in lines:
	for char in line:
		keyboard.press(char)
		keyboard.release(char)
		#Sleep might be necessary for cetain applications
		#time.sleep(0.03)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	time.sleep(.5)
