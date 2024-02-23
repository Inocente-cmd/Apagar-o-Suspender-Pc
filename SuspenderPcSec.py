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
aPrint(f"OJO: La aplicacion va a esta precionanado el shift, cuidado que esto le afecte el programa que esta ejecutando ",time_test=0.10)

print("Para para de emergencia precione la 'Q' muchas veces")

sec = int(input("Escribas los segundos que quiere que el pc espera ante de suspenderse: "))

hora_actual = datetime.now()
hora_str = hora_actual.strftime('%I:%M:%S %p')
print("Hora actual:", hora_str)

hora_objeto = datetime.strptime(hora_str, '%I:%M:%S %p')
nueva_hora_objeto = hora_objeto + timedelta(seconds=sec)
hora_de_suspencion = nueva_hora_objeto.strftime('%I:%M:%S %p')
print("Hora de suspencion:", hora_de_suspencion)
time.sleep(0.5)


while True:
    
    if keyboard.is_pressed('q'):
        break

    hora_actual = datetime.now()
    hora_str = hora_actual.strftime('%I:%M:%S %p')

    print(hora_str, hora_de_suspencion)

    if keyboard.is_pressed('q'):
        break

    if hora_str == hora_de_suspencion:
        
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
        
