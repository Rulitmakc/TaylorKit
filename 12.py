import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from termcolor import colored
from pystyle import Colorate, Colors, Center

os.system('cls' if os.name == 'nt' else 'clear')

banner = """
████████╗ █████╗ ██╗   ██╗██╗      ██████╗ ██████╗ 
╚══██╔══╝██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗██╔══██╗
   ██║   ███████║ ╚████╔╝ ██║     ██║   ██║██████╔╝
   ██║   ██╔══██║  ╚██╔╝  ██║     ██║   ██║██╔══██╗
   ██║   ██║  ██║   ██║   ███████╗╚██████╔╝██║  ██║
   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝
                                                   
███████╗██████╗  █████╗ ███╗   ███╗                
██╔════╝██╔══██╗██╔══██╗████╗ ████║                
███████╗██████╔╝███████║██╔████╔██║                
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║                
███████║██║     ██║  ██║██║ ╚═╝ ██║                
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝                
                                                   
"""
print(Colorate.Vertical(Colors.blue_to_red, banner))
main = """ написать на почту 
╔══════════════════════════════════╗
║[1] - Отправить                   ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""
print(Colorate.Vertical(Colors.blue_to_red, main))
def send_email(sender_email, sender_password, receiver_email, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = theme
        msg.attach(MIMEText(message, 'plain'))
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(Colorate.Horizontal(Colors.red_to_blue, f"Письмо успешно отправлено от {sender_email} на {receiver_email}!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"Ошибка при отправке письма от {sender_email} на {receiver_email}"))
senders ={
  'gucguguguuggihigg@gmail.com': 'vadd baad eojx hbcm',
  'ydghffydshsjsjdj@gmail.com': 'xoml ybkq ghfg jtev',
  'iydititzdyztxufxfuxfy@gmail.com': 'hqgd avqh jkca',
  'dhdjnddndzbxjxjjcjxjxxkx@gmail.com': 'zusw ftcj dcrg tmyy',
  'siyryrkyhdtjjydgi@gmail.com': 'krcs qfpo iwxj gwua',
  'ueehehrhrjj67@gmail.com': 'unvj scxu cqky mucn',
  'lvlvllccovlvddv@gmail.com': 'rykq ypcv lqla fqip'
}

def main():
    while True:
        command = input(Colorate.Horizontal(Colors.red_to_blue, "\nВыбирай: "))
        if command == "1":
            gmail = input(Colorate.Horizontal(Colors.red_to_blue, "куда?: "))
            theme = input(Colorate.Horizontal(Colors.red_to_blue, "Введи заголовок: "))
            receivers = [f'{gmail}']
            message = input('Текст: ')
            for sender_email, sender_password in senders.items():
                for receiver_email in receivers:
                    send_email(sender_email, sender_password, receiver_email, message)
        elif command == "99":
            print(Colorate.Horizontal(Colors.red_to_blue, "выхожу"))
            os.system("python main.py")
            break
        else:
            print(Colorate.Horizontal(Colors.red_to_blue, "даун или 1 или 99"))

if __name__ == "__main__":
    main()
