from openpyxl import load_workbook

import pyautogui as auto

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By


database = "C:\\Users\\rafam\\Projects\\RPA\\RPA\\Desafio\\challenge.xlsx"
dtb = load_workbook(database)

# Select sheet with information
sheet = dtb["Sheet1"]


# Starting and acessing website
browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

browser.get("https://www.rpachallenge.com/")
auto.sleep(2)

# Find elements and send the text
# //*[@] to search the item
for line in range(2, len(sheet['A']), +1):         

    # First name
    first_name = sheet["A%s" % line].value

    browser.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(first_name)
    # Last name
    auto.sleep(1)
    last_name = sheet["B%s" % line].value
    browser.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(last_name)

    # Company Name
    auto.sleep(1)
    company_name = sheet["C%s" % line].value
    browser.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys(company_name)

    # Address
    auto.sleep(1)
    address = sheet["E%s" % line].value
    browser.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys(address)

    # Role
    auto.sleep(1)
    role = sheet["D%s" %line].value
    browser.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys(role)

    # E-mail
    auto.sleep(1)
    email = sheet["F%s" %line].value
    browser.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys(email)

    # Phone
    auto.sleep(1)
    phone = sheet["G%s" %line].value
    browser.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(phone)

    auto.sleep(1)
    # Click on submmit button
    browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input").click()

    auto.sleep(1)

    print("Data successfully send.")
