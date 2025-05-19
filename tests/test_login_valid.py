from pages.login_page import LoginPage

def test_valid_login(browser):
    page = LoginPage(browser)
    page.load()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in browser.current_url

