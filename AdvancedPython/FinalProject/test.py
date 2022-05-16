from bs4 import BeautifulSoup
import requests
import re
ads = list()
for p in range(0,6):
    r = requests.get('https://divar.ir/s/karaj/buy-apartment?page=',p)
    print(r)
    soup = BeautifulSoup(r.text,'html.parser')
    bodys = soup.find_all("div", class_="post-card-item kt-col-6 kt-col-xxl-4")
    for body in bodys:
        if re.search(r'\>توافقی\<',str(body)):
            pass
        else:
            ads.append(body)
print(len(ads))
# Construction year
# Area
# Floor
# Price
# parking , warehouse , elavator
