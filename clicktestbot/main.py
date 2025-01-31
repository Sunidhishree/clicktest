import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

driver=webdriver.Chrome(options= opt)
driver.get("https://cpstest.org/")

pad=driver.find_element(By.ID,"clickarea")

while True:
    pad.click()
