import pytest
from api import app   # import the flask app

@pytest.fixture 
def client():
    # provide a test client for flask app
    app.config["TESTING"] = True    #enable testng mode
    with app.test_client() as client:
        yield client  # provide the test client instance
    
def test_add_user(client):
    # test adding new user
    response = client.post('/user', json = {"id" : 1, "name" : "Alice"})
    assert response.status_code ==201
    assert response.json == {"id" : 1, "name" : "Alice"}

def test_get_user(client):
    #Test retrieving a user, first add user
    client.post('/user', json = {"id" : 2, "name" : "Bob"})

    #then retrieve the user

    response = client.get('/users/2')

    assert response.status_code == 200
    assert response.json == {"id" : 2, "name": "Bob"}

def test_user_not_found(client):
     response = client.get('/users/99')

     assert response.status_code == 400
     assert response.json == {"error" : "user not found"}