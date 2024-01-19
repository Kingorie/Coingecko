# Overview
This Python script utilizes Selenium, a browser automation tool, to scrape cryptocurrency data from the Coingecko website. The script extracts information such as coin name, ticker symbol, price, 1-hour change, 24-hour change, 7-day change, 24-hour volume, market cap, and fully diluted valuation. The data is then formatted into a Pandas DataFrame and saved as a CSV file.

# Dependencies
* Selenium: Web automation library for controlling web browsers.
* Pandas: Data manipulation library for creating and manipulating dataframes.
* Datetime: Module for working with dates and times.
* OS: Module for interacting with the operating system.
* Shutil: Module for file operations.

# Code Sections
* Initialization: Import necessary libraries.
* Web Scraping Setup: Set up the Selenium WebDriver to automate the Chrome browser.
* Data Extraction: Extract relevant data from the Coingecko website using XPath expressions.
* Data Processing: Create a Pandas DataFrame from the extracted data and perform some data cleaning.
* Save to CSV: Save the DataFrame to a CSV file with a timestamp in the filename.
* Move File: Optionally, move the generated CSV file to a specified destination folder.

# Notes
* The script uses the Chrome browser, and the pageLoadStrategy capability is set to "none" for faster page interaction.
* The XPath expressions may need adjustments if the structure of the Coingecko website changes.
* Make sure to handle the ChromeDriver path appropriately based on your system configuration.
