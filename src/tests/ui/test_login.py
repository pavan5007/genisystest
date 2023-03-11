import pytest
from src.pages.login import *

@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login():
    result  = login_existing_user("ammineni8007@gmail.com","P@van@5007")
    assert result == "https://app.splashthat.com/events"

@pytest.mark.regression
def test_login_invalid_username():
    result = login_existing_user("ammineni80075@gmail.com", "P@van7@5007")
    assert result != "https://app.splashthat.com/events"

@pytest.mark.regression
def test_login_invalid_password():
    result = login_existing_user("ammineni8007@gmail.com","python44334@1234")
    assert result != "https://app.splashthat.com/events"