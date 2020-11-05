from bs4 import BeautifulSoup
from requests import session

# Url:  free-proxy-list.net
# Created: November 5, 2020
# Only for educational purposes, I'm not responsible for any action
# MIT License | Copyright (c) 2020 1SniFo

def main(headers):
    http = list()
    url = "https://free-proxy-list.net/"
    page = session().get(url, headers=headers)
    soup = BeautifulSoup(page.text, "lxml")
    table = soup.find("table")
    print(f"[Settings] Leeching:", page.url)
    for row in table.findAll('tr'):
        a = list(row.findAll('td'))
        try:
            test = (a[0].getText() + ":" + a[1].getText())
            http.append(test)
        except:
            pass
    return {"http": http, "socks4": [], "socks5": []}
