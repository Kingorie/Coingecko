#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd


# In[ ]:


# Webdriver to automate browser

#driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
driver = webdriver.Chrome()
driver.get('https://coingecko.com')

# Click button: Show Fully Diluted Valuation
button = driver.find_element(
    'xpath', '//body[1]/div[4]/div[4]/div[2]/div[2]/div[1]/button[1]')
# clicking on the button
button.click()

# maximize window position
driver.maximize_window


# In[ ]:


# Get the following columns from table

# Coin
# Price
# 1h
# 24h
# 7d
# 24h Volume
# Mkt Cap
# FDV


Coin = driver.find_elements('xpath', '//tbody/tr/td[3]')
Price = driver.find_elements('xpath', '//tr/td[4]/div/div[2]')
H1 = driver.find_elements('xpath', "//tr/td[5]")
H24 = driver.find_elements('xpath', '//tr/td[6]')
d7 = driver.find_elements('xpath', '//tr/td[7]')
Vol = driver.find_elements('xpath', '//tr/td[8]/span')
Mkt_cap = driver.find_elements('xpath', '//tr/td[9]/span')
FDV = driver.find_elements('xpath', '//tr/td[10]')


# Check if code works:


# # Check if code works
# 
# print(len(FDV))
# 
# for n in FDV:
#     print(n.text)

# In[ ]:


# Loop over all lists and get text elements:

result = []

for i in range(len(Coin)):
    data = {
        'Coin': Coin[i].text,
        'Price': Price[i].text,
        '1h': H1[i].text,
        '24h': H24[i].text,
        '7d': d7[i].text,
        '24h Volume': Vol[i].text,
        'Mkt Cap': Mkt_cap[i].text,
        'Fully Diluted Valuation': FDV[i].text


    }

    result.append(data)


# In[ ]:


df = pd.DataFrame(result)
df


# In[ ]:


df.to_excel('Coingecko.xlsx', index=False)


# In[ ]:


driver.close()

