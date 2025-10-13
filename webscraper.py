from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def startUp(driver):
    loginIdField = driver.find_element(By.XPATH, '//*[@id="userid"]')
    loginButton1 = driver.find_element(By.XPATH, '//*[@id="signInSbmtBtn"]')
    loginIdField.send_keys(input("Enter your LexisNexis login ID: "))
    loginButton1.click()
    time.sleep(10)
    passwordField = driver.find_element(By.XPATH, '//*[@id="password"]')
    passwordField.send_keys(input("Enter your LexisNexis password: "))
    time.sleep(2)
    loginButton2 = driver.find_element(By.XPATH, '//*[@id="next"]')
    loginButton2.click()
    time.sleep(5)
    productSwitcher = driver.find_element(By.CSS_SELECTOR, 'em.icon.wide')
    productSwitcher.click()
    pgButton = driver.find_element(By.XPATH, '//*[@id="1000522"]')
    pgButton.click()
    driver.find_element(By.CSS_SELECTOR, 'i.icon.la-CloseRemove.close-btn').click()

def inputDocId(driver, docid):
    searchField = driver.find_element(By.XPATH, '//*[@id="searchTerms"]')
    searchField.send_keys(f"docid=0ZHX-0ZHX_{docid}")
    searchButton = driver.find_element(By.CSS_SELECTOR, 'button.icon.la-Search')
    searchButton.click()
    searchResult = driver.find_element(By.CSS_SELECTOR, 'a[data-action="title"]')
    searchResult.click()
    driver.execute_script("document.getElementById('searchTerms').value = '';")




