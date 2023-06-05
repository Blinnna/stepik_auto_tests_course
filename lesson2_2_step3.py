from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1_element = browser.find_element(By.XPATH, "//span[@id='num1']")
    num1 = num1_element.text
    num2_element = browser.find_element(By.XPATH, "//span[@id='num2']")
    num2 = num2_element.text    
    x = str(int(num1) + int(num2))
    select = Select(browser.find_element(By.XPATH, "//select[@id='dropdown']"))
    select.select_by_value(x)
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()	
