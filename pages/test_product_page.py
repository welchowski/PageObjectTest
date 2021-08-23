from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasketPageLocators



class ProductPage(BasePage): 
    def add_to_basket(self):
        
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
    
    
                   
class BasketPage(BasePage):

    def should_be_msg_same_produsct_added_to_basket(self):
        name=self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        print(name)
        msg=self.browser.find_element(*BasketPageLocators.MSG_PRODUCT_ADDED).text   
        assert name==msg, "name of product don't same" 

    def should_be_single_price_with_product_added(self):
        price=self.browser.find_element(*ProductPageLocators.PRICE).text
        msg_price=self.browser.find_element(*BasketPageLocators.PRICE_MSG).text
        print(self.browser.find_element(*ProductPageLocators.PRICE).text)
        print("price=" + price + " msg_prise="+msg_price)
        assert price in msg_price, "price difference"

        
