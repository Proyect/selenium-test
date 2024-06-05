""""" Autor: Ariel Diaz
     https://infrasoft.com.ar/
     Salta Argentina    
     Licence: Creative Commons 
"""""
""" This library uses Selenium"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
def login(user, password, site):
    driver.get(site)
    driver.implicitly_wait(0.5)
    input("presione luego de carga login \n")
    input_element = driver.find_element(By.ID, value="login-usuario")
    input_element.send_keys(user)
    input_element = driver.find_element(By.ID, value="login-contrasenia")
    input_element.send_keys(password)
    button_element = driver.find_element(By.ID, value="login-btn")
    button_element.click()
    print("Done Login.")
    print("Start Data Enter Process")
    time.sleep(5)
    return driver

def selenium_input(identify="", value="",by="XPATH"):
     try:
        if(by=="XPATH"):        
            input_element = driver.find_element(By.XPATH, identify)            
        
        if(by=="ID"):
            input_element = driver.find_element(By.ID, identify)            
        
        if(by=="NAME"):
            input_element = driver.find_element(By.NAME, identify)

        if(by=="CLASS"):
            input_element = driver.find_element(By.CLASS_NAME, identify)

        input_element.send_keys(value)
        return True

     except:
        print("Error in "+ identify)
        #input()
        return False

def selenium_Button(identify="",by="XPATH"):
    try:
        if(by=="XPATH"): 
            button_element = driver.find_element(By.XPATH, identify)
        
        if(by=="ID"):
            button_element = driver.find_element(By.ID, identify)

        if(by=="NAME"):
            button_element = driver.find_element(By.NAME, identify)
        button_element.click()
        return True
    except:
        print("Error in "+ identify)
        #input()
        return False