from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Abrindo site
browser.get("https://rpachallengeocr.azurewebsites.net/")

table = browser.find_element(By.XPATH, '//*[@id="tableSandbox"]')

lines = table.find_elements(By.TAG_NAME, "tr") # each line == tr
columns = table.find_elements(By.TAG_NAME, "td") # each columns == td

line = 1

for i in lines:
    print(i.text)
    line += 1