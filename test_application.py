from application import application
with application.test_client() as c:
    response = c.get('/')
    assert response.data == 'Hello world!'
    assert response.status_code == 200
