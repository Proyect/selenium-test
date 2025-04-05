""""" Autor: Ariel Diaz     
     Salta Argentina 
     Tel: (+54) 9 387 2204925  
     Licence: Creative Commons 
"""""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import os 
from decouple import config
from basic import *

user = config('ips_user') 
password = config('ips_password')
curso = config('ips_curso')
site = config('ips_link')

def loginIPS(user, password):
    driver.get(site)
    driver.implicitly_wait(0.5)   
    input("presione luego de carga login \n")    
    selenium_input('//*[@id="txtUserName"]', user)
    selenium_input('//*[@id="txtPassword"]', password) 
    time.sleep(1)
    selenium_Button('//*[@id="btnLogin"]')
    return driver

def main():    
    driver = loginIPS(user, password)
    listNoFind = []
    with open("migrate.csv", "r") as f:
        os.system("cls")
        lector = csv.reader(f)
        input("Open the insert data \n")
        selenium_Button('//*[@id="btnNuevaPlanilla"]')
        time.sleep(2)
        selenium_Button('//*[@id="ddlTurnos"]')        
        time.sleep(2)
        selenium_Button('//*[@id="ddlTurnos"]/option[6]')        
        time.sleep(2)
        selenium_Button('//*[@id="btnAgregarPlanilla"]')
        input("presione luego de seleccionar la planilla \n")
        os.system("cls")
        #selenium_Button('//*[@id="ddlTurnos"]/option[6]')
        print("cargando datos: "+ curso)
        time.sleep(2)
        selenium_Button('//*[@id="btnPlanillaDetalle"]')
        time.sleep(2)
        selenium_Button('/html/body/div[2]/div[7]/div/button')       
        for element in lector:
            os.system("cls")
            print("Data to analize: ")
            element = element[0].split(";")
            print("Student: " + element[1]+" "+element[2]+" "+element[3])
            try:
                selenium_input('//*[@id="txtNroDoc"]', element[3])                
                time.sleep(2)
                if(driver.find_element(By.XPATH, '//*[@id="txtCurso"]').get_attribute("value") == ""):
                    selenium_input('//*[@id="txtCurso"]', curso)
                selenium_Button('//*[@id="ddlImporte"]')                
            except:
                listNoFind.append(element)
                print("No find: " + element[3])
            time.sleep(4)
            selenium_Button('//*[@id="btnAgregarFila"]')
            
            #input("Verificar si se agrego el alumno \n")
            os.system("cls")
main()