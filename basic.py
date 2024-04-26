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
    input("presione luego de carga login")
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