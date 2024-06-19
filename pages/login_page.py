import allure
from conftest import fake
from pages.base_page import BasePage
from utils.locators import LoginPageLocators, MainPageLocators
from utils.special_requests import generate_random_string
randoms_string = generate_random_string(10)
email = fake.email()


class LoginPage(BasePage):

    @allure.step('Ждем загрузки заголовка страницы входа')
    def wait_for_login_page_header(self):
        return self.wait_loading_of_element(LoginPageLocators.LOGIN_HEADER)

    @allure.step('Нажимаем ссылку восстановления пароля')
    def click_restore_password(self):
        return self.click_element(LoginPageLocators.BUTTON_RESTORE_PASSWORD)

    @allure.step('Вводим email')
    def enter_email(self, email):
        self.enter_text_to_element(locator=LoginPageLocators.EMAIL_INPUT_FIELD, keys=email)

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        self.enter_text_to_element(locator=LoginPageLocators.PASSWORD_INPUT_FIELD, keys=password)

    @allure.step('Нажимаем кнопку Войти')
    def click_login_button(self):
        return self.click_element(LoginPageLocators.BUTTON_LOGIN)

    @allure.step('Нажимаем Конструктор')
    def click_constructor(self):
        return self.click_element(MainPageLocators.MENU_CONSTRUCTOR)

    @allure.step('Заполняем поля email и пароль, нажимаем на вход')
    def fill_email_and_password_and_enter(self, email='', password=''):
        self.wait_for_login_page_header()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.try_out_url()
