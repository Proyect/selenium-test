""""" Autor: Ariel Diaz
     https://infrasoft.com.ar/
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
# vbles

site = config('progresar_site')
city = config('progresar_city')
school = config('progresar_col')
password = config('progresar_password')

driver = webdriver.Chrome()

def loginProg(site, city, school, password):
    driver.get(site)
    driver.implicitly_wait(0.5)
    input("presione luego de carga login \n")
    input_element = driver.find_element(By.ID, value="provincia")
    input_element.send_keys(city)
    driver.implicitly_wait(1)
    input_element = driver.find_element(By.XPATH, '//*[@id="establecimiento"]/option[89]')
    input_element.click()
    input_element = driver.find_element(By.ID, value="clave")
    input_element.send_keys(password)
    time.sleep(1)
    button_element = driver.find_element(By.XPATH,'/html/body/div/form/div/div[4]/div/button')
    button_element.click()

def main():    
    loginProg(site, city, school, password)
    with open("migrate.csv", "r") as f:
        os.system("cls")
        lector = csv.reader(f)
        print("Open the insert data \n")
        button_element = driver.find_element(By.XPATH,'//*[@id="navbarCollapse"]/ul/li[2]/a')    
        button_element.click()
        driver.implicitly_wait(1)
        button_element = driver.find_element(By.XPATH,'//*[@id="navbarCollapse"]/ul/li[2]/ul/li/a')    
        button_element.click()
        time.sleep(1)
        
        for element in lector:
            os.system("cls")
            print("Data to analize: ")
            element = element[0].split(";")
            print("Student: " + element[1]+" "+element[2]+" "+element[0])
            try:
                input_element = driver.find_element(By.XPATH, '//*[@id="renovantes_filter"]/label/input')
                input_element.send_keys(element[0])                
                val = driver.find_element(By.NAME, 'cuit[]').get_attribute("value")
                   
            except:
                print("No se pudo cargar el DNI")
            time.sleep(1)
            try:                               
                input_element = driver.find_element(By.XPATH, '//*[@id="es_alumno_regular'+val+'"]/option[2]')
                input_element.click()
                
            except:
                print("Error en la admicion de progresar")             

            button_element = driver.find_element(By.XPATH,'//*[@id="Form2"]/center/button')    
            button_element.click()
            time.sleep(1) 
            try:
                input_element = driver.find_element(By.XPATH, '/html/body/div/div/h2/a')
                input_element.click()
            except:
                input_element = driver.find_element(By.XPATH, '/html/body/div/a')
                input_element.click()
            
main()