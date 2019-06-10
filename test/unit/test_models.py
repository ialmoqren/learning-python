import numbers
from api.models.orders import Orders
from api.models.photographers import Photographers
from api.models.users import Users


def test_new_order():
    """
    GIVEN a Orders model
    WHEN a new Orders is created
    THEN check the username and password fields are defined correctly
    """

    order = Orders("some_full_name", "some_email",
                   "some_phone", "some_details")

    assert order.fullName == "some_full_name"
    assert order.email == "some_email"
    assert order.phone == "some_phone"
    assert order.details == "some_details"

    assert order.id is None
    assert order.timestamp is None


def test_new_photographer():
    """
    GIVEN a Photographers model
    WHEN a new Photographers is created
    THEN check the username and password fields are defined correctly
    """

    photographer = Photographers("some_full_name", "some_email", "some_phone")
    assert photographer.fullName == "some_full_name"
    assert photographer.email == "some_email"
    assert photographer.phone == "some_phone"


def test_new_user():
    """
    GIVEN a Users model
    WHEN a new Users is created
    THEN check the username and password fields are defined correctly
    """

    user = Users("some_username", "some_password")
    assert user.username == "some_username"
    assert user.password == "some_password"
