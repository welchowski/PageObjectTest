import pytest
import time
from time import sleep

@pytest.mark.smoke
def test_guest_can_add_book_to_basket(browser):
    print("ddddd")
	# переход на нужную страницу
    browser.get(link)
    #time.sleep(30)
	# поиск кнопки добавления товара в корзину
    #sleep(30) #sleep для проверки правильности инициализации браузера
    add_to_basket = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert add_to_basket, 'кнопка добавления товара отсутвует'



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
@pytest.mark.regression
def test_exist_add_to_cart_button(browser):
	# переход на нужную страницу
    browser.get(link)
    #time.sleep(30)
	# поиск кнопки добавления товара в корзину
    #sleep(30) #sleep для проверки правильности инициализации браузера
    add_to_basket = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert add_to_basket, 'кнопка добавления товара отсутвует'