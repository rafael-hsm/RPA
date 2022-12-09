import pandas as pd

import pyautogui as auto

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By

from webdriver_manager.microsoft import EdgeChromiumDriverManager


browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

browser.get("https://www.magazineluiza.com.br/")

browser.find_element(By.ID, 'input-search').send_keys('Notebook')

auto.sleep(2)

auto.press("enter")

auto.sleep(5)

list_products = browser.find_elements(By.CLASS_NAME, "hYPKVt")

for item in list_products:
    name = ""
    price = ""
    url = ""

    if name == "":
        try:
            name = item.find_element(By.CLASS_NAME, "sc-hhOBVt").text
        except Exception:
            pass
    elif price == "":
        try:
            name = item.find_element(By.CLASS_NAME, "fslCuc").text
        except Exception:
            pass
    
    print(name)
