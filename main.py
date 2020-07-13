# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 00:25:53 2020

@author: SEVVAL
"""
from selenium import webdriver
import time #  web sayfasının kaç sn aktif kalmasını istiyorsak
import csv

kilometre = []
model = []
year = []
yakit = []
vites = []
price = []
browser = webdriver.Firefox()
url ="********,sayfa=0"



for i in range(1,66):  # sayfa sayisi
    newUrl = url+str(i)
    browser.get(newUrl)
    divCount=1
    fiyat=browser.find_elements_by_css_selector(".ok-spcrlclb-price")
    vites_tur=browser.find_elements_by_xpath("/html/body/div[3]/div/div[3]/div/div[2]/div/div/div['divCount']/div/a/div[3]/div/div[8]")
    yakit_tur=browser.find_elements_by_xpath("/html/body/div[3]/div/div[3]/div/div[2]/div/div/div['divCount']/div/a/div[3]/div/div[6]")
    yil=browser.find_elements_by_xpath("/html/body/div[3]/div/div[3]/div/div[2]/div/div/div['divCount']/div/a/div[3]/div/div[2]")
    models=browser.find_elements_by_xpath("/html/body/div[3]/div/div[3]/div/div[2]/div/div/div['divCount']/div/a/div[2]")
    km=browser.find_elements_by_xpath("/html/body/div[3]/div/div[3]/div/div[2]/div/div/div['divCount']/div/a/div[3]/div/div[4]")
    for element in km:
        kilometre.append(element.text)
            #time.sleep(1)
    for mod_el in models:
        model.append(mod_el.text)
   
    for years in yil:
        year.append(years.text)   
        
    for yakit_turu in yakit_tur:
        yakit.append(yakit_turu.text)
        
    for vites_turu in vites_tur:
        vites.append(vites_turu.text)  
       
    for fiyati in fiyat:
        price.append(fiyati.text)        
        divCount+=1

       
browser.close() 
    
#%%  Verilerden csv dosyası oluşturuldu
import pandas as pd
df_yeni = pd.DataFrame({'Model':model,'Kilometre':kilometre,'Yil':year,'Yakıt tur':yakit,'Vites':vites,'Price':price}) 

df_yeni.to_csv('arac_tahmin.csv', index=False, encoding='utf-8')
data_yeni=pd.read_csv("arac_tahmin.csv")
