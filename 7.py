
import os
import sys
import time
import ctypes
import socket
import json
import base64
import random
import webbrowser
import threading
import subprocess
import re
from datetime import datetime, timedelta
from requests.exceptions import RequestException
import requests
from bs4 import BeautifulSoup
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import whois
import colorama
from colorama import Fore, init
from pystyle import Anime, Colors, Colorate, Center
import termcolor
from termcolor import colored
from pystyle import Write, Colors

os.system('cls' if os.name == 'nt' else 'clear')



main = """
████████╗░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░
╚══██╔══╝██╔══██╗╚██╗░██╔╝██║░░░░░██╔══██╗██╔══██╗
░░░██║░░░███████║░╚████╔╝░██║░░░░░██║░░██║██████╔╝
░░░██║░░░██╔══██║░░╚██╔╝░░██║░░░░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║░░░██║░░░███████╗╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝


░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
                        
     ╔══════════════════════════════════════╗
     ║                                      ║
     ║          (1):поиск утечек            ║
     ║                                      ║
     ║            (99):выйти                ║
     ║                                      ║
     ╚══════════════════════════════════════╝
"""
print(Colorate.Vertical(Colors.blue_to_red, main))


USERSBOX_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkX2F0IjoxNzI1MTk2NzMwLCJhcHBfaWQiOjE3MjUxOTY3MzB9.qG_GQCdZqvUHSHd0yGpnPiUGKo-KRsgNnMo8ZDpRItg"

def search_by_number():
    phone = input(Colorate.Vertical(Colors.blue_to_red, "\nВведите Запрос: "))
    
    try:
        response = requests.get(f"https://api.proxynova.com/comb?query={phone[-11:]}&start=0&limit=100", allow_redirects=False)
        response.raise_for_status()
        lines = response.json().get("lines", [])
        for line in lines:
            print(f"Result: {line}")
    except requests.RequestException:
        print(Colorate.Vertical(Colors.blue_to_red, (f"Error fetching data from ProxyNova.")))
    
    try:
        response = requests.get(f"https://api.usersbox.ru/v1/explain", headers={'Authorization': f'Bearer {USERSBOX_API_KEY}'}, params={'q': phone})
        response.raise_for_status()
        items = response.json().get('data', {}).get('items', [])
        for item in items:
            database = item['source']['database']
            collection = item['source']['collection']
            hits_count = item['hits']['count']
            print(Colorate.Vertical(Colors.blue_to_red, (f"\nУтечки {database}, Collection: {collection}")))
    except requests.RequestException:
        print(Colorate.Vertical(Colors.blue_to_red, (f"Error")))
    
    def search_vk_by_phone(phone):
        response = requests.get(f"https://find.vk.com/phone/{phone}")
        if response.status_code == 200:
            print(Colorate.Vertical(Colors.blue_to_red, (f"VK found!")))
            print(f"https://find.vk.com/phone/{phone}")
            return response
        else:
            print(Colorate.Vertical(Colors.blue_to_red, (f"VK not found")))
            return None
    
    result = search_vk_by_phone(phone)
    if result is not None:
        print(result)
    else:
        print(Colorate.Vertical(Colors.blue_to_red, (f"User with this phone number not found in VK.")))
    
    url = f'https://www.avito.ru/rossiya/telefony?q={phone}'
    response = requests.head(url)
    if response.status_code == 200:
        print(Colorate.Vertical(Colors.blue_to_red, (f'Avito found')))
        print(f"https://www.avito.ru/rossiya/telefony?q={phone}")
    else:
        print(Colorate.Vertical(Colors.blue_to_red, (f'Avito not found')))
    
    def google_search_phone(phone):
        query = f"https://www.google.com/search?q={phone}"
        response = requests.get(query)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('a')
            links = []
            for result in search_results:
                href = result.get('href')
                if href and href.startswith('/url?q='):
                    link = href.replace('/url?q=', '').split('&')[0]
                    links.append(link)
            if len(links) > 0:
                print(Colorate.Vertical(Colors.blue_to_red, (f"Links found:")))
                for link in links:
                    print(Colorate.Vertical(Colors.blue_to_red, (link)))
            else:
                print(Colorate.Vertical(Colors.blue_to_red, (f"Links not found")))
        else:
            print(Colorate.Vertical(Colors.blue_to_red, (f"Error during request")))
    
    google_search_phone(phone)

def main():
    while True:
        choice = input(Colorate.Vertical(Colors.blue_to_red, "выбирай"))
        if choice == '1':
            search_by_number()
        elif choice == '99':
            subprocess.run(['python','main.py'])
        else:
            print(Colorate.Vertical(Colors.blue_to_red, (f"Некорректный выбор")))

if __name__ == "__main__":
    main()