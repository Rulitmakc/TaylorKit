from pystyle import Colors
import subprocess
import os
import asyncio
import aiohttp
import socket
import random
import time
from pystyle import Colors, Colorate
import subprocess
import requests
from bs4 import BeautifulSoup
from pystyle import *
import socket
import os
import csv
import time
import subprocess
import phonenumbers
from ipwhois import IPWhois
import pystyle
import telebot
from telebot import types
import csv
import time
import json
from phonenumbers import geocoder, carrier, timezone
import ctypes
from ctypes import wintypes
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import termcolor
from termcolor import colored
from pystyle import Colors, Colorate
import subprocess
from pystyle import Colorate, Colors, Center
import os
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests
import webbrowser
import urllib.parse
import platform

def lookup_phone(phone):
    try:
        parsed_number = phonenumbers.parse(phone)
        location = geocoder.description_for_number(parsed_number, "ru")
        operator = carrier.name_for_number(parsed_number, "ru")
        time_zones = timezone.time_zones_for_number(parsed_number)
        
        print(Colorate.Horizontal(Colors.blue_to_red, "\n Информация о номере:"))
        print(Colorate.Horizontal(Colors.blue_to_red, f" Страна: {location}"))
        print(Colorate.Horizontal(Colors.blue_to_red, f"  Оператор: {operator}"))
        
        filtered_zones = []
        if location == "Russia":
            filtered_zones = [tz for tz in time_zones if "Asia" in tz or "Europe" in tz]
            filtered_zones.sort()
        else:
            filtered_zones = time_zones
            
        print(Colorate.Horizontal(Colors.blue_to_cyan, f" Часовой пояс: {', '.join(filtered_zones)}"))

        try:
            response = requests.get(f"https://nominatim.openstreetmap.org/search?country={location}&format=json")
            if response.status_code == 200:
                data = response.json()
                if data:
                    lat = data[0]['lat']
                    lon = data[0]['lon']
                    print(Colorate.Horizontal(Colors.blue_to_red, f"└─▶ Примерные координаты: {lat}, {lon}"))
        except:
            pass
        
        print(Colorate.Horizontal(Colors.blue_to_red, "\n Возможные ссылки на соцсети:"))
        print(Colorate.Horizontal(Colors.blue_to_red, f"  WhatsApp: https://wa.me/{phone.replace('+', '')}"))
        print(Colorate.Horizontal(Colors.blue_to_red, f" Telegram: https://t.me/+{phone.replace('+', '')}"))
        print(Colorate.Horizontal(Colors.blue_to_red, f" Viber: viber://chat?number={phone.replace('+', '')}"))
            
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_yellow, f"\n Ошибка поиска информации: {str(e)}"))
        print(Colorate.Horizontal(Colors.red_to_yellow, " Проверьте формат номера телефона"))


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

Intro = """

████████╗░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░  
╚══██╔══╝██╔══██╗╚██╗░██╔╝██║░░░░░██╔══██╗██╔══██╗  
░░░██║░░░███████║░╚████╔╝░██║░░░░░██║░░██║██████╔╝  
░░░██║░░░██╔══██║░░╚██╔╝░░██║░░░░░██║░░██║██╔══██╗  
░░░██║░░░██║░░██║░░░██║░░░███████╗╚█████╔╝██║░░██║  
░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝  

██╗░░██╗██╗████████╗
██║░██╔╝██║╚══██╔══╝
█████═╝░██║░░░██║░░░
██╔═██╗░██║░░░██║░░░
██║░╚██╗██║░░░██║░░░
╚═╝░░╚═╝╚═╝░░░╚═╝░░░                                                                    

                
Welcome to Taylor kit! Press "Enter" to continue.
"""

Anime.Fade(Center.Center(Intro), Colors.blue_to_red,Colorate.Vertical, interval=0.010, enter=True)

def show_banner():
    banner = """
    
            ████████╗░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░  
            ╚══██╔══╝██╔══██╗╚██╗░██╔╝██║░░░░░██╔══██╗██╔══██╗  
            ░░░██║░░░███████║░╚████╔╝░██║░░░░░██║░░██║██████╔╝  
            ░░░██║░░░██╔══██║░░╚██╔╝░░██║░░░░░██║░░██║██╔══██╗  
            ░░░██║░░░██║░░██║░░░██║░░░███████╗╚█████╔╝██║░░██║  
            ░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝  

                        ██╗░░██╗██╗████████╗
                        ██║░██╔╝██║╚══██╔══╝
                        █████═╝░██║░░░██║░░░
                        ██╔═██╗░██║░░░██║░░░
                        ██║░╚██╗██║░░░██║░░░
                        ╚═╝░░╚═╝╚═╝░░░╚═╝░░░

    ╔═══════════════════════════════════════════════════════════════════════╗
    ║################## https://t.me/+w3jbAuqfNzM1MDQy #####################║
    ║#                                                                     #║
    ║#           (1):ддос                      (2):поиск по бд             #║
    ║#                                                                     #║
    ║#        (3):флуд кодами                 (4):поиск по сайту           #║
    ║#                                                                     #║
    ║#        (5):инфа номера                    (6):сносер                #║
    ║#                                                                     #║
    ║#           (7):утечки                     (8):троллинг               #║
    ║#                                                                     #║
    ║#                           (99):выход                                #║
    ║#                                                                     #║
    ╚═══════════════════════════════════════════════════════════════════════╝
    """
    print(Colorate.Vertical(Colors.blue_to_red, banner))

def main_menu():
    while True:
        clear_console()
        show_banner()

        choice = input(Colorate.Horizontal(Colors.red_to_blue, "\nВыбирай: "))

        if choice == "1":
            subprocess.run(['python','1.py'])

        elif choice == "2":
            subprocess.run(['python','2.py'])

        elif choice == "3":
            subprocess.run(['python','3.py'])

        elif choice == "4":
            subprocess.run(['python','4.py'])

        elif choice == "5":
            print(Colorate.Horizontal(Colors.blue_to_red, """
╭────────────────────────╮
(    ПОИСК ПО НОМЕРУ     )
╰────────────────────────╯"""))
            
            phone = input(Colorate.Horizontal(Colors.blue_to_green, "\n[#] Введите номер телефона (например +79991234567): "))
            lookup_phone(phone)
            input(Colorate.Horizontal(Colors.blue_to_green, "\n[#] тап энтер чтоб продолжить"))

        elif choice == "6":
            subprocess.run(['python','6.py'])

        elif choice == "7":
            subprocess.run(['python','7.py'])

        elif choice == "8":
            choice = input("выбери 1.2")       
            if choice == "1":
                print("АЛО БЛЯТЬ ПАРОДИЯ НА ЧЕЛОВЕКА ТВОЕЙ МАТЕРИ Я В РОТ КОНЧАЛ А ПОТОМ ЕЙ БЛЯТЬ ЕБЛАНИК ПРОСТРЕЛИЛ ЗА ТО ЧТО ПРОРОНИЛА КАПЛЮ МОЕЙ ДРАГОЦЕННОЙ СПЕРМЫ БЛЯТЬ ЕЩЕ РАВЗ ТЫ СКАЖЕШЬ ХОТЬ СЛОВО ПРОТИВ МЕНГЯ БЛЯТЬ Я ПРОСТРЕЛЮ КОЛЕНИ ВСЕЙ ТВОЕЙ СЕМЬЕ ТЫ ПОНЯЛ МЕНЯ БЛЯТЬ УЕБИЩЕ НИЧТОЖНОЕК")
                vs = input("энтер для выхода")
                if vs == "99":
                    main_menu()
                else:
                    main_menu()

            elif choice == "2":
                print("СУКА ЕБАНОЕ ХУЕСОСИЩЕ ЗАКТРОЙ ЕБЛЕТ ПИДОРАСНИНА КАК ТВОРЯ МАМКА ПОСЛЕ ТОГО КАК СДЕЛАЛА МНЕ МИНЕТ И ОН БЫЛ ХУЙНЯ ПОЭТОМУ ЕЙ Я ПРОСТРУЛИЛ ЕБЛЕТ НАХЙУ И РОТ ОНА НЕ ОТКРЫВАЛА ПОСЛЕ ЭТОГО ПОЭТОМУК ПОСЛЕДУЙ ПРИМЕРУ СВОЕЙ МАМААШИ И НЕ ЗАСТАВЛЯЙ МЕНЯ ДЕЛАТЬ ТЕБЕ ТАКЖЕ КААК И ТВОЕЙ МАМКЕ")
                vsx = input(" энетер для выхода")
                if vsx == "99":
                    main_menu()
                else:
                    main_menu()
            else:
                main_menu()
        elif choice == "99":
            subprocess.run(['python','99.py'])
            break

        else:
            print(Colorate.Horizontal(Colors.red, "\nНеверный выбор"))
            time.sleep(2)

if __name__ == "__main__":
    main_menu()