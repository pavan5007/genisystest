import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def login_existing_user(username,password):
    driver_obj = webdriver.Chrome("chromedriver.exe")
    driver_obj.maximize_window()
    driver_obj.get("https://splashthat.com/login")
    driver_obj.implicitly_wait(10)
    driver_obj.find_element(By.ID, "homeRealmDiscoveryInput").send_keys(username)
    driver_obj.find_element(By.ID, "homeRealmDiscoverySubmit").click()
    driver_obj.find_element(By.ID, "loginPasswordInput").send_keys(password)
    driver_obj.find_element(By.ID, "loginSubmit").click()
    time.sleep(10)
    return driver_obj.current_url
