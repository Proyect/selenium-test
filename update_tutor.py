""""" Autor: Ariel Diaz
     https://infrasoft.com.ar/
     Salta Argentina 
     Tel: (+549) 3872204925  
     Licence: Creative Commons 
"""""
from datetime import date, datetime
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
link_student = config('sinide_data_student')

driver =login(user, password, site) # student in course
os.system("cls")
listNoFind = []
with open("migrate.csv", "r") as f:
    lector = csv.reader(f)
    print("Start data enter")
    driver.get(link_student)
    input("si cargo el site, presione enter")
    for element in lector:
        print("Data to analize: ")
        element = element[0].split(";")
        driver.get(link_student)# Section Student
        time.sleep(2)
        #input("si cargo el site, presione enter \n")
        dni = element[4]
        #dni = dni[2:10]
        selenium_input('//*[@id="id_search"]', dni+"\n")       
        print("Seach to correct Data: " + element[4] +", " +element[3] + "  "+ element[2])
        
        time.sleep(4)
        selenium_Button('//*[@id="page-content"]/div/div/div/sge-table-search/div/div/div[3]/table/tbody/tr/td[9]/span')
        selenium_Button('/html/body/ul/li[1]/a')
        
        time.sleep(2)
        selenium_Button('//*[@id="persona-relacion"]/span')
        
        time.sleep(2)
        cuil = element[11]
        selenium_input('//*[@id="cuil"]', cuil.replace("-","").strip())
        print("Data Tutor: "+element[9] +" "+element[10]+" "+ cuil)
        selenium_Button('/html/body/div[1]/div/div/form/div/div[1]/div[1]/div/div/span/button')        
                
        selenium_Button('//*[@id="nivel-educativo"]/div[1]/span')
        time.sleep(4)
        selenium_Button('//*[@id="ui-select-choices-row-12-4"]/span/span')

        selenium_Button('/html/body/div[1]/div/div/form/div/div[1]/div[4]/input')
        selenium_input('//*[@id="textoLibre"]',element[12])

        now = datetime.now()
        today = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
        selenium_input('//*[@id="fecha_actualizacion_nivel_educativo"]/div/input', today)                
        
        input("Si los datos son correctos presione enter")
        selenium_Button('//*[@id="form-buttons"]/div/button/span')
        #-------------------------------------------------
        time.sleep(3)
        selenium_Button('//*[@id="domicilio-pais"]/div[1]/span')
        time.sleep(2)
        selenium_Button('//*[@id="ui-select-choices-row-13-0"]/span')

        selenium_Button('//*[@id="domicilio-provincia"]/div[1]/span')
        time.sleep(3)
        selenium_Button('//*[@id="ui-select-choices-row-14-16"]/span')

        selenium_Button('//*[@id="domicilio-localidad"]/div[1]/span')
        time.sleep(3)
        selenium_Button('//*[@id="ui-select-choices-row-15-115"]/span')#salta (capital)

        selenium_input('//*[@id="codigo_postal"]',"4400")

        selenium_input('//*[@id="calle"]',element[6]+" "+element[7])
        selenium_input('//*[@id="numero_calle"]',"1")
        #-----------------------------------------------------------------------
        input('Presione enter para continuar la tercera parte')
        selenium_Button('//*[@id="form-buttons"]/div/button/span')
        #enter de email data
        selenium_Button('/html/body/div[1]/div/div/form/div/div[1]/div[2]/input')
        time.sleep(2)
        selenium_input('/html/body/div[1]/div/div/form/div/div[1]/div[3]/input[1]',element[13])
        selenium_input('/html/body/div[1]/div/div/form/div/div[1]/div[3]/input[2]',element[13])

        input("Verificar si los datos son correctos")
        selenium_Button('//*[@id="form-buttons"]/div/button')
        time.sleep(2)
        selenium_Button('//*[@id="form-buttons"]/div/button/span')
        input("Actualizar Datos en el repositorio")
        driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239")
        driver.refresh()
        os.system("cls")
input("press to End") 
print(listNoFind)
with open("listNoFound.csv", "w") as archivo:
    for elemento in listNoFind:
        archivo.write(f"{elemento}\n")

