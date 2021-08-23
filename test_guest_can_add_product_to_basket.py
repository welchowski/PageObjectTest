import pytest
from .pages.test_product_page import ProductPage
from .pages.test_product_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.locators import BasketPageLocators
from .pages.base_page import BasePage

import time
from selenium import webdriver

@pytest.mark.parametrize('code', [0,1,2,3,4,5,6, pytest.param(7, marks=pytest.mark.xfail),8,9])
def test_guest_can_add_product_to_basket(browser, code):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{code}"
    print(link)
    page = ProductPage(browser, link)
    
   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()      
                   # открываем страницу
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page_busket=BasketPage(browser, browser.current_url)
    page_busket.should_be_msg_same_produsct_added_to_basket()
    page_busket.should_be_single_price_with_product_added()


    print(link)
   #time.sleep(5)
    
    


    