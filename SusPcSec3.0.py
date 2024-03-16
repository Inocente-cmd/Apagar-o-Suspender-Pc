import time
from time import sleep
import time
from datetime import datetime, timedelta
import pyautogui
import keyboard

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

print("Para para de emergencia mantenga precionada la tecla 'Q' \n")

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
        hora_inicio = datetime.now()
        hora_str_in = hora_inicio.strftime('%I:%M:%S %p')
        print("Hora de inicio:", hora_str_in)
        while True:
            pyautogui.press("shift")
            hora_actual = datetime.now()
            hora_str = hora_actual.strftime('%I:%M:%S %p')
            print("Hora de inicio:", hora_str_in, "        Hora actual:", hora_str,)
            if keyboard.is_pressed('q'):
                off = 1
                break
        break
    



    if opt == "perra": # codigo secreto
            while True:
                print("Entraste como admin")
                if keyboard.is_pressed('q'):
                    break
                break 
            off = 1
            break 
                # kill this process
            

            


    else:

        if off ==1:
            print("")
        else:

            sec = int(input("Escribas los segundos que quiere que el pc espera ante que se accione: "))

            hora_actual = datetime.now()
            hora_str = hora_actual.strftime('%I:%M:%S %p')
            print("Hora actual:", hora_str)

            hora_objeto = datetime.strptime(hora_str, '%I:%M:%S %p')
            nueva_hora_objeto = hora_objeto + timedelta(seconds=sec)
            hora_de_suspencion = nueva_hora_objeto.strftime('%I:%M:%S %p')
            print("Hora de suspencion:", hora_de_suspencion)
            time.sleep(0.5)
            break

if off ==1:
    print("")
else:

    while True:
        
    

        if keyboard.is_pressed('q'):
            break

        hora_actual = datetime.now()
        hora_str = hora_actual.strftime('%I:%M:%S %p')

        print(hora_str, hora_de_suspencion)

        if keyboard.is_pressed('q'):
            break


        if hora_str == hora_de_suspencion:

            if opt == "1": # Apagar
            
                if keyboard.is_pressed('q'):
                    break

                aPrint(f"llego el momento para Apagarse ",time_test=0.15)
                if keyboard.is_pressed('q'):
                    break
                pyautogui.hotkey('win','d')
                if keyboard.is_pressed('q'):
                    break
                time.sleep(0.9)
                pyautogui.hotkey('alt','f4')
                if keyboard.is_pressed('q'):
                    break
                time.sleep(1)
                if keyboard.is_pressed('q'):
                    break
                if keyboard.is_pressed('q'):
                    break
                pyautogui.press('enter')

                break


            if opt == "2": # Suspender
            
                if keyboard.is_pressed('q'):
                    break

                aPrint(f"llego el momento para suspenderse ",time_test=0.15)
                if keyboard.is_pressed('q'):
                    break
                pyautogui.hotkey('win','d')
                if keyboard.is_pressed('q'):
                    break
                time.sleep(0.9)
                pyautogui.hotkey('alt','f4')
                if keyboard.is_pressed('q'):
                    break
                time.sleep(1)
                pyautogui.press('up')
                if keyboard.is_pressed('q'):
                    break
                time.sleep(1)
                if keyboard.is_pressed('q'):
                    break
                pyautogui.press('enter')

                break


        else:
            pyautogui.press("shift")
            
