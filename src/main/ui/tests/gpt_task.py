from playwright.sync_api import expect

from ui.pages.basket_page import BasketPage
from ui.pages.catalog_page import CatalogPage
from ui.steps.basket_steps import BasketSteps
from ui.steps.catalog_steps import CatalogSteps
from ui.steps.login_steps import LoginSteps


def test_login_locked_out_user(page):
    user = LoginSteps(page)
    user.open_login_page().login("locked_out_user", "secret_sauce")

    user.expect_login_page()
    user.expect_error_text("locked out")

def test_basket_empty(auth_page):
    user = CatalogSteps(auth_page)

    user.open_catalog()
    user.add_to_cart('Sauce Labs Backpack')

    assert  user.get_cart_count() == 1

    user.remove_from_cart('Sauce Labs Backpack')

    assert user.get_cart_count() == 0

def test_catalog_sort(auth_page):
    user = CatalogSteps(auth_page)

    user.sort_items('az')

    assert user.get_product_names() == sorted(user.get_product_names())

    user.sort_items('za')

    assert user.get_product_names() == sorted(user.get_product_names(), reverse= True)

"""авторизоваться
→ добавить товар в корзину
→ перейти в корзину
→ проверить наличие товара
→ удалить товар
→ проверить, что корзина пуста"""
def test_basket(auth_page):
    catalog = CatalogSteps(auth_page)
    catalog.add_to_cart('Sauce Labs Backpack')
    catalog.open_cart()

    basket = BasketSteps(auth_page)

    assert 'Sauce Labs Backpack' in basket.get_item_names()

    basket.remove_item('Sauce Labs Backpack')

    assert 'Sauce Labs Backpack' not in basket.get_item_names()