""""" Autor: Ariel Diaz
     https://infrasoft.com.ar/
     Salta Argentina 
     Tel: (+549) 3872204925  
     Licence: Creative Commons 
"""""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import csv
import os 
from decouple import config
from basic import *

user = config('sinide_user')
password = config('sinide_password')
site = config('sinide_url')

driver =login(user, password, site)
os.system("cls")
listNoFind = []
with open("migrate.csv", "r") as f:
    lector = csv.reader(f)
    print("Start data enter")
    driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/alumnos")
    input("si cargo el site, presione enter")
    for element in lector:
        print("Data to analize: ")
        element = element[0].split(";")
        driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/alumnos")# Section Student
        time.sleep(2)
        #input("si cargo el site, presione enter \n")
        dni = element[2]
        dni = dni[2:10]
        selenium_input('//*[@id="id_search"]', dni+"\n")
       
        print("Seach to correct Data: " + element[0] +", " +element[1] + "  "+ element[2])
        
        if(not selenium_Button('//*[@id="no-data"]')):
            listNoFind.append(element)
        time.sleep(2)
        driver.refresh()
        os.system("cls")
input("press to End") 
print(listNoFind)
with open("listNoFound.csv", "w") as archivo:
    for elemento in listNoFind:
        archivo.write(f"{elemento}\n")

