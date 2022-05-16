import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import mysql.connector
cnx = mysql.connector.connect(user='testuser', password='',
                              host='127.0.0.1')#, database= 'divar')

cursor = cnx.cursor()
#quary = 'CREATE DATABASE Digi'
cursor.execute(quary)

n = int(input('n = ')) #number of ads(min)
tablename = input('tablename = ')
quary = 'DROP TABLE IF EXISTS ' + tablename
cursor.execute(quary)
quary = 'CREATE TABLE ' + tablename + '(ID int, nvarchar(100),Price_m nvarchar(50),Price nvarchar(50),Area nvarchar(20),Construction nvarchar(20),Parking nvarchar(2),Warehouse nvarchar(2),Elavator nvarchar(2),Floor nvarchar(15),Room nvarchar(10), gh char(1))'
cursor.execute(quary)