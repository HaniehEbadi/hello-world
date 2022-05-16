import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import mysql.connector
cnx = mysql.connector.connect(user='testuser', password='',
                              host='127.0.0.1', database= 'divar')

cursor = cnx.cursor()
#quary = 'CREATE DATABASE divar'
tablename = 'tehranpars'
n = 200 #number of ads(min)
quary = 'DROP TABLE IF EXISTS ' + tablename
cursor.execute(quary)
quary = 'CREATE TABLE ' + tablename + '(ID int,Location nvarchar(100),Price_m nvarchar(50),Price nvarchar(50),Area nvarchar(20),Construction nvarchar(20),Parking nvarchar(2),Warehouse nvarchar(2),Elavator nvarchar(2),Floor nvarchar(15),Room nvarchar(10), gh char(1))'
cursor.execute(quary)

browser=webdriver.Firefox()
browser.get('https://divar.ir/s/tehran/buy-apartment/east-tehran-pars?non-negotiable=true&size=-70&building-age=0-5')

def scroll(k):
    k = 184 * k
    browser.execute_script("window.scrollBy(0,"+ str(k) +")")
    time.sleep(2)

def fetch_links():
    body = browser.find_element(By.TAG_NAME,'main')
    links = body.find_elements(By.TAG_NAME,'a')
    link_urls = [l.get_property('href') for l in links]
    return link_urls

def faToen(num):
    l = len(num)
    num = num.split('٬')
    num = ''.join(num)
    num = int(num)
    p = '{:,}'
    num = p.format(num)
    return num

LinkUrls = list()

link_urls = fetch_links()
LinkUrls.extend(link_urls[0:13])
L = 0
while(L<n):
    llu = len(link_urls) 
    llu = llu / 3
    scroll(int(llu))
    link_urls = fetch_links()
    if link_urls[len(link_urls)-1] not in LinkUrls:
        LinkUrls.extend(link_urls)
    if len(LinkUrls) == L:
        L = n
    else:
        L = len(LinkUrls)
    print(len(LinkUrls))

c = 0
ID = 0
List = list()
while(c+1<len(LinkUrls)):
    c += 1
    browser.get(LinkUrls[c])
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source,'html.parser')
    body = soup.find_all('div' ,class_="post-info")
    bodysoup = BeautifulSoup(str(body))

    location = bodysoup.find_all('div' ,class_="kt-wrapper-row__child")
    if len(location) != 0:
        l = re.findall(r'.*در(.*)<',str(location))
        location = l.pop()
        location = location.split()
        location = '‌'.join(location)
        location = '{:^20}'.format(location)

        gholname = bodysoup.find_all('p',class_="kt-description-row__text--primary") 
        ghol = re.findall(r'سند ندارد',str(gholname))
        if len(ghol) == 0:
            gh = 1
        else:
            gh = 0 

        group1 = bodysoup.find_all('span',class_="kt-group-row-item__value")
        g1 = list() # area,construction,room
        for i in range(0,3):
            g1.append(re.findall(r'>(.*)?<',str(group1[i])).pop())
        room = g1.pop()
        if room.isdigit():
            room = int(room)
        construction = g1.pop()
        area = g1.pop()

        g3 = list() # elevator,parking,warehouse
        for i in range(3,6):
            item = re.findall(r'ندارد',str(group1[i]))
            if len(item) == 0:
                g3.append('OK')
            else :
                g3.append('X')

        group2 = bodysoup.find_all('p' ,class_="kt-unexpandable-row__value")
        floor = re.findall(r'>(.*)?<',str(group2.pop())).pop() #translate
        if len(group2) == 3 :
            group2.pop() #trash شخصی یا املاک
        
        price_per_metr = re.findall(r'>(.*)?<',str(group2.pop())).pop()
        price_per_metr = price_per_metr.split()
        price_per_metr = faToen(price_per_metr[0])
        
        price = re.findall(r'>(.*)?<',str(group2.pop())).pop()
        price = price.split()
        price = faToen(price[0])

        if (area,price,construction) not in List:
            ID += 1
            List.append((area,price,construction))
            cursor.execute('INSERT INTO '+ tablename +' VALUES (\'%i\', \'%s\', \'%s\', \'%s\', \'%i\', \'%i\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' %(ID,location,price_per_metr,price,int(area),int(construction),g3[1],g3[2],g3[0],floor,room,gh))
            cnx.commit()
        print(ID,c,len(LinkUrls))
browser.close()

quary = 'SELECT * FROM ' + tablename + ''' INTO OUTFILE 'C:\\\\ProgramData\\\\MySQL\\\\MySQL Server 8.0\\\\Uploads\\\\tehranpars.csv'
        FIELDS ENCLOSED BY '"'
        TERMINATED BY ','
        LINES TERMINATED BY '\n'; '''
cursor.execute(quary)

cnx.close()