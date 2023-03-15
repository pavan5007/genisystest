import pytest
from src.pages.signup import *

@pytest.mark.smoke
@pytest.mark.regression
def test_signup():
    result  = create_account()
    assert result == "https://app.splashthat.com/login/verifyEmail"

