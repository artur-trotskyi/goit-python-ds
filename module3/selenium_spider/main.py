# https://www.youtube.com/watch?v=mETRn9gS43M&t=7229s
# не запрацювало (можливо з-за докера)
# відео містить ще багато цікавого контенту

from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("https://www.quotes.toscrape.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    username = driver.find_element(by=By.ID, value='username')
    password = driver.find_element(by=By.ID, value='password')

    username.send_keys('admin')
    password.send_keys('admin')

    button = driver.find_element(by=By.XPATH, value='/html//input[@class="btn btn-primary"]')
    button.click()

    sleep(3)
