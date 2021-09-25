from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

try:
    # переход на нужную страницу
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # функция, которая находит значение выражения при заданном x
    def calc(x):
        return str( math.log( abs( 12 * math.sin( int(x) ) ) ) )


    # находим цену дома и ждем, пока она не станет $100, бронируем
    button = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    # находим значение x для выполнения задания
    x = browser.find_element_by_id("input_value")
    x_value = x.text

    # высчитываем результат для первого задания
    first_test_result = calc(x_value)

    # вводим ответ к первому тесту
    first_test_input = browser.find_element_by_id("answer")
    first_test_input.send_keys(first_test_result)

    # нажимаем на кнопку
    send_button = browser.find_element_by_id("solve")
    send_button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()