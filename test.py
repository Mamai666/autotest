from povtorpytest.playwright.page.login_page import LoginPage
from povtorpytest.playwright.page.checkout_page import CheckoutPage
from povtorpytest.playwright.page.inventory_page import InventoryPage


def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)


    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form('Alex', 'Cha', '12345678')