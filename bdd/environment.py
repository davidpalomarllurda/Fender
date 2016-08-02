from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import time


def before_all(context):

    dir = os.path.dirname(__file__)
    chrome_driver_path = dir + "\chromedriver.exe" #remove the .exe extension on linux or mac platform

    context.driver = webdriver.Chrome(chrome_driver_path)
    context.driver.implicitly_wait(30)
    context.driver.maximize_window()

    
    

def after_all(context):
    context.driver.quit()
