import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.olx.co.id/jakarta-selatan_g4000030/q-iphone")
time.sleep(5)
#Judul
#container > main > div > div > section > div > div > div:nth-child(6) > div._2CyHG > div > div:nth-child(2) > ul > li > a > div > span._2poNJ
#container > main > div > div > section > div > div > div:nth-child(6) > div._2CyHG > div > div:nth-child(2) > ul > li > a > div > span._2Ks63

#Load more button
#container > main > div > div > section > div > div > div:nth-child(6) > div._2CyHG > div > div:nth-child(2) > ul > li.TA_b7 > div > button


while True:
    try:
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"main > div > div > section > div > div > div:nth-child(6) > div._2CyHG > div > div:nth-child(2) > ul > li.TA_b7 > div > button"))).click()
        time.sleep(2)
    except Exception as e:
        print(e)
        break


iphone=[]
row = driver.find_elements(By.CSS_SELECTOR,"main > div > div > section > div > div > div:nth-child(6) > div._2CyHG > div > div:nth-child(2) > ul > li > a > div")
for data in row:
    judul=data.find_element(By.CSS_SELECTOR,"span._2poNJ").text
    harga=data.find_element(By.CSS_SELECTOR,"span._2Ks63").text
    
    dt_olx = {
        "JUDUL":judul,
        "HARGA":harga
    }

    iphone.append(dt_olx)

#buat data frame
df = pd.DataFrame(iphone)
print(df)

# Save to Excel
df.to_excel("Iphone OLX.xlsx","Iphone",index=False)
print("Dataframe is written to excel file sucessfully")
time.sleep(30)