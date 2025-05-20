from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize("username,password,expected_error", [
    ("wrong_user", "secret_sauce", "Username and password do not match any user"),
    ("standard_user", "wrong_pass", "Username and password do not match any user"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("", "", "Username is required")
])
def test_invalid_login(browser, username, password, expected_error):

    page = LoginPage(browser)
    page.load()

    page.login(username, password)

    error_text = page.get_error_message()
    assert expected_error.lower() in error_text.lower()
    