import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_item_button_exist(browser):
    browser.get(link)
    browser.find_element(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    
    time.sleep(10)
    
    