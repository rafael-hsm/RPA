import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.by import By

service_ = EdgeService(EdgeChromiumDriverManager().install())
browser_ = webdriver.Edge(service=service_)

browser_.get("https://business.facebook.com/creatorstudio/home")

time.sleep(4)

browser_.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div/span/div/div/div').click()

time.sleep(2)

print("Finished")
