import requests
import json
from colorama import *
import time
import platform
import os

# who is a Models ?
time.sleep(1)
whosys = platform.uname() [0]
whomodel = platform.uname() [1]

if whomodel == "localhost":

    phone = True
    
else:
    phone = False
    


if whosys == "Windows":
    systems = "win"
    
elif whosys == "Linux":
    systems = "linux"
    

def clear():
    
    if phone == True:
        os.system("clear")
        
    if systems == "linux":
        os.system("clear")

    elif whosys == "Windows":
        
        os.system("cls")

clear()

print(Fore.GREEN+"""

  ███╗   ███╗██████╗      ██████╗  ██████╗ ██╗     ██╗
  ████╗ ████║██╔══██╗    ██╔════╝ ██╔═══██╗██║     ██║
  ██╔████╔██║██████╔╝    ██║  ███╗██║   ██║██║     ██║
  ██║╚██╔╝██║██╔══██╗    ██║   ██║██║   ██║██║     ██║
  ██║ ╚═╝ ██║██║  ██║    ╚██████╔╝╚██████╔╝███████╗██║
  ╚═╝     ╚═╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚══════╝╚═╝
                                                     
""")

init()
time.sleep(0.2)
sleepuser = int(input(Fore.RED+" [!] "+Fore.WHITE+"How many minutes should prices be sent : ")) 
time.sleep(0.2)
print("")
time.sleep(0.2)
chatid = input(Fore.RED+" [!] "+Fore.WHITE+"Please Enter Chat ID : ")
time.sleep(0.2)
print("\n")
print((Fore.RED+" [!] "+Fore.WHITE+"Preparing to send information!"))
time.sleep(3)

print("\n")

url = "http://168.119.202.31:8000/api/v2/crypto/"

def bit():
    http = requests.get(url) .text
    myjson = json.loads(http)
    
    for data in myjson['data']:
        
        name = " نام : "+data['name']
        dollar = " قیمت دلار : "+data['dollar_price']
        toman = " قیمت تومان : "+data['name']
        change = " تغییرات روزانه : "+data['daily_change']
        weekly = " تغییرات هفته  : "+data['weekly_change']

        # print("")
        print(Fore.GREEN+" [+] "+Fore.WHITE+str(data['name'])+Fore.WHITE+" information sent")


        def startservertelegram():
            
            global chatid
            abzar = " سلام قیمت ارز های دیجیتال به شرع زیر است : "+"\n"
            abzar1 = " ساخته شده توسط احسان گلی"
            apiurl = "https://api.telegram.org/bot1580267562:AAEkgLLPoNOjEBGCCBaLS3ukOm-3TAvdds4/sendMessage?chat_id="
            text = "&text="
            url = str(apiurl) + str(chatid) + str(text)
            hello = str(abzar) + str(name) + "\n" + str(dollar) + "\n" + str(toman) + "\n" + str(change) + "\n" + str(weekly) + "\n" # + str(abzar1)
            textuel = url + hello
            payload = {"Urlbox": textuel,"MethodList":"post" }
            httpdebugger = "https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx"
            req = requests.post(httpdebugger , payload)
    
        startservertelegram()


while True:
    bit()
    time.sleep(sleepuser)

