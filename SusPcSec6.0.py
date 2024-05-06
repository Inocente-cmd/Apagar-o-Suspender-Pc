import time
from datetime import datetime, timedelta
import pyautogui
import keyboard
import psutil      #Ver nivel de bateria
import datetime
import subprocess
import pygame
import pyttsx3
import ctypes

pyautogui.FAILSAFE = False

import sys
def aPrint(string,time_test):
    for i in string :
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(time_test)
    print()

aPrint(f"OJO: La aplicacion va a esta precionanado el shift, cuidado que esto le afecte el programa que esta ejecutando ",time_test=0.01)

print("Para para de emergencia mantenga precionada la tecla 'control + e' \n")
print("""*Puede escribir un codigo secreto*
Las opciones son las siguientes """)


print("""1. Apagar
2. Suspender
3. Charging""")

off = 0
elec = 0

def musicquita(fa):
    pass
    archivo_audio = "C:\Windows\Media\Alarm09.wav"
    pygame.mixer.init()
    pygame.mixer.music.load(archivo_audio)
    pygame.mixer.music.play()
    time.sleep(4)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    #time.sleep(1.7)

def texto_a_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def hour():
    sec = 55
    Tiempo_antiguo = datetime.datetime.now()
    Tiempo_antiguo2 = Tiempo_antiguo.strftime('%I:%M:%S')
    hora_objeto = datetime.datetime.strptime(Tiempo_antiguo2, '%I:%M:%S')
    nueva_hora_objeto = hora_objeto + timedelta(seconds=sec)
    hora_de_accion = nueva_hora_objeto.strftime('%I:%M:%S')
    return hora_de_accion

def valorcito(valores):
    print("Probando audio...")
    musicquita("messi")
    sec = int(input("Escribas los segundos que quiere que el pc espera ante que se accione: "))
    hora_actual = datetime.datetime.now()
    hora_str = hora_actual.strftime('%I:%M:%S %p')
    #print("Hora actual:", hora_str)
    hora_objeto = datetime.datetime.strptime(hora_str, '%I:%M:%S %p')
    nueva_hora_objeto = hora_objeto + timedelta(seconds=sec)
    hora_de_accion = nueva_hora_objeto.strftime('%I:%M:%S %p')
    #print("Hora de Accion:", hora_de_accion)

    dif_hora_1 = datetime.datetime.now()
    pais = hour()
    while True: 

        dif_hora_2 = datetime.datetime.now()
        diferencia = nueva_hora_objeto - hora_actual
        diferencia_horas = diferencia.seconds // 3600
        diferencia_minutos = (diferencia.seconds % 3600) // 60
        diferencia_segundos = diferencia.seconds % 60
        dirent_total = diferencia_horas , diferencia_minutos , diferencia_segundos
        fecha_actual = datetime.datetime.now()
        tiempo_objeto = fecha_actual.replace(hour=dirent_total[0], minute=dirent_total[1], second=dirent_total[2])
        dife = tiempo_objeto.strftime("%H:%M:%S")
        hora_actual = datetime.datetime.now()
        hora_str = hora_actual.strftime('%I:%M:%S %p')
        time_actial = datetime.datetime.now()
        time_actial2 = time_actial.strftime('%I:%M:%S') 
        
        if time_actial2 == pais:
            ctypes.windll.user32.keybd_event(0x87, 0, 0, 0)
            ctypes.windll.user32.keybd_event(0x87, 0, 2, 0)
            print("Boton precionado")
            time.sleep(1)
            pais = hour()

        print("Tiempo actual: ",hora_str,"        ", "Tiempo de ejecucion: ",hora_de_accion, "     Tiempo Restante: ",dife)

        if keyboard.is_pressed(['ctrl', 'e']):
            break
        
        if hora_str == hora_de_accion:
            if valores == 1:
                if keyboard.is_pressed(['ctrl', 'e']):
                    break
                print("Se va a apagarse")
                musicquita("messi")
                subprocess.run(["shutdown", "/s", "/t", "10"])  
                break

            if valores == 2:
                print("Se va a suspender") #rundll32.exe powrprof.dll, SetSuspendState 
                musicquita("messi")
                subprocess.run(["rundll32.exe", "powrprof.dll", "SetSuspendState"])
                break
                
        else:
            pass

opt = str(input("Escriba la opccion: "))

if opt == "3" : #charging
    print("Probando audio...")
    musicquita("messi")
    dif_hora_1 = datetime.datetime.now()
    hora_inicio = datetime.datetime.now()
    hora_str_in = hora_inicio.strftime('%I:%M:%S %p')
    print("Hora de inicio:", hora_str_in)
    pais = hour()
    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        charging = battery.power_plugged
        """
        if charging:
            print(f"Batería: {percent}% (Cargando)")
        else:
            print(f"Batería: {percent}% (No está cargando)")
        """
        char = False
        if charging == False:
            char = "No esta cargando"
        if charging == True:
            char = "Esta cargando"
        
        dif_hora_2 = datetime.datetime.now()
        diferencia = dif_hora_2 - dif_hora_1
        diferencia_horas = diferencia.seconds // 3600
        diferencia_minutos = (diferencia.seconds % 3600) // 60
        diferencia_segundos = diferencia.seconds % 60
        dirent_total = diferencia_horas , diferencia_minutos , diferencia_segundos

        if keyboard.is_pressed(['ctrl', 'e']):
            break

        fecha_actual = datetime.datetime.now()
        tiempo_objeto = fecha_actual.replace(hour=dirent_total[0], minute=dirent_total[1], second=dirent_total[2])
        dife = tiempo_objeto.strftime("%H:%M:%S")
        hora_actual = datetime.datetime.now()
        hora_str = hora_actual.strftime('%I:%M:%S %p')
        #print("Tienes:",percent,"%","    La bateria:",char,"    La duracion de carga: ",dife,"   Hora de inicio:", hora_str_in, "   Hora actual:", hora_str, )
        print("Tienes:",percent,"%","    La bateria:",char,"    La duracion de carga: ",dife,)
        hora_actual = datetime.datetime.now()
        hora_str = hora_actual.strftime('%I:%M:%S %p')
        time_actial = datetime.datetime.now()
        time_actial2 = time_actial.strftime('%I:%M:%S') # Simepr acitalizandose
        if time_actial2 == pais:
            ctypes.windll.user32.keybd_event(0x87, 0, 0, 0)
            ctypes.windll.user32.keybd_event(0x87, 0, 2, 0)
            print("Boton precionado")
            time.sleep(1)
            pais = hour()


        if percent == 80:
            texto = "The Battery is fully charged"
            texto2 = "Please disconect the charger"
            #texto = "The bluethood devise is ready to pair, The bluethood devise is conected sucessfully"
            while True:
                texto_a_voz(texto)
                if keyboard.is_pressed(['ctrl', 'e']):
                    break
                texto_a_voz(texto2)
                if keyboard.is_pressed(['ctrl', 'e']):
                    break
                musicquita("messi")
                if keyboard.is_pressed(['ctrl', 'e']):
                    break
        else:
            pass         
    
elif opt.isdigit() and int(opt) == 1:
    valorcito(1)
    
elif opt.isdigit() and int(opt) == 2:
    valorcito(2)

elif opt == "clown": # codigo secreto
        #while True:
        print("Entraste como admin")
        #    if keyboard.is_pressed(['ctrl', 'e']):
        #        break
        off = 1
        time.sleep(3)
         
            # kill this process

elif opt.isdigit() and int(opt) >= 4:
    print("Ese numero no es valido")
    time.sleep(2)

else:
    print("Esa palabra no es el codigo secreto")
    time.sleep(2)

# Probar Clown 
#        1
#        2
#        3
#        4
#        32 
#        100
#        w           

            
