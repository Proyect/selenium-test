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
import os 
from decouple import config
from basic import *

user = config('linkedin_user') 
password = config('linkedin_password')

def login(user, password):
    loguin_search = config('linkedin_site_login')
    driver.get(loguin_search)
    time.sleep(7)
    print("Done Login.")
    selenium_input('//*[@id="username"]',user)
    selenium_input('//*[@id="password"]',password)
    selenium_Button('/html/body/div/main/div[2]/div[1]/form/div[3]/button')
    print("Start Data Enter Process")    
    return driver

def request():
    selenium_Button('artdeco-button__text', "CLASS")  

def nextRequest():
    selenium_Button('//*[@id="ember1500"]/span') 
    
def finishedRequest():
    selenium_Button('/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')

def main():
    #driver = webdriver.Chrome()
    os.system("cls")   
    driver = login(user,password)
    exit = "0"
    link = config("linkedin_link_serach")
    while (exit != "0"):
        driver.get(link)
        driver.refresh()
        time.sleep(7)
        input("Continue?")
        nextRequest()   
        exit = input("continue in the solicitud ?   \n 1: It's Finished \n 2: If is continues")        
        if(exit == "1"):        
            finishedRequest()

main()
