import pytest
from src.pages.login import *
import json
from pytest_bdd import scenario, given, when, then


@scenario('login.feature', 'Login and select plan')
def test_login():
    pass


@given('I am on login screen')
def login_user():
    login()


@given('Log in to application')
def login_application():
    json_file = open('configurations.json', 'r')
    user_details = json.load(json_file)
    login_existing_user(user_details["username"], user_details["password"])


@when('I go to the Library')
def select_library():
    get_library()


@when('I choose unlock access select plan')
def select_unlock_access():
    unlock_access_select_plan()


@then('I should be on plan demo')
def plan_demo():
    plan_demo


