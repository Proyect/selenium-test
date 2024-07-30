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

user = config('sinide_user')
password = config('sinide_password')
site = config('sinide_url')

def main():
    driver =login(user, password, site)
    os.system("cls")
    input("Presione enter si ingreso al sitio")
    link = config("sinide_date_search")
    driver.get(link)
    time.sleep(5)
    selenium_Button('//*[@id="page-content"]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[6]/div/button')   
    time.sleep(2)
    for element in range(50):
        selenium_Button('/html/body/div[1]/div/div/div/form/div[2]/div[1]/div/div/button')    
        time.sleep(3)       
    input("finished")
main()
