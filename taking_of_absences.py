""""" Autor: Ariel Diaz
     https://infrasoft.com.ar/
     Salta Argentina 
     Tel: (+549) 387 220 49 25  
     Licence: Creative Commons 
"""""
from selenium import webdriver
from selenium.webdriver.common.by import By

from decouple import config
from basic import *
import os 

user = "20182306070" #config('sinide_user')
password =  "SGE20182306070"    #config('sinide_password')
site =  "https://sge.salta.gob.ar/ui/#!/login" #config('sinide_url')

def main():
    driver =login(user, password, site)
    os.system("cls")
    link = "https://sge.salta.gob.ar/ui/#!/home/unidad/18239/tomar-asistencia/Todas/29053//" #config("sinide_date_search")
    link2 = "https://sge.salta.gob.ar/ui/#!/home/unidad/18239/tomar-asistencia/Todas/29054//" #config("sinide_date_search2")
    link3 = "https://sge.salta.gob.ar/ui/#!/home/unidad/18239/tomar-asistencia/Todas/29055//" #config("sinide_date_search3")
    link_group = [link, link2, link3]
    for i in link_group:
        input("Presione enter si ingreso al sitio")    
        driver.get(i)
        time.sleep(5)
        if(selenium_Button('//*[@id="page-content"]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[5]/div/button')):
            time.sleep(2)
        else:
            input("haga click en el primer alumno a tomar asistencia")
        for element in range(50):
            if(selenium_Button('/html/body/div[1]/div/div/div/form/div[2]/div[1]/div/div/button')):#
                time.sleep(2)       
            else:
                break

        opt = input("Presione Enter para grabar y continuar con el siguiente curso \n Presione 1 y Enter para salir del programa")
        if(opt =="1"):
            break
main()
