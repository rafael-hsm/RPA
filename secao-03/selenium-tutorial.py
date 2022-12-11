import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.by import By

service_ = EdgeService(EdgeChromiumDriverManager().install())
browser_ = webdriver.Edge(service=service_)

browser_.get("https://google.com")

browser_.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Ernst & Young")

time.sleep(2)

print("Finished")
