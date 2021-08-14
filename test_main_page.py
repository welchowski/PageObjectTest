from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    
    page = MainPage(browser, MainPageLocators.LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()

    page.should_be_login_link()     # выполняем метод страницы — переходим на страницу логина
    page_1=LoginPage(browser, MainPageLocators.LINK)
    page_1.should_be_login_page()


    