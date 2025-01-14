from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'danieltest'
    assert response.json()['email'] == 'danieltest@email.com'
    assert response.json()['first_name'] == 'Daniel'
    assert response.json()['last_name'] == 'Wu'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '111111111'

def test_change_password_success(test_user):
    response = client.put('/user/password', json={'password': 'test1234', 'new_password': 'new1234'})
    assert response.status_code == 204

def test_change_password_invalid_current_password(test_user):
    response = client.put('/user/password', json={'password': 'wrongpassword', 'new_password': 'new1234'})
    assert response.status_code == 401
    assert response.json() == {'detail': 'Error on password change'}

def test_change_phone_number_success(test_user):
    response = client.put('/user/phonenumber/222222222')
    assert response.status_code == 204
