from api.models.users import Users


def test_new_user():
    """
    GIVEN a Users model
    WHEN a new Users is created
    THEN check the username and password fields are defined correctly
    """

    user = Users("some_username", "some_password")
    assert user.username == "some_username"
    assert user.password == "some_password"
