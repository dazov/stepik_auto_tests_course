from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try:  
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Smolensk")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Ivanov@Smolensk.ru")
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.NAME, "file")
    element.send_keys(file_path)

    
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()