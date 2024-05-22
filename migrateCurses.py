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

def main():
    driver =login(user, password, site)
    os.system("cls")
    listNoFind = []
    with open("migrate.csv", "r") as f:
        lector = csv.reader(f)
        print("Start data enter")
        driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/organizacionCursada/titulacion/")
        input("si cargo el site, presione enter \n")
        classroom = "https://sge.salta.gob.ar/ui/#!/home/unidad/18239/inscripciones/titulacion/division/29071/titulaciones"
        listStuden = "https://sge.salta.gob.ar/ui/#!/home/unidad/18239/inscripcion/titulacion/29071///titulacionUnidadServicio/145/gradoNivelServicio/21/inscribir"
        driver.get(classroom)
        time.sleep(6)
        selenium_Button('//*[@id="$index"]')
       
        for element in lector:
            os.system("cls")
            print("Data to analize: ")
            element = element[0].split(";")
            driver.get(classroom)# Section Student
            print(classroom+" \n")
            time.sleep(4)

            driver.get(listStuden)
            print("Seach to correct Data: " + element[2] +", " +element[1] + "  "+ element[3])        
            time.sleep(2)

            selenium_input('//*[@id="id_search"]',element[3])          
            time.sleep(2)

            if(not selenium_Button('//*[@id="page-content"]/div/div/div/div/form/table/tbody/tr[1]/td[1]/input')):
                listNoFind.append(element)
                            
            #input("si cargo el site, presione enter \n")
            time.sleep(2)
            selenium_Button('//*[@id="form-buttons"]/div/button')
           
            time.sleep(2)
            selenium_Button('//*[@id="$index"]')  
            selenium_input('//*[@id="repitente"]', "No")
            
            time.sleep(2)       
            selenium_Button('//*[@id="form-buttons"]/div/button/span')
            time.sleep(2)
            selenium_Button('//*[@id="form-buttons"]/div/button/span')
            
    input("press to End") 
    print(listNoFind)
    with open("listNoFound.csv", "w") as archivo:
        for elemento in listNoFind:
            archivo.write(f"{elemento}\n")
main()


        