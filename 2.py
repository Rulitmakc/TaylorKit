from pystyle import Colorate, Colors, Center
import os
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests
import webbrowser
import urllib.parse
import platform
import subprocess

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_databases(search_type, query):
    found = False
    
    # Define database file paths for different search types
    if search_type == "phone":
        db_files = ["databases/BD.csv", "databases/BD1.csv", "databases/BD2.csv", "databases/BD3.csv", "databases/BD4.csv", "databases/BD5.csv", "databases/BD6.csv", "databases/BD7.csv", "databases/BD8.csv", "databases/BD9.csv", "databases/BD10.csv", "databases/BD11.csv", "databases/BD12.csv", "databases/BD13.csv", "databases/BD14.csv", "databases/BD15.csv" ,"databases/BD16.csv", "databases/BD17.csv", "databases/BD18.csv", "databases/BD19.csv"]
    elif search_type == "telegram":
        db_files = ["databases/BD.csv", "databases/BD1.csv", "databases/BD2.csv", "databases/BD3.csv", "databases/BD4.csv", "databases/BD5.csv", "databases/BD6.csv", "databases/BD7.csv", "databases/BD8.csv", "databases/BD9.csv", "databases/BD10.csv", "databases/BD11.csv", "databases/BD12.csv", "databases/BD13.csv", "databases/BD14.csv", "databases/BD15.csv" ,"databases/BD16.csv", "databases/BD17.csv", "databases/BD18.csv", "databases/BD19.csv"]
    elif search_type == "email":
        db_files = ["databases/BD.csv", "databases/BD1.csv", "databases/BD2.csv", "databases/BD3.csv", "databases/BD4.csv", "databases/BD5.csv", "databases/BD6.csv", "databases/BD7.csv", "databases/BD8.csv", "databases/BD9.csv", "databases/BD10.csv", "databases/BD11.csv", "databases/BD12.csv", "databases/BD13.csv", "databases/BD14.csv", "databases/BD15.csv" ,"databases/BD16.csv", "databases/BD17.csv", "databases/BD18.csv", "databases/BD19.csv"]
    elif search_type == "name":
        db_files = ["databases/BD.csv", "databases/BD1.csv", "databases/BD2.csv", "databases/BD3.csv", "databases/BD4.csv", "databases/BD5.csv", "databases/BD6.csv", "databases/BD7.csv", "databases/BD8.csv", "databases/BD9.csv", "databases/BD10.csv", "databases/BD11.csv", "databases/BD12.csv", "databases/BD13.csv", "databases/BD14.csv", "databases/BD15.csv" ,"databases/BD16.csv", "databases/BD17.csv", "databases/BD18.csv", "databases/BD19.csv"]
    else:
        print(Colorate.Horizontal(Colors.red_to_yellow, "\n[!] по новой"))
        return

    print(Colorate.Horizontal(Colors.blue_to_green, f"\n[#] Идет поиск"))

    for db_file in db_files:
        try:
            if not os.path.exists(db_file):
                print(Colorate.Horizontal(Colors.red_to_yellow, f"\n[!] Бд не найдена: {db_file}"))
                continue
                
            with open(db_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                db_found = False
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                        
                    if query.lower() in line.lower():
                        if not db_found:
                            print(Colorate.Horizontal(Colors.blue_to_green, f"\n[+] Найдены совпадения:"))
                            db_found = True
                            
                        parts = line.split(',')
                        for part in parts:
                            part = part.strip('" ')
                            if part:
                                print(Colorate.Horizontal(Colors.blue_to_red, f"└─▶ {part}"))
                        found = True
                        
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_yellow, f"\n[!] Ошибка чтения бд {db_file}: {str(e)}"))

    if not found:
        print(Colorate.Horizontal(Colors.red_to_yellow, "\n[-] Совпадений нету"))

def lookup_phone(phone):
    try:
        parsed_number = phonenumbers.parse(phone)
        location = geocoder.description_for_number(parsed_number, "ru")
        operator = carrier.name_for_number(parsed_number, "ru")
        time_zones = timezone.time_zones_for_number(parsed_number)
        
        print(Colorate.Horizontal(Colors.blue_to_red, "\n[+] Информация о номере:"))
        print(Colorate.Horizontal(Colors.blue_to_red, f"└─▶ Страна: {location}"))
        print(Colorate.Horizontal(Colors.blue_to_red, f"└─▶ Оператор: {operator}"))
        
        filtered_zones = []
        if location == "Russia":
            filtered_zones = [tz for tz in time_zones if "Asia" in tz or "Europe" in tz]
            filtered_zones.sort()
        else:
            filtered_zones = time_zones
            
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"└─▶ Часовой пояс: {', '.join(filtered_zones)}"))

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
        
        print(Colorate.Horizontal(Colors.blue_to_red, "\n[+] Возможные ссылки на соцсети:"))
        print(Colorate.Horizontal(Colors.blue_to_red, f"└─▶ WhatsApp: https://wa.me/{phone.replace('+', '')}"))
        print(Colorate.Horizontal(Colors.blue_to_red, f"└─▶ Telegram: https://t.me/+{phone.replace('+', '')}"))
        print(Colorate.Horizontal(Colors.blue_to_red, f"└─▶ Viber: viber://chat?number={phone.replace('+', '')}"))
            
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_yellow, f"\n[!] Ошибка поиска информации: {str(e)}"))
        print(Colorate.Horizontal(Colors.red_to_yellow, "[!] Проверьте формат номера телефона"))

def main():
    
    while True:
        print(Center.XCenter(Colorate.Vertical(Colors.blue_to_red, '''


████████╗░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░    ░██████╗░█████╗░███████╗████████╗
╚══██╔══╝██╔══██╗╚██╗░██╔╝██║░░░░░██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██╔════╝╚══██╔══╝
░░░██║░░░███████║░╚████╔╝░██║░░░░░██║░░██║██████╔╝    ╚█████╗░██║░░██║█████╗░░░░░██║░░░
░░░██║░░░██╔══██║░░╚██╔╝░░██║░░░░░██║░░██║██╔══██╗    ░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░
░░░██║░░░██║░░██║░░░██║░░░███████╗╚█████╔╝██║░░██║    ██████╔╝╚█████╔╝██║░░░░░░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝    ╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░
---------------------------------------------------------------------------------------
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║$$$$$$$$$$$$$$$$$$$$║------------------------------║$$$$$$$$$$$$$$$$$$$║
    ║$$$$$$$$$$$$$$$$$$$║ https://t.me/+w3jbAuqfNzM1MDQy ║$$$$$$$$$$$$$$$$$$║
    ║$$$$$$$$$$$$$$$$$$$$║------------------------------║$$$$$$$$$$$$$$$$$$$║
    ║═══════════════════════════════════════════════════════════════════════║
    ║                                                                       ║
    ║                                                                       ║
    ║                                                                       ║
    ║                 		╔══════════════════╗                        ║
    ║                 		║ [1]:П0ИСК П0 БД  ║                        ║
    ║                 		║                  ║                        ║
    ║                 		║   [99]:ВЫХ0Д     ║           		    ║
    ║                		╚══════════════════╝            	    ║
    ║    ╔═══════════════════════════════════════════════════════════╗      ║
    ║    ║          		АВТ0Р НЕ ПРИЗЫВАЕТ                   ║      ║
    ║    ║         	       К ПЛ0ХИМ ДЕЙВСТВИЯМ                   ║      ║
    ║    ║    		П0ЛЬЗУЙТЕСЬ С УЧЕТ0М ЭТИКИ И ЗАК0НА          ║      ║
    ║    ║               	    УДАЧИ!                           ║      ║
    ║    ║      ------------------------------------------           ║      ║
    ║    ╚═══════════════════════════════════════════════════════════╝      ║
    ║                          ║ VERSION:KIT ║                              ║
    ║                          ║-------------║              	            ║
    ╚═══════════════════════════════════════════════════════════════════════╝
''')))

        choice = input(Colorate.Horizontal(Colors.blue_to_red, "\n[#] Выберите опцию: "))
        
        if choice == "1":
            print(Colorate.Horizontal(Colors.blue_to_green, """
╭────────────────────────╮
(     ПОИСК ПО БД.       ) 
╰────────────────────────╯

[1] Поиск по юзу тг
[2] Поиск по номеру 
[3] Поиск по почте 
[4] Поиск по ФИО"""))
            
            search_choice = input(Colorate.Horizontal(Colors.blue_to_green, "\n[#] Выберите тип поиска: "))
            
            if search_choice not in ["1", "2", "3", "4"]:
                print(Colorate.Horizontal(Colors.blue_to_red, "\n[!] гавна выбор"))
                continue
                
            query = input(Colorate.Horizontal(Colors.blue_to_green, "\n[#] че найте надо: "))
            
            search_types = {
                "1": "telegram",
                "2": "phone",
                "3": "email", 
                "4": "name"
            }
            
            search_databases(search_types[search_choice], query)
            input(Colorate.Horizontal(Colors.blue_to_red, "\n[#] тап энтер чтоб продолжить"))
            
        elif choice == "21231231231231232":
            print(Colorate.Horizontal(Colors.blue_to_red, """
╭────────────────────────╮
(    ПОИСК ПО НОМЕРУ     )
╰────────────────────────╯"""))
            
            phone = input(Colorate.Horizontal(Colors.blue_to_green, "\n[#] Введите номер телефона (например +79991234567): "))
            lookup_phone(phone)
            input(Colorate.Horizontal(Colors.blue_to_green, "\n[#] тап энтер чтоб продолжить"))

        elif choice == "99":
            print(Colorate.Horizontal(Colors.blue_to_red,"\n выход"))
            subprocess.run(['python','main.py'])
            
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "\n[!] Неверный выбор"))
            continue

if __name__ == "__main__":
    main()