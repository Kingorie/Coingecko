# %%
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import pandas as pd
import time

# %% [markdown]
# # Webdriver to automate browser
# ''' 
# WebDriverManager.chromedriver().setup();
# WebDriver driver = new ChromeDriver();
# driver.get("http://google.com");  
#  '''
#    
# #driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
# driver = webdriver.Chrome('/Users/kingori/Downloads/chromedriver')
# page = 1
# url = f"https://www.coingecko.com/?page={page}"
# driver.get(url)
# 

# %%
page = 1

for i in range(3,7):
    #driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
    driver = webdriver.Chrome('/Users/kingori/Downloads/chromedriver')
    url = f"https://www.coingecko.com/?page={i}"
    driver.get(url)
    
    # Click button: Show Fully Diluted Valuation
    button = driver.find_element('xpath', '//body/div[4]/div[4]/div[2]/div[2]/div/button')
    # clicking on the button
    button.click()

    # maximize window position
    driver.maximize_window
    
    # Get the following columns from table

    # Coin
    # Price
    # 1h
    # 24h
    # 7d
    # 24h Volume
    # Mkt Cap
    # FDV


    Coin = driver.find_elements('xpath', '//tbody/tr/td[3]/div/div[2]/a[1]/span[1]')
    Ticker = driver.find_elements('xpath', '//tbody/tr/td[3]/div/div[2]/a[1]/span[2]')
    Price = driver.find_elements('xpath', '//tr/td[4]/div/div[2]')
    H1 = driver.find_elements('xpath', "//tr/td[5]")
    H24 = driver.find_elements('xpath', '//tr/td[6]')
    d7 = driver.find_elements('xpath', '//tr/td[7]')
    Vol = driver.find_elements('xpath', '//tr/td[8]/span[1]')
    Mkt_cap = driver.find_elements('xpath', '//tr/td[9]/span')
    FDV = driver.find_elements('xpath', '//tr/td[10]')
    
    # Loop over all lists and get text elements:

    result = []

    for i in range(len(Vol)):
        data = {
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
        
        df = pd.DataFrame(result)

    #Remove $ and commas from column names
    columns = ['Price', '24h Volume', 'Mkt Cap']
    for col in columns:
        df[col] = df[col].str.replace('$','')
        df[col] = df[col].str.replace(',',"").astype(float)

    columns = ['Fully Diluted Valuation']
    for col in columns:
        df[col] = df[col].str.replace('$',"")
        df[col] = df[col].str.replace('-',"0")
        df[col] = df[col].str.replace(',',"").astype(float)
        
    df
    
    # Insert date to filename
    import datetime
    date_string = datetime.datetime.now().strftime("%Y%m%d %H-%M-%S")
    #file = ('%s%s.xlsx' % ("coingecko_", datestring) )
    #file = ("coingecko_"f"{datestring}{_page}.csv")
    file_name = (f"report_{date_string}_{page}.csv")

    # Save dataframe to CSV file
    df.to_csv(file_name, index=0)
    
    # Close web driver
    driver.close()
 
    

# %%
# Merge file

folder = '/Users/kingori/Library/CloudStorage/GoogleDrive-kingori.ek@gmail.com/My Drive/Documents/Github/Coingecko'



#csv_files = [file for file in os.listdir(folder) if file.endswith('.csv')]
csv_files = []

for file in os.listdir(folder):
    if file.endswith('.csv'):
        csv_files.append(file)

with open(f'coingecko_{date_string}.csv', 'w') as f:
    for file in csv_files:
        file_path = os.path.join(folder, file)
        with open(file_path, 'r') as infile:
            f.write(infile.read())
            

csv_files


# %%
# Remove duplicate headers fom the merged file using CSV library

import csv

filename = f"coingecko_{date_string}.csv"

# Read csv file
with open(filename, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
# Create set to store unique rows
unique_rows = set()
# Iterate through the rows, adding each row to the set only if it's not already in it
unique_data = []
for row in data:
    if tuple(row) not in unique_rows:
        unique_data.append(row)
        unique_rows.add(tuple(row))

# Write unique data to a new CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(unique_data)

# %%

import os
import shutil

# Source and destination folder
src_folder = '/Users/kingori/Library/CloudStorage/GoogleDrive-kingori.ek@gmail.com/My Drive/Documents/Github/Coingecko/'
dest_folder = '/Users/kingori/Library/CloudStorage/GoogleDrive-kingori.ek@gmail.com/My Drive/Documents/Github/Coingecko/Reports/'

# Iterate through source folder
for file in os.listdir(src_folder):
    # check if file is an excel
    if file.endswith('.csv') and file.startswith('coingecko'):
        # Build full path of files
        src_file = os.path.join(src_folder, file)
        dest_file = os.path.join(dest_folder, file)
        # move file to dest folder 
        shutil.move(src_file, dest_folder)
    
print(src_file)

# %%
import glob

# Find all csv files using glob.glob() function 
csv_files = glob.glob(f"{src_folder}*.csv")
for file in csv_files:
    os.remove(file)

# %%



