import serial
import time
import requests

#Intenta conectar el puerto serial del arduino en los puertos /dev/tty/USB(0--1)
def conectarArduino():
    try:
        return serial.Serial('/dev/ttyUSB0',9600)
    except:
        try:
            return serial.Serial('/dev/ttyUSB1',9600)
        except:
            try:
                return serial.Serial('/dev/ttyUSB2',9600)
            except:
                try:
                    return serial.Serial('/dev/ttyUSB3',9600)
                except:
                    try:
                        return serial.Serial('/dev/ttyUSB4',9600)
                    except:
                        pass

arduino = conectarArduino()
URL = 'https://gonzalobernard.pythonanywhere.com/update'
while True:
    time.sleep(10)
    try:
        read_serial = arduino.readline()
        if read_serial:
            temp = read_serial[:4]
            hum = read_serial[6:10]
            ph = read_serial[12:15]
            # La fecha es asignada en el servidor
            date = 0
            PARAMS = {'ph':ph , 'temp':temp , 'hum':hum , 'date':date }
            try:
                response = requests.get( url = URL, params = PARAMS,  auth = ('indoor', 'indoor'))
                print(response , " " , ph , " " , temp , " " , hum , " " , date)
            except:
                print("HTTP error de conexion")
    except:
        print("Error en Arduino - Intentando reconectar")
        arduino = conectarArduino()