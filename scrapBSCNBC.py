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
        url = "https://www.cnbcindonesia.com/search?query=energy"
        driver =webdriver.Chrome()
        driver.get(url)


        for loadButton in range(1):
            WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".terbaru")))
            time.sleep(2)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        #beautifulsoup for locator
        products=[]
        for item in soup.find_all('a', href=True):
            link = item['href']
            
            products.append(
                (link)
            )

        #dataframe 
        df = pd.DataFrame(products, columns=['LINK'])

        # Save to Excel
        df.to_excel("cnbc.xlsx","Iphone",index=False)
        print("Dataframe is written to excel file sucessfully")


        driver.close()

sl = ScrapeOLX()
sl.scrape()