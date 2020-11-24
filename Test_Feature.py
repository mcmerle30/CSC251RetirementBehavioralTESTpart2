from behave import *

use_step_matcher("re")


@given("retirement age between 1900 and 1937", [1900, 1937])
def year(context):
    pass


@when("assert these values")
def assert_value(value):
    assert value == (65, 0)


@then("the value equals year 65 month 0")
def value_equals_year(value):
    value.calculate_retirement_age(year)
