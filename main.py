from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from webscraper import loggingIn, inputDocId

docid = "2395717"
driver = webdriver.Chrome()
driver.get("https://advance.lexis.com/")

#try:
loggingIn(driver)
#except:
    #print("Login failed. Please try again.")
    #driver.quit()

#try:
inputDocId(driver, docid)
#except:
    #print("Failed to input document ID. Please try again.")
    #driver.quit()