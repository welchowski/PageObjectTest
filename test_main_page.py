from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    
    page = MainPage(browser, MainPageLocators.LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()

    page.should_be_login_link()     # выполняем метод страницы — переходим на страницу логина
    login_page=LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


    