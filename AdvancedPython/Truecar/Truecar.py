from bs4 import BeautifulSoup
import requests
import re
import mysql.connector
cnx = mysql.connector.connect(user='testuser', password='',
                              host='127.0.0.1', database= 'truecar')

model_ = input('model: ')
Mymodel = model_.lower()

r = requests.get('https://www.truecar.com/used-cars-for-sale/listings/' + Mymodel)
print(r)

soup = BeautifulSoup(r.text,'html.parser')
bodys = soup.find_all('div' ,class_="card-content vehicle-card-body order-3")

cursor = cnx.cursor()
tablename = Mymodel
quary = 'DROP TABLE IF EXISTS ' + tablename
cursor.execute(quary)
quary = 'CREATE TABLE ' + tablename + '(Model nvarchar(50),Price nvarchar(50), VehicleMileage nvarchar(50))'
cursor.execute(quary)

c = 0
for body in bodys:
    if c < 20:
        modelsoup = BeautifulSoup(str(body),'html.parser')
        model = modelsoup.find_all('span',class_="vehicle-header-make-model text-truncate")
        m = re.findall(r'>(.*)<!-- --> <!-- -->(.*)<',str(model))
        m = m.pop()
        m = m[0] +' '+ m[1]
        pricesoup = BeautifulSoup(str(body),'html.parser')
        price = pricesoup.find_all('div',class_="heading-3 margin-y-1 font-weight-bold")
        p = re.findall(r'Price">(.*)?</div',str(price))
        vehicleMileagesoup = BeautifulSoup(str(body),'html.parser')
        vehicleMileage = vehicleMileagesoup.find_all('div',class_="font-size-1 text-truncate")
        v = re.findall(r'svg>(.*)?<!',str(vehicleMileage))
        cursor.execute('INSERT INTO '+ model_ +' VALUES (\'%s\', \'%s\' , \'%s\')' %(m,p.pop(),v.pop()))
        cnx.commit()
        c += 1
cnx.close()