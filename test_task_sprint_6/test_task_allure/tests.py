from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

base_url = 'https://qa-mesto.praktikum-services.ru/'

@allure.step('ШАГ 1')
def test_check_email_placeholder():
    driver = webdriver.Chrome()
    driver.get(base_url)

    email = driver.find_element(By.ID, "email")

    assert email.get_attribute("placeholder") == 'Email'

    driver.quit()

def test_check_password_placeholder():
    driver = webdriver.Chrome()
    driver.get(base_url)

    password = driver.find_element(By.ID, "password")

    assert password.get_attribute("placeholder") == 'Пароль'

    driver.quit()