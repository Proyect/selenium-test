""""" Autor: Ariel Diaz
     https://infrasoft.com.ar/
     Salta Argentina    
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

with open("migrate.csv", "r") as f:
    lector = csv.reader(f)
    print("Start data enter")
    driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/alumnos")
    input("si cargo el site, presione enter")
    for element in lector:
        print("Data to analize: ")
        element = element[0].split(";")
        driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/alumnos")# Section Student
        print("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/alumnos \n")
        
        input("si cargo el site, presione enter")
        input_element = driver.find_element(By.ID, value="id_search")
        input_element.send_keys(element[3])
        button_element = driver.find_element(By.ID, value="agregar_alumno_btn")
        button_element.click()
        print("Seach to correct Data: " + element[2] +", " +element[1] + "  "+ element[3])
        input_element = driver.find_element(By.ID, value="persona-busqueda-input")
        input_element.send_keys(element[3])
        button_element = driver.find_element(By.ID, value="persona-busqueda-buscar")
        button_element.click()

        ops = input("Ingrese: 1: si es la persona correcta. 2: si requiere verificacion de datos \n")
        if(ops == "1"):
            button_element = driver.find_element(By.XPATH,'//*[@id="table-buscar"]/table/tbody/tr/td[8]/a/span')
            button_element.click()
            time.sleep(6)
            button_element = driver.find_element(By.XPATH,'//*[@id="form-buttons"]/div/button/span')
            button_element.click()
        else:
            button_element = driver.find_element(By.XPATH,'//*[@id="closeSearchModal"]/span')
            button_element.click()
input("press to End") 
