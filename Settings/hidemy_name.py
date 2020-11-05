from bs4 import BeautifulSoup
from requests import session

# Url:  https://hidemy.name
# Created: October 25, 2020
# Only for educational purposes, I'm not responsible for any action
# MIT License | Copyright (c) 2020 1SniFo

def main(headers):
    http = list()
    socks4 = list()
    socks5 = list()
    start = 0
    old = 0
    while True:
        page = session().get(f"https://hidemy.name/en/proxy-list/?start={start}#list", headers=headers)
        print(f"[Settings] [{start}] Leeching:", page.url)
        start += 64
        soup = BeautifulSoup(page.text, "lxml")
        table = soup.find("table")
        for row in table.findAll('tr'):
            a = list(row.findAll('td'))
            try:
                proxy_type = a[4].getText().lower()
                proxy = (a[0].getText() + ":" + a[1].getText())
                if "http" in proxy_type:
                    http.append(proxy)
                elif "socks4" in proxy_type:
                    socks4.append(proxy)
                elif "socks5" in proxy_type:
                    socks5.append(proxy)
            except:
                pass
        if len(http) + len(socks4) + len(socks5) == old:
            return {"http": http, "socks4": socks4, "socks5": socks5}
        else:
            old = len(http) + len(socks4) + len(socks5)

