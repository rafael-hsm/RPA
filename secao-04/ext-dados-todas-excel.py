from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

import pandas as pd

import pyautogui as auto

dataframe_list = []

browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

browser.get("https://rpachallengeocr.azurewebsites.net/")

line = 1

cont = 1

while cont < 4:
    table = browser.find_element(By.XPATH, '//*[@id="tableSandbox"]')
    lines = table.find_elements(By.TAG_NAME, "tr")
    columns = table.find_elements(By.TAG_NAME, "td")

    for line_actual in lines:
        print(line_actual.text)
        dataframe_list.append(line_actual.text)

        line =+ 1

    cont += 1

    auto.sleep(2)

    # Search button next and click
    browser.find_element(By.XPATH,'//*[@id="tableSandbox_next"]' ).click()
    auto.sleep(2)

else:
    print('Dados Extraidos com sucesso!')


file_excel = pd.ExcelWriter('dados_abas_site.xlsx', engine='xlsxwriter')
file_excel.save()

df = pd.DataFrame(dataframe_list, columns=['Due Date'])
file_excel = pd.ExcelWriter('dados_abas_site.xlsx', engine='xlsxwriter')

df.to_excel(file_excel, sheet_name='dados', index=False)
file_excel.save()