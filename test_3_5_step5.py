import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# "236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"

@pytest.mark.parametrize('lesson', ["236899", "236903", "236904"])  
def test_auth(browser,lesson):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.implicitly_wait(10)
    browser.get(link)
    
    auth_button=browser.find_element(By.XPATH, "//a[@id='ember33']")
    auth_button.click()
    print("Найти кнопку логин")
    
    input1 = browser.find_element(By.XPATH, "//input[@name='login']")
    input1.send_keys("blinnna@gmail.com")
    print("Ввести почту")
    
    input2 = browser.find_element(By.XPATH, "//input[@name='password']")
    input2.send_keys("V4erg*abVEkp")
    print("Ввести пароль")
    
    enter_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    enter_button.click()
    print("Нажать кнопку")
    
    time.sleep(5)
    
    answer_input = browser.find_element(By.XPATH, "//textarea")
    answer_input.send_keys(math.log(int(time.time())))
    print("Ввести ответ")
        
    submit_button = browser.find_element(By.XPATH, "//button[@class='submit-submission']")
    submit_button.click()
    print("Нажать кнопку отправки ответа")
    
    time.sleep(10)
    
    feedback = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='smart-hints__hint']"))
        )
    assert feedback.text != "Correct!", "Тест не упал"
    print(feedback.text)
    
    

    

