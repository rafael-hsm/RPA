from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

import pandas as pd


dataframe_list = []

browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

browser.get("https://rpachallengeocr.azurewebsites.net/")

table = browser.find_element(By.XPATH, '//*[@id="tableSandbox"]')

lines = table.find_elements(By.TAG_NAME, "tr")
columns = table.find_elements(By.TAG_NAME, "td")

cont = 1
for line in lines:
    print(line.text)
    dataframe_list.append(line.text)
    cont +=1

file_excel = pd.ExcelWriter('data_site.xlsx', engine='xlsxwriter')

df = pd.DataFrame(dataframe_list, columns=['Date Invoice'])

# Prepara o arquivo do Excel usando xlsxwriter como mecanismo
file_excel = pd.ExcelWriter('data_site.xlsx', engine='xlsxwriter')

df.to_excel(file_excel, sheet_name='Sheet 01', index=True)

file_excel.save()
