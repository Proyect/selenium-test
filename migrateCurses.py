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
from basic import login

driver =login("27146440946","SGE27146440946","https://sge.salta.gob.ar/ui/#!/login")
os.system("cls")
listNoFind = []
with open("migrate.csv", "r") as f:
    lector = csv.reader(f)
    print("Start data enter")
    driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/organizacionCursada/titulacion/")
    input("si cargo el site, presione enter \n")
    classroom = "https://sge.salta.gob.ar/ui/#!/home/unidad/18239/inscripciones/titulacion/division/29069/titulaciones"
    listStuden = "https://sge.salta.gob.ar/ui/#!/home/unidad/18239/inscripcion/titulacion/29069///titulacionUnidadServicio/145/gradoNivelServicio/23/inscribir"
    driver.get(classroom)
    time.sleep(6)
    button_element = driver.find_element(By.XPATH,'//*[@id="$index"]')    
    button_element.click()
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
        try:
            input_element = driver.find_element(By.XPATH, '//*[@id="id_search"]')
            input_element.send_keys(element[3])
        except:
            print("id_search no encontrado")
        
        time.sleep(2)
        try:
            input_element = driver.find_element(By.XPATH, '//*[@id="page-content"]/div/div/div/div/form/table/tbody/tr[1]/td[1]/input')
            input_element.click()                                                                     
        except:
            print("Element no find")
            listNoFind.append(element)
        #input("si cargo el site, presione enter \n")
        time.sleep(2)
        button_element = driver.find_element(By.XPATH,'//*[@id="form-buttons"]/div/button')
        button_element.click()
        time.sleep(2)  
        try:
            button_element = driver.find_element(By.XPATH,'//*[@id="$index"]')    
            button_element.click()
            input_element = driver.find_element(By.XPATH, '//*[@id="repitente"]')
            input_element.send_keys("No")
        except:
            pass
        time.sleep(2)       
        #confirm
        try:
            button_element = driver.find_element(By.XPATH,'//*[@id="form-buttons"]/div/button/span')
            button_element.click()
            time.sleep(2)
            button_element = driver.find_element(By.XPATH,'//*[@id="form-buttons"]/div/button/span')
            button_element.click()
        except:
            print("btn no encontrados")
input("press to End") 
print(listNoFind)
with open("listNoFound.csv", "w") as archivo:
    for elemento in listNoFind:
        archivo.write(f"{elemento}\n")



        