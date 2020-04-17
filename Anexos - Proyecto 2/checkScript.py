#!/usr/bin/python
import urllib
from urllib.request import urlopen
from datetime import datetime
import sys
import time
import os
from systemd import journal

def internetAvailable():
	try:
		urlopen('https://www.google.com', timeout=5)
		# probar conectividad a google.com
		# se puede usar 'https://api.amazon.com/auth/o2/token' pero para hacerlo mas general usaremos google
		return True
	except urllib.error.URLError as Error:
		# si no hay conectividad, se asume que no hay internet
		print(Error)
		return False

def usbAudioAvailable():
	lines=os.popen('aplay -l').readlines()
	for line in lines:
		if 'card 1: Device [Generic USB Audio Device], device 0: USB Audio [USB Audio]' in line:
			return True
	return False

def usbMicAvailable():
	lines=os.popen('arecord -l').readlines()
	for line in lines:
		if 'card 1: Device [Generic USB Audio Device], device 0: USB Audio [USB Audio]' in line:
			return True
	return False

if __name__ == "__main__":
	internetWasActive=True
	# si no habia internet y ahora sí, tenemos que reinciar el servicio
	audioWasAvailable=True
	# si no estaba el usb, y ahora sí, tenemos que reiniciar el servicio
	
	journal.send('Checking script started at %s\n' % datetime.now())
	#sys.stdout.write('Checking script started at %s\n' % datetime.now())
	while True:
		time.sleep(10)
		# medir cada 10 segundos
		if internetAvailable():
			journal.send(' + [INFO]: Internet is active - %s\n' % datetime.now())
			#sys.stdout.write(" + [INFO]: Internet is active - %s\n" % datetime.now())
			if not internetWasActive:
				os.system('sudo systemctl stop AlexaPi.service && sudo systemctl start AlexaPi.service')
				# detener y reiniciar el proceso, tambien se puede usar restart
			internetWasActive=True
		else:
			journal.send(' - [WARNING]: Internet is NOT active - %s\n' % datetime.now())
			#sys.stdout.write(" - [WARNING]: Internet is NOT active - %s\n" % datetime.now())
			internetWasActive=False
		
		if usbAudioAvailable() and usbMicAvailable():
			journal.send(' + [INFO]: USB Sound card is available - %s\n' % datetime.now())
			if not audioWasAvailable:
				os.system('sudo systemctl stop AlexaPi.service && sudo systemctl start AlexaPi.service')
				# detener y reiniciar el proceso, tambien se puede usar restart
			audioWasAvailable=True
		else:
			journal.send(' - [WARNING]: USB Sound card is NOT available - %s\n' % datetime.now())
			audioWasAvailable=False

