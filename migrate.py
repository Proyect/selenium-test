""""" Autor: Ariel Diaz
     https://infrasoft.com.ar/
     Salta Argentina 
     Tel: (+549) 387 220 49 25  
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
        #print(element)
        driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/alumnos")# Section Student        
        time.sleep(4)
        #input("si cargo el site, presione enter \n")
        selenium_input("id_search", element[3],"ID")
        selenium_Button("agregar_alumno_btn", "ID")
        
        print("Seach to correct Data: " + element[2] +", " +element[1] + "  "+ element[3])
        selenium_input("persona-busqueda-input", element[3], "ID")
        selenium_Button("persona-busqueda-buscar", "ID")        

        ops = input("Ingrese: 1: si es la persona correcta. 2: si requiere verificacion de datos \n")
        if(ops == "1"):
            selenium_Button('//*[@id="table-buscar"]/table/tbody/tr/td[8]/a/span')            
            time.sleep(6)
            selenium_input('//*[@id="provincia_nacimiento"]/div[1]/span', "Salta")            
           
            if(element[10]=="M"):
                selenium_input('//*[@id="sexo"]/div[1]/span/span[2]/span', "Masculino")                
            else:
                selenium_input('//*[@id="sexo"]/div[1]/span/span[2]/span', "Femenino")                
            
            input("presione enter si los datos son correctos")
            selenium_Button('//*[@id="form-buttons"]/div/button/span')            
        elif(ops=="2"):
            selenium_Button('//*[@id="closeSearchModal"]/span')
            listNoFind.append(element)           
        else:
            pass
input("press to End") 
print(listNoFind)
with open("listNoFound.csv", "w") as archivo:
    for elemento in listNoFind:
        archivo.write(f"{elemento}\n")