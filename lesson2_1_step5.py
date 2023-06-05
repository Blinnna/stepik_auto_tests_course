from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
	# Открываем ссылку
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)	
    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)    
    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)    
    checkbox1 = browser.find_element(By.XPATH, "//label[contains(text(), 'the robot')]")
    checkbox1.click()
    radio1 = browser.find_element(By.XPATH, "//label[contains(text(), 'Robots rule')]")
    radio1.click()
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()	
	