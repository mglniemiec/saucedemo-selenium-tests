from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize("username,password", [
    ("wrong_user", "secret_sauce"),
    ("standard_user", "wrong_pass"),
    ("", "secret_sauce"),
    ("standard_user", ""),
    ("", "")
])
def test_invalid_login(browser, username, password):

    page = LoginPage(browser)
    page.load()

    page.login(username, password)

    assert "inventory" not in browser.current_url
    assert "error" in browser.page_source.lower()
