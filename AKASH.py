import os

import time

import sys

from platform import uname

from os import path,system

print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools');time.sleep(2)
    

os.system("xdg-open https://www.facebook.com/akash.404.cyber")

def clear():

  os.system("clear")

  

 

logo=("""

\033[1;32m:::'###::::'##:::'##::::'###:::::'######::'##::::'##:
\033[1;34m::'## ##::: ##::'##::::'## ##:::'##... ##: ##:::: ##:
\033[1;35m:'##:. ##:: ##:'##::::'##:. ##:: ##:::..:: ##:::: ##:
\033[1;34m'##:::. ##: #####::::'##:::. ##:. ######:: #########:
 \033[1;36m#########: ##. ##::: #########::..... ##: ##.... ##:
\033[1;31m ##.... ##: ##:. ##:: ##.... ##:'##::: ##: ##:::: ##:
 \033[1;32m##:::: ##: ##::. ##: ##:::: ##:. ######:: ##:::: ##:
\033[1;32m..:::::..::..::::..::..:::::..:::......:::..:::::..::
\033[1;32m[+]==============================================
\033[1;32m[+] \033[1;33mCREATED BY   :  \033[1;33mHADI ANHAF AIMAN
\033[1;32m[+] \033[1;34mON FACEBOK   :  \033[1;34mHADI ANHAF AIMAN
\033[1;32m[+] \033[1;35mON GITHUB    :  \033[1;35m AKASH-110
\033[1;32m[+] \033[1;36mTOOL STATUS  :  \033[1;36mRANDOM
\033[1;32m[+] \033[1;36mTOOL VIRSION :  \033[1;36m 4G LITE
\033[1;32m[+]==============================================""")

clear()
print(logo)
print("")

print("[1]RAMDOM UID CLONE MIX ID M1")
print("[2]RANDOM UID CLONE MIX ID M2")
print("[3]RANDOM UID CLONE MIX ID M3")
print("[3]EXIT")

xd=input('CHOOSE: ')

if xd in ['1','01']:

    if path.isfile('M1.cpython-311.so'):

        import M1

        

if xd in ['2','02']:

    if path.isfile('M2.cpython-311.so'):

        import M2    

elif xd in ['3','03']:
    if path.isfile('M3.cpython-311.so'):

        import M3    

 

       

        print('\n[•] Checking updates...')

        system('python MIX.py update')
