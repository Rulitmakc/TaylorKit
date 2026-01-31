import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from pystyle import Colors, Colorate
import subprocess
import os 

senders = {
    'interollsnos@rambler.ru': 'feDLSiueGT89APb81v74',
    'islamhuynya@gmail.com': 'zmARvx1MRvXppZV6xkXj',
    'kirillobsos40@gmail.com': '1CtFuHTaQxNda8X06CaQ',
    'andreytelegram4@gmail.com': 'DFa12912',
'mildredperez653@gmail.com': 'ejiv57j5vknn',
'kaysnyder872@gmail.com': 'kdub58k6blnm',
'gailfranco025@gmail.com': 'kfub84pm8njx',
'bradmitchellgf54@gmail.com': 'vgftr5432w',
'dylanjnpi1910@gmail.com': 'bo96ffco',
'chasityrojas759@gmail.com': 'kdhb75j8bkk',
'arianahqds1908@gmail.com': 'cxS7NV09',
'chennicholas43@gmail.com': 'wzxdsfgvhjk',
'baileyonbw1904@gmail.com': '49H578jI',
'nathanddas1969@gmail.com': 'CfJ14Nd3',
'abbottdarrell89@gmail.com': 'bs26ry47ui',
'noradlci1923@gmail.com': 'yY74w4GG',
'haroldmendez524@gmail.com': 'rdvbnmjklh',
'jasonevhx2000@gmail.com': 'Yka4cT6M',
'carsonsmallhu78@gmail.com': 'bv65r4e3wa',
'milacmrv2015@gmail.com': 'u20fi6UK',
'maricooke852@gmail.com': 'kvjvb35yg5rfd',
'lanceanthonys453@gmail.com': 'ur54ed32wv',
'benjaminqlmm1934@gmail.com': 'TG2XC9e1',
'marshadawson089@gmail.com': 'kdh64kb6knk',
'haroldhart635@gmail.com': 'swqertyhuio',
'patscott6451@gmail.com': 'djiv75l7bln',
'magamed123123321@gmail.com': 'magamed111',
'andreysorokiin567@gmail.com': 'dadada789',
'glebpabg044@gmail.com': 'pubg7731',
'i71902739@gmail.com': 'lolipap89',
'davijd888@gmail.com': 'daviid890',
'vanavertov777@gmail.com': 'vertov777',
'jsjdjdjdhdfb@gmail.com': 'Interpoll231',
'timurvysockij374@gmail.com': 'timurka654',
'nikitagelev7@gmail.com': 'ckazka890',
'chtkotskiy@mail.ru': 'kakaha567',
'paveldyrov@mail.ru': 'pipkas78',
'pavlovncivan@gmail.com': 'cabaka45',
'nikitavaceslav6@gmail.com': 'nekit2022',
'cmctelegram@gmail.com': 'piska9087',
'podderzkatelegram7@gmai.com': 'teleru65',
'gryzp9608@gmail.com': 'pipiska789',
'orgtelegram360@gmail.com': 'legen6790'
}
receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def logo():

     os.system('cls' if os.name == 'nt' else 'clear')

     print(Colorate.Horizontal(Colors.blue_to_red, """
                               
    ████████╗░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░
    ╚══██╔══╝██╔══██╗╚██╗░██╔╝██║░░░░░██╔══██╗██╔══██╗
    ░░░██║░░░███████║░╚████╔╝░██║░░░░░██║░░██║██████╔╝
    ░░░██║░░░██╔══██║░░╚██╔╝░░██║░░░░░██║░░██║██╔══██╗
     ░░██║░░░██║░░██║░░░██║░░░███████╗╚█████╔╝██║░░██║
    ░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝

            ░██████╗███╗░░██╗░█████╗░░██████╗
            ██╔════╝████╗░██║██╔══██╗██╔════╝
            ╚█████╗░██╔██╗██║██║░░██║╚█████╗░
             ╚═══██╗██║╚████║██║░░██║░╚═══██╗
            ██████╔╝██║░╚███║╚█████╔╝██████╔╝
            ╚═════╝░╚═╝░░╚══╝░╚════╝░╚═════╝░
            ╔══════════════════════════════════╗
            ║##################################║
            ║#                                #║
            ║#          (1):снос ака          #║
            ║#                                #║
            ║#        (2):снос канала         #║
            ║#                                #║
            ║#         (3):снос бота          #║
            ║#                                #║
            ║#          [99] Выйти            #║
            ║#                                #║
            ║###############KIT################║
            ╚══════════════════════════════════╝
"""))



def menu():

    choice = input("ВЫБИРАЙ: ")
    return choice
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    logo()
    choice = menu()
    if choice == '1':
        print(Colorate.Horizontal(Colors.blue_to_red, "1. СНОС ЗА ДЕТСКУЮ ПОРНУХУ."))
        print(Colorate.Horizontal(Colors.blue_to_red, "2. СНОС ДОКСЕРОВ."))
        print(Colorate.Horizontal(Colors.blue_to_red, "4. СНОС СЕССИЙ."))
        print(Colorate.Horizontal(Colors.blue_to_red, "5. СНОС АККАУНТА С ПРЕМКОЙ"))
        print(Colorate.Horizontal(Colors.blue_to_red, "6. СНОС АККАУНТА С ВИРТ НОМЕРОМ."))
        comp_choice = input(Colorate.Horizontal(Colors.blue_to_red, "ВЫБИРАЙ: "))
        if comp_choice in ["1", "2", "3"]:
            print(Colorate.Horizontal(Colors.blue_to_red, "СЛЕДУЙТЕ УКАЗАНИЯМ.. "))
            username = input(Colorate.Horizontal(Colors.blue_to_red, "ЮЗЕP ЖЕРТВЫ: "))
            id = input(Colorate.Horizontal(Colors.blue_to_red, "АЙДИ ЖЕРТВЫ: "))
            chat_link = input(Colorate.Horizontal(Colors.blue_to_red, "ССЫЛКА НА ЧАТ: "))
            violation_link = input(Colorate.Horizontal(Colors.blue_to_red, "ССЫЛКА НА НАРУШЕНИЕ В ЧАТЕ: "))
            print(Colorate.Horizontal(Colors.blue_to_red, "ОЖИДАЙТЕ..."))
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который продает порнографию с участием несовершеннолетних. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. прошу заблокировать данного пользывателя.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 14888
                    time.sleep(1)

        elif comp_choice == "4":
            username = input(Colorate.Horizontal(Colors.blue_to_red, "ЮЗЕРНЕЙМ ЖЕРТВЫ: "))
            id = input(Colorate.Horizontal(Colors.blue_to_red, "АЙДИ ЖЕРТВЫ: "))
            print(Colorate.Horizontal(Colors.blue_to_red, "ОЖИДАЙТЕ."))
            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                    print(Colorate.Horizontal(Colors.blue_to_red, f"Отправлено на {receiver} от {sender_email}!"))
                    sent_emails += 14888
                    time.sleep(1)

        elif comp_choice in ["5", "6"]:
            username = input(Colorate.Horizontal(Colors.blue_to_red, "ЮЗЕРНЕЙМ ЖЕРТВЫ: "))
            id = input(Colorate.Horizontal(Colors.blue_to_red, "АЙДИ ЖЕРТВЫ: "))
            comp_texts = {
                "5": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                "6": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 9999
                    time.sleep(1)


    elif choice == "2":
        
        print(Colorate.Horizontal(Colors.blue_to_red, "1. С ЛИЧНЫМИ ДАННЫМИ"))
        print(Colorate.Horizontal(Colors.blue_to_red, "2. С ЖИВОДЁРСТВОМ "))
        print(Colorate.Horizontal(Colors.blue_to_red, "3. С ЦП"))
        print(Colorate.Horizontal(Colors.blue_to_red, "4. ДЛЯ КАНАЛОВ С ПРАЙСАМИ"))
        ch_choice = input(Colorate.Horizontal(Colors.blue_to_red, "ВЫБИРАЙ: "))

        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input(Colorate.Horizontal(Colors.blue_to_red, "ССЫЛКА НА КАНАЛ: "))
            channel_violation = input(Colorate.Horizontal(Colors.blue_to_red, "ССЫЛКА НА НАРУШЕНИЕ: "))
            print(Colorate.Horizontal(Colors.blue_to_red, "ОЖИДАЙТЕ"))
            comp_texts = ()
         
            
            print(Colorate.Horizontal(Colors.blue_to_red, "ОЖИДАЙТЕ"))
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 100000
                    time.sleep(5)

    elif choice == "3":
        print(Colorate.Horizontal(Colors.blue_to_red, "1.СНОС ЗА ДЕТСКИЙ ПОРНА"))
        print(Colorate.Horizontal(Colors.blue_to_red, "2.СНОС ЗА РАСЧЛЕНЕНКУ И ТП"))
        bot_ch = input(Colorate.Horizontal(Colors.blue_to_red, "ВЫБИРАЙТЕ: "))

        if bot_ch == "1":
            bot_user = input(Colorate.Horizontal(Colors.blue_to_red, "ЮЗЕРНЕЙМ БОТА: "))
            print(Colorate.Horizontal(Colors.blue_to_red, "ОЖИДАЙТЕ"))
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который занимается распространением порнографии с участием несовершеннолетних . Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                    print(Colorate.Horizontal(Colors.blue_to_red, f"Отправлено на {receiver} от {sender_email}!"))
                    sent_emails += 1
                    time.sleep(1)
        
        elif choice == "99":
            subprocess.run(['python','main.py'])
        
        

  
if __name__ == "__main__":
    main()