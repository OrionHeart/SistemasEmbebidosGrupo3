import os
import glob
import time
import csv
from datetime import datetime

def lineasTemperatura():
	f = open(archivoSensor,'r')
	lines = f.readlines()
	f.close()
	return lines
	
if __name__ == '__main__':
	# Habilitar la lectura de datos por el puerto de one-wire:
	os.system('modprobe w1-gpio')
	os.system('modprobe w1-therm')
	
	# El folder del dispositivo y la ruta del archivo a leer:
	carpetaSensor = glob.glob('/sys/bus/w1/devices/' + '28*')[0]
	archivoSensor = carpetaSensor + '/w1_slave'
	
	# Se crea el archivo de salida:
	nombrearchivito = datetime.today().strftime('%Y%m%d') + '_TEMPERATURA.csv'

	antes = time.time()-9
	with open(nombrearchivito,mode='w') as tempFile:
		tempWriter = csv.writer(tempFile, delimiter=',');
		
		# Mientras el codigo este corriendo:	
		while 1:
			# Se abre el archivo del sensor, se lee en la variable 'lines' y se cierra:
			lines = lineasTemperatura()
			
			# Mientras que en la primera linea, los ultimos 3 caracteres no sean 'YES', 
			# espera 0.2s y lee otra vez, el sensor aun no esta transmitiendo data
			while lines[0].strip()[-3:] != 'YES':
				time.sleep(0.2)
				lines = lineasTemperatura()
			
			# Posicion de la data temperatura en la segunda linea del archivo 't=xxxxx'
			tempPos = lines[1].find('t=')

			# Si encontro algo
			if tempPos != -1:
				# Calculo de la temp omitiendo el 't=' y haciendolo en float
				temp = float(lines[1][tempPos+2:])/1000.0
				# Escribir al archivo la data de temp en formato "AAAAMMDD HHMMSS, temp"
				while int(time.time()-antes) <= 10:
					pass # Do nothing, just wait				
				tempWriter.writerow([datetime.today().strftime('%Y%m%d %H%M%S'), str(temp)])
				antes=time.time()				
				time.sleep(9) # Esperar 10s
	


	

