import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_start_browser_with_language(browser):
    browser.get(link)
    button=browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button != True, "Корзина не найдена"
