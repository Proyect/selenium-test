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
dniNoFound = []
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
        #print("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/alumnos \n")
        time.sleep(4)
        #input("si cargo el site, presione enter \n")
        try:
            input_element = driver.find_element(By.ID, value="id_search")
            input_element.send_keys(element[3])
            button_element = driver.find_element(By.ID, value="agregar_alumno_btn")
            button_element.click()
        except:
            print("Error en la busqueda")
        print("Seach to correct Data: " + element[2] +", " +element[1] + "  "+ element[3])
        try:
            input_element = driver.find_element(By.ID, value="persona-busqueda-input")
            input_element.send_keys(element[3])
            button_element = driver.find_element(By.ID, value="persona-busqueda-buscar")
            button_element.click()
        except:
            print("Error en busqueda avanzada")

        ops = input("Ingrese: 1: si es la persona correcta. 2: si requiere verificacion de datos \n")
        if(ops == "1"):
            button_element = driver.find_element(By.XPATH,'//*[@id="table-buscar"]/table/tbody/tr/td[8]/a/span')
            button_element.click()
            time.sleep(6)
            try:
                input_element = driver.find_element(By.XPATH, '//*[@id="provincia_nacimiento"]/div[1]/span')
                input_element.send_keys("Salta")
            except:
                print("No se pudo cambiar provincia")
            try:
                if(element[10]=="M"):
                    input_element = driver.find_element(By.XPATH, '//*[@id="sexo"]/div[1]/span/span[2]/span')
                    input_element.send_keys("Masculino")
                else: 
                    input_element = driver.find_element(By.XPATH, '//*[@id="sexo"]/div[1]/span/span[2]/span')
                    input_element.send_keys("Femenino")
            except:
                print("No se pudo cambiar el sexo")
            input("presione enter si los datos son correctos")
            button_element = driver.find_element(By.XPATH,'//*[@id="form-buttons"]/div/button/span')
            button_element.click()
        elif(ops=="2"):
            button_element = driver.find_element(By.XPATH,'//*[@id="closeSearchModal"]/span')
            button_element.click()
        else:
            pass
input("press to End") 
print(dniNoFound)
with open("listNoFound.csv", "w") as archivo:
    for elemento in dniNoFound:
        archivo.write(f"{elemento}\n")