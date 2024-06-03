from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
import pytest

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def user():
    return User.objects.create_user(username='test_user', password='test_password')

def test_front_page_view(client):
    response = client.get(reverse('front_page'))
    assert response.status_code == 200

def test_get_prescription_view(client):
    response = client.get(reverse('get_prescription'))
    assert response.status_code == 200

def test_member_account_view(client):
    response = client.get(reverse('member_account'))
    assert response.status_code == 200

def test_workout_plan_view(client):
    response = client.get(reverse('workout_plan'))
    assert response.status_code == 200

def test_nutrition_plan_view(client):
    response = client.get(reverse('nutrition_plan'))
    assert response.status_code == 200

def test_feedback_view(client):
    response = client.get(reverse('feedback'))
    assert response.status_code == 200

def test_view_users_view(client, user):
    response = client.get(reverse('view_users'))
    assert response.status_code == 200

def test_login_view_get(client):
    response = client.get(reverse('login_view'))
    assert response.status_code == 200

def test_login_view_post_valid(client, user):
    response = client.post(reverse('login_view'), {'username': 'test_user', 'password': 'test_password'})
    assert response.status_code == 302  # 302 is the status code for redirect
    assert response.url == reverse('user', kwargs={'id': user.id})

def test_login_view_post_invalid(client):
    response = client.post(reverse('login_view'), {'username': 'invalid_user', 'password': 'invalid_password'})
    assert response.status_code == 200
    assert b'Authentication error!' in response.content

def test_logout_view(client):
    response = client.get(reverse('logout_view'))
    assert response.status_code == 302

def test_base_view_authenticated(client, user):
    client.login(username='test_user', password='test_password')
    response = client.get(reverse('base_view'))
    assert response.status_code == 200
    assert b'test_user' in response.content

def test_base_view_unauthenticated(client):
    response = client.get(reverse('base_view'))
    assert response.status_code == 200
    assert b'None' in response.content

def test_add_user_view_get(client):
    response = client.get(reverse('add_user'))
    assert response.status_code == 200

def test_add_user_view_post_valid(client):
    response = client.post(reverse('add_user'), {'username': 'new_user', 'password_1': 'new_password', 'password_2': 'new_password', 'name': 'John', 'surname': 'Doe', 'email': 'john@example.com'})
    assert response.status_code == 302  # 302 is the status code for redirect
    assert User.objects.filter(username='new_user').exists()

def test_add_user_view_post_existing_user(client, user):
    response = client.post(reverse('add_user'), {'username': 'test_user', 'password_1': 'new_password', 'password_2': 'new_password', 'name': 'John', 'surname': 'Doe', 'email': 'john@example.com'})
    assert response.status_code == 200
    assert b'User already exists!' in response.content

def test_add_user_view_post_password_mismatch(client):
    response = client.post(reverse('add_user'), {'username': 'new_user', 'password_1': 'new_password', 'password_2': 'mismatch_password', 'name': 'John', 'surname': 'Doe', 'email': 'john@example.com'})
    assert response.status_code == 200
    assert b'Passwords do not match!' in response.content

def test_reset_password_view_get(client, user):
    response = client.get(reverse('reset_password', kwargs={'id': user.id}))
    assert response.status_code == 200

def test_reset_password_view_post_valid(client, user):
    response = client.post(reverse('reset_password', kwargs={'id': user.id}), {'password_1': 'new_password', 'password_2': 'new_password'})
    assert response.status_code == 302  # 302 is the status code for redirect
    user.refresh_from_db()
    assert user.check_password('new_password')

def test_reset_password_view_post_password_mismatch(client, user):
    response = client.post(reverse('reset_password', kwargs={'id': user.id}), {'password_1': 'new_password', 'password_2': 'mismatch_password'})
    assert response.status_code == 200
    assert b'Passwords do not match!' in response.content

def test_user_view_authenticated(client, user):
    client.login(username='test_user', password='test_password')
    response = client.get(reverse('user', kwargs={'id': user.id}))
    assert response.status_code == 200

def test_user_view_unauthenticated(client, user):
    response = client.get(reverse('user', kwargs={'id': user.id}))
    assert response.status_code == 302
