import network #
import BlynkLib #
from dcmotor import DCMotor #
from machine import Pin, PWM #
from servo import Servo #
from time import sleep #

# --- NETWORK SETUP ---
ssid = 'TU_NOMBRE_DE_RED' #
password = 'TU_CONTRASEÑA' #
red = network.WLAN(network.STA_IF) #
red.active(True) #
red.connect(ssid, password) #

while red.isconnected() == False: #
    pass #

print('Conexión correcta') #

# --- BLYNK SETUP ---
BLYNK_AUTH = 'TU_TOKEN_DE_BLYNK' #
blynk = BlynkLib.Blynk(BLYNK_AUTH) #

# --- HARDWARE INITIALIZATION ---
# (Ajusta los números de los pines según tus conexiones físicas)
Sensor = Pin(15, Pin.IN)  # Ejemplo de pin para el sensor IR

# Motores DC (L298N)
# dc_motor1 = DCMotor(...) 
# dc_motor2 = DCMotor(...)

# Servomotores
# Gancho = Servo(...) 
# Codo = Servo(...)

# --- BLYNK IOT CONTROL (MOVEMENT) ---
@blynk.on("V0") #
def up(bot0): #
    if int(bot0[0]) == 1: #
        dc_motor1.forward(40) #
        dc_motor2.forward(40) #
    else: #
        dc_motor1.stop() #
        dc_motor2.stop() #

# (Aquí agregarías las funciones para down, left, right en V1, V2, V3)

# --- MAIN LOOP (ROBOTIC ARM LOGIC) ---
contador = 0

while True: #
    blynk.run() #
    valSensor = Sensor.value() #
    
    if valSensor == 1: # No detecta nada
        # Mantiene las posiciones del gancho
        if angGancho == 60: #
            Gancho.move(angGancho) #
            sleep(1) #
            angCodo = 0 #
            Codo.move(angCodo) #
        else: #
            angGancho = 0 #
            Gancho.move(angGancho) #
            sleep(1) #
            
    else: # Detecta objeto
        if contador == 0: # Primera situación: Cierra gancho y sube brazo
            angGancho = 0 #
            Gancho.move(angGancho) #
            contador = 1 #
            sleep(1) #
            angCodo = 45 #
            Codo.move(angCodo) #
            
        else: # Segunda situación: Abre gancho y baja brazo
            angGancho = 60 #
            Gancho.move(angGancho) #
            contador = 0 #
            sleep(1) #
            angCodo = 45 #
            
            # Evita que el brazo baje con mucha fuerza
            for a in range(angCodo, 0, -1): #
                Codo.move(a) #
                sleep(0.01) #
