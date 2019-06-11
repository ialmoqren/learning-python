
def test_get_photographers(app):
    """Send a GET with good auth and expect a message."""
    client = app.test_client()
    result = client.get("/photographers")
    assert result.status_code == 200
    assert True
