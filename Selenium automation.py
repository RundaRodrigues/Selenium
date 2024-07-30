from selenium import webdriver
import time

driver = webdriver.Firefox()


driver.get('https://youtube.com.br')


print(driver.title)