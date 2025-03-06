from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:  
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/execute_script.html"
    browser.get(link)

    #подсчет
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    #скролл футера
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()