import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service

class ScrapeOLX():

    def scrape(self):
        url = "https://www.olx.co.id/jakarta-selatan_g4000030/q-iphone-11"
        driver =webdriver.Chrome()
        driver.get(url)


        while True:
            try:
                WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#app")))
                WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"main > div > div > section > div > div > div:nth-child(6) > div._2CyHG > div > div:nth-child(2) > ul > li.TA_b7 > div > button"))).click()
                time.sleep(2)
            except Exception as e:
                print(e)
                break

        # for loadButton in range():
        #     WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#app")))
        #     WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"main > div > div > section > div > div > div:nth-child(6) > div._2CyHG > div > div:nth-child(2) > ul > li.TA_b7 > div > button"))).click()
        #     time.sleep(2)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        #beautifulsoup for locator
        products=[]
        for item in soup.findAll('li', class_='_1DNjI'):
            product_name = item.find('span', class_='_2poNJ').text
            price = item.find('span', class_='_2Ks63').text
            location = item.find('span', class_='_2VQu4').text
            
            products.append(
                (product_name, price,location)
            )

        #dataframe 
        df = pd.DataFrame(products, columns=['NAME','PRICE','LOCATION'])

        # Save to Excel
        df.to_excel("Iphone 11 OLX bs4.xlsx","Iphone 11",index=False)
        print("Dataframe is written to excel file sucessfully")


        driver.close()

sl = ScrapeOLX()
sl.scrape()