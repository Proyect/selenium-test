""""" Autor: Ariel Diaz
     https://infrasoft.com.ar/
     Salta Argentina 
     Tel: (+549) 3872204925  
     Licence: Creative Commons 
"""""

from selenium import webdriver
from selenium.webdriver.common.by import By
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
    time.sleep(5)
    listNoCUIL = [] 
    listNoFind = []
    time.sleep(5)
    os.system("cls")
    # Abre el archivo CSV
    with open("list.csv", "r") as f:
        lector = csv.reader(f)
        print("Start data enter")
        for element in lector:
            print("Data to analize: ")
            element = element[0].split(";")
            #print(element)
            if(len(element[3])==11):# correct cuil 
                print("Seach to correct Data: " + element[2] +", " +element[1] + "  "+ element[3])
                driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/search///")
                print("Ingresando a https://sge.salta.gob.ar/ui/#!/home/unidad/18239/search///")
                input("si cargo el site, presione enter")
                selenium_input("persona-busqueda-input",element[3],"ID")                        
                selenium_Button("persona-busqueda-buscar","ID")   

                ops = input("Ingrese: 1: si existe en la carga. 2: si requiere carga manual")
                if(ops =="1"):
                    selenium_Button("clickable","CLASS_NAME")
                else:
                    driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/usuario/ ")
                    print("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/usuario/ ")
                    input("Presione enter cuando cargue el site")
                    
                    selenium_input("apellido", element[1], "ID")
                    selenium_input("nombre", element[2],"ID")
                    selenium_input('//*[@id="tipo_documento"]/input[1]', "DNI")
                    selenium_input("nro_documento", element[12], "ID")
                    selenium_input("cuil", element[3], "ID")
                    selenium_input("fechaNacimientoInput", element[4], "NAME")
                    selenium_input("email", element[11], "NAME")
                    selenium_input("password", "SGE"+element[3], "NAME")
                    selenium_input("confirmation_password", "SGE"+element[3],"NAME")
                    input("esperando")

                # carga de materias
                print("Ingresando: https://sge.salta.gob.ar/ui/#!/home/unidad/18239/roles-gestion/"+element[3])
                driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/roles-gestion/"+element[3])
                time.sleep(5)
                input("PRESIONE ENTER SI SE CARGO EL SITIO")
                selenium_Button('//*[@id="page-content"]/div/div/div/roles-seleccion/div[2]/div[5]/sge-card/div/div/card-header/span')
                input("ingrese enter al terminar la carga del site")
                selenium_Button('//*[@id="page-content"]/div/div/div/roles-seccion-curricular/sge-select-lists/div[2]/div[1]/div[2]/ul/li[1]/a')
                selenium_Button('//*[@id="page-content"]/div/div/div/roles-seccion-curricular/sge-select-lists/div[2]/div[2]/div/button[1]/span')
                selenium_Button('//*[@id="page-content"]/div/div/div/roles-seccion-curricular/form-buttons/div/button/span')  
                input("Siguiente Elemento ?")
            else: #bad Cuil
                listNoCUIL.append(element)
                print("Cuil No correct")
    input("press to End") 
##driver.quit() SGE + cuil