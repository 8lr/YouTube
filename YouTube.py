import os,random,requests,time
from colorama import Fore
import sys as n
import time as mm
from time import sleep


def KURD(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 100)
KURD('''


        __   __        _____     _          
        \ \ / /       |_   _|   | |         
         \ V /___  _   _| |_   _| |__   ___ 
          \ // _ \| | | | | | | | '_ \ / _ \\
          | | (_) | |_| | | |_| | |_) |  __/
          \_/\___/ \__,_\_/\__,_|_.__/ \___|
                                    
                Author --> #UNIX
                Telegram --> U33UP
                Telegram Channel --> B_G_Y / E4CBM
                Instagram --> E4CB
                Github --> 8LR
''')
good = 0
bad = 0
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,tr-TR;q=0.6,tr;q=0.5,ckb;q=0.4',
    'cookie': 'VISITOR_INFO1_LIVE=LKvEWodn4Rc; YSC=2hEQ-YaAyjI; PREF=tz=Asia.Baghdad&f6=400&f7=100; GPS=1',
    'sec-ch-ua': 'Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"107.0.5304.107"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="107.0.5304.107", "Chromium";v="107.0.5304.107", "Not=A?Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'service-worker-navigation-preload': 'true',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
id = input("Enter you Telegram ID >> ")
mm.sleep(1)
token = input("Enter you token bot >> ")
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
num = int(input("How many letters do you want for the usernames to be >> "))
if num <= 3:
    print("We cannot choose smaller or equal to 3")
    input("Press Enter to exit")
    exit()
else:
    UNIX = 'abcdefghigklmnopqrstuvwxyz_-'
    while True:
        req = requests.session()
        raha = str("".join(random.choice(UNIX)for x in range(int(num))))
        sleep(1)
        YouTube = f'https://www.youtube.com/@{raha}'
        e4cb = requests.get(YouTube,headers=header)
        if e4cb.status_code ==404:
            print(Fore.GREEN+f"Username Available >> {raha}")
            good +=1
            print(f"{green}Good:{good} {blue}/ {red}Bad:{bad}")
            Telegram =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=YouTube Available ✅\nUsername: {raha}\n————————-\nTELE: @U33UP\nChannel: @B_G_Y / @E4CBM ')
            req = requests.post(Telegram)
        else:
            print(Fore.RED+f"Username Unavailable >> {raha}")
            bad +=1
            print(f"{green}Good:{good} {blue}/ {red}Bad:{bad}")
