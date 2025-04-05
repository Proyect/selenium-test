""""" Autor: Ariel Diaz
     https://infrasoft.com.ar/
     Salta Argentina    
     Licence: Creative Commons 
"""""
""" This library uses Selenium"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
def login(user, password, site):
    driver.get(site)
    driver.implicitly_wait(0.3)
    input("presione luego de carga login \n")
    input_element = driver.find_element(By.ID, value="login-usuario")
    input_element.send_keys(user)
    input_element = driver.find_element(By.ID, value="login-contrasenia")
    input_element.send_keys(password)
    button_element = driver.find_element(By.ID, value="login-btn")
    button_element.click()
    print("Done Login.")
    time.sleep(3)
    selenium_Button('//*[@id="page-content-wrapper"]/div/div/div/sge-table-search/div/div/div[3]/table/tbody/tr[1]/td[3]')
    
    time.sleep(3)
    selenium_Button('//*[@id="bs-example-navbar-collapse-1"]/sge-ul-menu-bar-us/ul[1]/li[1]/a/span[3]')
    selenium_Button('//*[@id="bs-example-navbar-collapse-1"]/sge-ul-menu-bar-us/ul[1]/li[1]/ul/li[3]/a')
    print("Start Data Enter Process")
    time.sleep(3)
    return driver

def selenium_input(identify="", value="",by="XPATH"):
     try:
        if(by=="XPATH"): 
            input_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, identify))
            )       
            input_element = driver.find_element(By.XPATH, identify)            
        
        if(by=="ID"):
            input_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, identify))
            ) 
            input_element = driver.find_element(By.ID, identify)            
        
        if(by=="NAME"):
            input_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.NAME, identify))
            )
            input_element = driver.find_element(By.NAME, identify)

        if(by=="CLASS"):
            input_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, identify))
            )
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
            button_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, identify))
            ) 
            button_element = driver.find_element(By.XPATH, identify)
        
        if(by=="ID"):
            button_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, identify))
            )
            button_element = driver.find_element(By.ID, identify)

        if(by=="NAME"):
            button_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.NAME, identify))
            )
            button_element = driver.find_element(By.NAME, identify)
        if(by=="CLASS"):
            button_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, identify))
            )
            button_element = driver.find_element(By.CLASS_NAME, identify)
        button_element.click()
        return True
    except:
        print("Error in "+ identify)
        #input()
        return False