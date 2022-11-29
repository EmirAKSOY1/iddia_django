import  requests
from bs4 import BeautifulSoup
import json
import time
import datetime

url = "https://arsiv.mackolik.com/Iddaa-Programi"
while True:
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")

    solmenu = soup.find_all("tr", id="Tr2", limit=30)

    def write_json(new_data, filename='maclar2.json'):
        with open(filename, 'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["maclar"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent=4)



    for mac in solmenu:
        ev_sahibi = mac.find_all("a", {"class": "iddaa-rows-style"}, limit=30)[0].text
        misafir = mac.find_all("a", {"class": "iddaa-rows-style"}, limit=30)[2].text

        ms1 = mac.find_all("a", {"class": "iddaa-rate MS1"}, limit=30)[0].text
        ms0 = mac.find_all("a", {"class": "iddaa-rate MSX"}, limit=30)[0].text
        ms2 = mac.find_all("a", {"class": "iddaa-rate MS2"}, limit=30)[0].text

        saat = mac.find_all("td",limit=30)[0].text
        kod = mac.find_all("td",limit=30)[9].text
        #saat = datetime.datetime.now()
        print(kod,"-",saat, '=>', ev_sahibi, '-', misafir, end="")
        print("Ms:", ms1, 'X', ms0, 'X', ms2)
        # y = {"takimlar": ev_sahibi + '-' + misafir,
        #      "mac-tarih": saat.minute,
        #      "MS1": ms1,
        #      "MS0": ms0,
        #      "MS2": ms2
        #      }
        # write_json(y)


    time.sleep(60)
    write_json("")
