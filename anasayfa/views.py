from django.http import HttpResponse
from django.template import loader
from.models import User
import  requests
from bs4 import BeautifulSoup


url = "https://arsiv.mackolik.com/Iddaa-Programi"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

solmenu = soup.find_all("tr", id="Tr2", limit=100)
print("toplam maç",len(solmenu))



Dict={}
for mac in solmenu:

  ev_sahibi = mac.find_all("a", {"class": "iddaa-rows-style"}, limit=30)[0].text
  misafir = mac.find_all("a", {"class": "iddaa-rows-style"}, limit=30)[2].text

  ms1 = mac.find_all("a", {"class": "iddaa-rate MS1"}, limit=30)[0].text
  ms0 = mac.find_all("a", {"class": "iddaa-rate MSX"}, limit=30)[0].text
  ms2 = mac.find_all("a", {"class": "iddaa-rate MS2"}, limit=30)[0].text
  kod = mac.find_all("td", limit=30)[9].text

  saat = mac.find_all("td",limit=30)[0].text

  Dict[kod]= {"kod":kod,"saat":saat,"ev_sahibi" :ev_sahibi +misafir , "ms1":ms1 ,"ms0":ms0, "ms2":ms2}








def index(request):
  print(Dict)

  template = loader.get_template('anasayfa.html')
  context = {
    'users' : Dict,
  }

  return HttpResponse(template.render(context,request))

