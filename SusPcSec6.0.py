import time
from time import sleep
import time
from datetime import datetime, timedelta
import pyautogui
import keyboard
import psutil      #Ver nivel de bateria
import datetime

pyautogui.FAILSAFE = False

import sys
def aPrint(string,time_test):
    for i in string :
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(time_test)
    print()
aPrint(f"OJO: La aplicacion va a esta precionanado el shift, cuidado que esto le afecte el programa que esta ejecutando ",time_test=0.01)

sleep(2)


print("Para para de emergencia mantenga precionada la tecla 'control + q' \n")

sleep(0.5)

print("""*Puede escribir un codigo secreto*
Las opciones son las siguientes """)
sleep(0.5)

print("""1. Apagar
2. Suspender
3. Charging""")

off = 0

while True:

    
    opt = str(input("Escriba la opccion: "))


    if opt == "3" : #charging
        dif_hora_1 = datetime.datetime.now()
        hora_inicio = datetime.datetime.now()
        hora_str_in = hora_inicio.strftime('%I:%M:%S %p')
        print("Hora de inicio:", hora_str_in)
        print("Revisa que whatsap esta inciado")
        print("El nuemro va a ser '625' ")


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
            pyautogui.press("shift")
            dif_hora_2 = datetime.datetime.now()
            diferencia = dif_hora_2 - dif_hora_1
            diferencia_horas = diferencia.seconds // 3600
            diferencia_minutos = (diferencia.seconds % 3600) // 60
            diferencia_segundos = diferencia.seconds % 60
            dirent_total = diferencia_horas , diferencia_minutos , diferencia_segundos
            
            fecha_actual = datetime.datetime.now()
            tiempo_objeto = fecha_actual.replace(hour=dirent_total[0], minute=dirent_total[1], second=dirent_total[2])
            dife = tiempo_objeto.strftime("%H:%M:%S")

            hora_actual = datetime.datetime.now()
            hora_str = hora_actual.strftime('%I:%M:%S %p')
            #print("Tienes:",percent,"%","    La bateria:",char,"    La duracion de carga: ",dife,"   Hora de inicio:", hora_str_in, "   Hora actual:", hora_str, )
            print("Tienes:",percent,"%","    La bateria:",char,"    La duracion de carga: ",dife,)

            if percent == 80:
                print("llamar telefono")
                pyautogui.press("win")
                sleep(0.5)
                pyautogui.typewrite("whatsapp")
                sleep(0.5)
                pyautogui.press("enter")
                sleep(2.1)
                pyautogui.typewrite("625")
                sleep(0.5)
                pyautogui.press("tab")
                sleep(0.5)
                pyautogui.press("enter")
                sleep(0.5)
                pyautogui.click(x=1988, y=123)
                sleep(5)

                off = 1
                break
            if keyboard.is_pressed(['ctrl', 'q']):
                off = 1
                break
        break
    



    if opt == "clown": # codigo secreto
            while True:
                print("Entraste como admin")
                if keyboard.is_pressed(['ctrl', 'q']):
                    break
                break 
            off = 1
            sleep(3)
            break 
                # kill this process
            

            


    else:

        if off ==1:
            pass
        else:
            
            if opt.isdigit() and int(opt) >= 4:
                print("El numero no es valido")
                sleep(1)
                off = 1
                break
            else:
                if off ==1:
                    pass
                else:
                    sec = int(input("Escribas los segundos que quiere que el pc espera ante que se accione: "))

                    hora_actual = datetime.datetime.now()
                    hora_str = hora_actual.strftime('%I:%M:%S %p')
                    print("Hora actual:", hora_str)

                    hora_objeto = datetime.datetime.strptime(hora_str, '%I:%M:%S %p')
                    nueva_hora_objeto = hora_objeto + timedelta(seconds=sec)
                    hora_de_suspencion = nueva_hora_objeto.strftime('%I:%M:%S %p')
                    print("Hora de suspencion:", hora_de_suspencion)

                    time.sleep(0.5)
                    break

if off ==1:
    pass
else:

    dif_hora_1 = datetime.datetime.now()

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

        if keyboard.is_pressed(['ctrl', 'q']):
            break

        hora_actual = datetime.datetime.now()
        hora_str = hora_actual.strftime('%I:%M:%S %p')

       #############################


        print("Tiempo actual: ",hora_str,"        ", "Tiempo de ejecucion: ",hora_de_suspencion, "     Tiempo Restante: ",dife)

        


        if hora_str == hora_de_suspencion:

            if opt == "1": # Apagar
            
                if keyboard.is_pressed(['ctrl', 'q']):
                    break

                aPrint(f"llego el momento para Apagarse ",time_test=0.15)
                if keyboard.is_pressed(['ctrl', 'q']):
                    break
                pyautogui.hotkey('win','d')
                if keyboard.is_pressed(['ctrl', 'q']):
                    break
                time.sleep(0.9)
                pyautogui.hotkey('alt','f4')
                if keyboard.is_pressed(['ctrl', 'q']):
                    break
                time.sleep(1)
                if keyboard.is_pressed(['ctrl', 'q']):
                    break
                if keyboard.is_pressed(['ctrl', 'q']):
                    break
                pyautogui.press('enter')

                break


            if opt == "2": # Suspender
            
                if keyboard.is_pressed(['ctrl', 'q']):
                    break

                aPrint(f"llego el momento para suspenderse ",time_test=0.15)
                if keyboard.is_pressed(['ctrl', 'q']):
                    break
                pyautogui.hotkey('win','d')
                if keyboard.is_pressed(['ctrl', 'q']):
                    break
                time.sleep(0.9)
                pyautogui.hotkey('alt','f4')
                if keyboard.is_pressed(['ctrl', 'q']):
                    break
                time.sleep(1)
                pyautogui.press('up')
                if keyboard.is_pressed(['ctrl', 'q']):
                    break
                time.sleep(1)
                if keyboard.is_pressed(['ctrl', 'q']):
                    break
                pyautogui.press('enter')

                break


        else:
            pyautogui.press("shift")
            
