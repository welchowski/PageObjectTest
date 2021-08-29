from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.go_to_login_page()

    page.should_be_login_link()
    login_page=LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


    