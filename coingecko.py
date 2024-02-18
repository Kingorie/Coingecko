#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import datetime
import shutil
import os

# Create ChromeOptions instance
chrome_options = Options() 
# Add any desired capabilities to chrome_options here

# Provide the correct path to chromedriver
chrome_path = '/Users/kingori/Downloads/chromedriver'

# Create a ChromeService instance
chrome_service = ChromeService(executable_path=chrome_path)

# Pass the service instance to the webdriver.Chrome constructor
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

try:
    result = []

    for i in range(1, 4):
        # Navigate to the specified URL
        driver.get("https://www.coingecko.com/?page=%s" % i)

        # Set a maximum wait time of 10 seconds
        wait = WebDriverWait(driver, 10)

        # Find and print the names of the coins on the page within a maximum of 10 seconds
        coin_names = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//tbody/tr/td[3]')))

        n = driver.find_elements('xpath', '//tbody/tr/td[2]')
        Coin = driver.find_elements('xpath', '//tbody/tr/td[3]')
        Ticker = driver.find_elements('xpath',
                                      '//tbody/tr/td[3]/a/div/div/div')
        Price = driver.find_elements('xpath', '//tbody/tr/td[5]')
        H1 = driver.find_elements('xpath', "//tbody/tr/td[6]/span")
        H24 = driver.find_elements('xpath', '//tbody/tr/td[7]/span')
        d7 = driver.find_elements('xpath', '//tbody/tr/td[8]')
        Vol = driver.find_elements('xpath', '//tbody/tr/td[10]/span')
        Mkt_cap = driver.find_elements('xpath', '//tbody/tr/td[11]/span')
        FDV = driver.find_elements('xpath', '//tr/td[10]')

        for i in range(len(Coin)):
            data = {
                '#': n[i].text,
                'Coin': Coin[i].text,
                'Ticker': Ticker[i].text,
                'Price': Price[i].text,
                '1h': H1[i].text,
                '24h': H24[i].text,
                '7d': d7[i].text,
                '24h Volume': Vol[i].text,
                'Mkt Cap': Mkt_cap[i].text,
                'Fully Diluted Valuation': FDV[i].text
            }

            result.append(data)

    # Create a DataFrame from the collected data
    df = pd.DataFrame(result)

    # Save the DataFrame to a single Excel file
    e = datetime.datetime.now()
    date_string = e.strftime("%Y%m%d %H-%M-%S")
    date_string2 = e.strftime("%Y-%m-%d")
    df.to_excel(f"coingecko_{date_string}.xlsx",
                sheet_name=date_string2,
                index=False)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.close()


# In[2]:


# Create a 'reports' folder and move the excel files there

# create folder named reports
directory = 'reports'

try:
    os.makedirs(directory)
except:
    pass


# In[3]:


# move the excel files to 'reports' folder

source_path = os.getcwd()
dest_path = os.getcwd() + '/' + directory


# Loop through the files in the current directory
for file in os.listdir(source_path):
    if file.endswith('.xlsx'):
        # Build the source and destination file paths
        source_file = os.path.join(source_path, file)
        dest_file = os.path.join(dest_path, file)

        # Move the file to the 'reports' folder
        shutil.move(source_file, dest_file)

