
def test_anonymous_visit(client):
    response = client.get('/')

    assert response.status_code == 200
