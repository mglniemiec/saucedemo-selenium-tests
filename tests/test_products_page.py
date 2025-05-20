from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_product_list_after_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(browser)

    assert "inventory" in browser.current_url
    assert "PRODUCTS" in products_page.get_title()
    assert len(products_page.get_products()) > 0
