import yaml
import importlib.util
from requests import session
from time import sleep

class main:
    def __init__(self):
        self.http = []
        self.socks4 = []
        self.socks5 = []

        # Loading config > from class with importing Config.yml
        try:
            with open('Config.yml', encoding="utf8") as file:
                config = yaml.full_load(file)['main']
                user_agent = {'User-agent': str(config['User_agent'])}
                self.IsColors = bool(config['colors'])
                duplicates = bool(config['duplicates'])
                # <------- leech Section ------->
                leech_enable = bool(config['leech']['enable'])
                leech_Settings = list(config['leech']['settings'])
                # <------- import Section ------->
                download_enable = bool(config['download']['enable'])
                # api
                api_list = {
                    "http": list(config['download']['api']['http']),
                    "socks4": list(config['download']['api']['socks4']),
                    "socks5": list(config['download']['api']['socks5'])
                }
                file.close()
        except Exception as error:
            print(self.colors("Error", 'red', f"On Loading config: {error}", 'none'))
        if download_enable:
            for i in api_list:
                for c in api_list[i]:
                    if len(c) > 5:
                        print(self.colors("Loading", 'red', f"Url: {c}", 'none'))
                        self.save(self.load(c), i)
        if leech_enable:
            for i in leech_Settings:
                try:
                    print(self.colors("Leeching", 'green', f"Loading {i}", 'none'))
                    spec = importlib.util.spec_from_file_location("module.main", f"Settings/{i}")
                    foo = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(foo)
                    test = foo.main(user_agent)
                    for k in test:
                        self.save(test[k], k)
                except Exception as error:
                    print(self.colors(type(error).__name__, 'red', f"Something happen on {i}", 'none'))
        total = len(self.http) + len(self.socks4) + len(self.socks5)
        if duplicates:
            self.http = list(dict.fromkeys(self.http))
            self.socks4 = list(dict.fromkeys(self.socks4))
            self.socks5 = list(dict.fromkeys(self.socks5))
            New_total = len(self.http) + len(self.socks4) + len(self.socks5)
            print(self.colors("Duplicates", 'rose', f"{total - New_total} proxies has been removed", 'none'))
        total = len(self.http) + len(self.socks4) + len(self.socks5)
        for t in api_list:
            with open(f"output/{t}.txt", "w") as w:
                if t == "http":
                    w.writelines("%s\n" % place for place in self.http)
                elif t == "socks4":
                    w.writelines("%s\n" % place for place in self.socks4)
                else:
                    w.writelines("%s\n" % place for place in self.socks5)
            w.close()
        print(self.colors("Completed", "blue", f"with result of http(s):{len(self.http)} and socks4:{len(self.socks4)} and socks5:{len(self.socks5)} final total:{total}", 'none'))


    def save(self, proxies, px_type):
        if px_type == "http":
            self.http += proxies
        elif px_type == "socks4":
            self.socks4 += proxies
        else:
            self.socks5 += proxies

    def load(self, url):
        while True:
            try:
                download = session().get(url, timeout=6)
                print(self.colors("Successful", 'green', f"Loading Url: {url}", 'none'))
                return list(download.text.split())
            except Exception as e:
                print(self.colors(type(e).__name__, 'red', f"Url: {url} retrying in few seconds", 'none'))
                sleep(6)


    def colors(self, title, title_color, msg, msg_color):
        color_type = {
            "none": '',
            "rose": '\033[95m',
            "blue": '\033[94m',
            "cyan": '\033[96m',
            "green": '\033[92m',
            "yellow": '\033[93m',
            "red": '\033[91m'}
        if self.IsColors:
            return f"[{color_type[title_color]}{title}\033[0m] {color_type[msg_color]}{msg}\033[0m"
        else:
            return msg


if __name__ == "__main__":
    print("""\n       ꧁༺ 𝓹𝓻𝓸𝔁𝔂 𝓵𝓮𝓮𝓬𝓱𝓮𝓻 𝓫𝔂 𝓢𝓷𝓲𝓯𝓸 ༻꧂
                ꧁༺ 𝓥1.0 ༻꧂\n\n""")
    main()
