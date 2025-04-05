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

site = config('progresar_site')
city = config('progresar_city')
school = config('progresar_col')
password = config('progresar_password')


def loginProg(site, city, school, password):
    driver.get(site)
    driver.implicitly_wait(0.5)   
    input("presione luego de carga login \n")    
    selenium_input("provincia", city, "ID")
    driver.implicitly_wait(1)
    selenium_Button('//*[@id="establecimiento"]/option[89]')
    selenium_input("clave", password, "ID") 
    time.sleep(1)
    selenium_Button('/html/body/div/form/div/div[4]/div/button')
    return driver

def main():    
    driver = loginProg(site, city, school, password)
    listNoFind = []
    with open("migrate.csv", "r") as f:
        os.system("cls")
        lector = csv.reader(f)
        input("Open the insert data \n")
        selenium_Button('//*[@id="navbarCollapse"]/ul/li[2]/a')
        time.sleep(2)
        selenium_Button('//*[@id="navbarCollapse"]/ul/li[2]/ul/li[5]/a')        
        time.sleep(2)
        
        for element in lector:
            os.system("cls")
            print("Data to analize: ")
            element = element[0].split(";")
            print("Student: " + element[1]+" "+element[2])
            try:
                input_element = driver.find_element(By.XPATH, '//*[@id="renovantes_filter"]/label/input')
                dni = element[0]
                #dni = dni[2:10]
                input_element.send_keys(dni)                
                val = driver.find_element(By.NAME, 'cuit[]').get_attribute("value")

                selenium_Button('//*[@id="nivel_educativo_03'+val+'"]') 
                selenium_Button('//*[@id="nivel_educativo_03'+val+'"]/option[2]')
                time.sleep(1)

                selenium_Button('//*[@id="finalizo_alumno_regular_03'+val+'"]')
                selenium_Button('//*[@id="finalizo_alumno_regular_03'+val+'"]/option[2]')
                time.sleep(1)
                
                selenium_Button('//*[@id="anio_curso_03'+val+'"]')
                curso = str(int (element[2])+1)
                selenium_Button('//*[@id="anio_curso_03'+val+'"]/option['+curso+']')
                time.sleep(1)
                
                selenium_Button('//*[@id="en_que_nivel_03'+val+'"]')
                if(element[2] >2):
                    selenium_Button('//*[@id="en_que_nivel_03'+val+'"]/option[5]') 
                else:
                    selenium_Button('//*[@id="en_que_nivel_03'+val+'"]/option[6]')           
                time.sleep(2)                
                
                selenium_Button('//*[@id="curso_ultimo_anio_este_anio_03'+val+'"]')
                if(element[2]==5):
                    selenium_Button('//*[@id="curso_ultimo_anio_este_anio_03'+val+'"]/option[2]')
                    time.sleep(1)
                    selenium_Button('//*[@id="egreso_sin_adeudar_03'+val+'"]')
                    selenium_Button('//*[@id="egreso_sin_adeudar_03'+val+'"]/option[2]')
                else:
                    selenium_Button('//*[@id="curso_ultimo_anio_este_anio_03'+val+'"]/option[3]')                    
                time.sleep(2)                
                
            except:
                print("No se pudo cargar el DNI")
                listNoFind.append(element)
            time.sleep(1)                                  
            input("Valores correctamente cargados?")
            selenium_Button('//*[@id="Form2"]/center/button')            
            time.sleep(1)
            selenium_Button('/html/body/div/div/h2/a') 
            selenium_Button('/html/body/div/a')            
            
    print(listNoFind)
    with open("listNoFound.csv", "w") as archivo:
        for elemento in listNoFind:
            archivo.write(f"{elemento}\n")
main()
