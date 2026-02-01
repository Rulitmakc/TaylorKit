import whois
from pystyle import Colors, Colorate
import time
import subprocess
import os 

os.system('cls' if os.name == 'nt' else 'clear')

print(Colorate.Vertical(Colors.blue_to_red, """

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
     ║                                      ║
     ║       (1):поиск по домену            ║
     ║                                      ║
     ║      (2):поиск по айпи сайта         ║
     ║                                      ║
     ║            (99):выйти                ║
     ║                                      ║
     ║ перед использованием скачайте модуль ║
     ║          python_whois                ║
     ╚══════════════════════════════════════╝
"""))
def main():
    while True:
        choice = input (Colorate.Horizontal(Colors.blue_to_red, "выбирай: "))
        if choice == "1":
            domen = input (Colorate.Horizontal(Colors.blue_to_red, "впиши домен (example.com): "))
            time.sleep(1)
            print(Colorate.Horizontal(Colors.blue_to_green, "поиск.."))
            time.sleep(2)
            domain_info = whois.whois(domen)
            print(domain_info)

        elif choice == "2":
            ip = input (Colorate.Horizontal(Colors.blue_to_red, "впиши айпи (192.168.0.1): "))
            time.sleep(1)
            print(Colorate.Horizontal(Colors.blue_to_green, "поиск.."))
            time.sleep(2)
            ipinfo = whois.whois(ip)
            print(ipinfo)

        elif choice == "99":
            print(Colors.red, "выход..")
            time.sleep(2)
            subprocess.run(['python','main.py'])

        else:
            print(Colorate.Horizontal(Colors.red, "\nНеверный выбор !"))
            time.sleep(2)

if __name__ == "__main__":
    main()