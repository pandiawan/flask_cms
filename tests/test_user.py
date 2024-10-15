import json
from flask import url_for


def test_create_user(client, headers):
    user_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "username": "johndoe",
        "password": "123456"
    }

    response = client.post(url_for('user.create'), json=user_data, headers=headers)
    assert response.status_code == 201
    assert response.json['_id'] is not None
    assert response.json['name'] == user_data['name']


def test_get_all_users(client, headers):
    response = client.get(url_for('user.get_all'), headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_user_by_id(client, headers):
    user_data = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "username": "janedoe",
        "password": "654321"
    }
    create_response = client.post(url_for('user.create'), json=user_data, headers=headers)
    user = json.loads(create_response.data)

    response = client.get(url_for('user.get_by_id', user_id=user['_id']), headers=headers)
    assert response.status_code == 200
    assert response.json['_id'] == user['_id']
    assert response.json['name'] == user_data['name']
    assert response.json['email'] == user_data['email']
    assert response.json['username'] == user_data['username']


def test_update_user(client, headers):
    user_data = {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "username": "janesmith",
        "password": "987654"
    }
    create_response = client.post(url_for('user.create'), json=user_data, headers=headers)
    user = json.loads(create_response.data)

    updated_data = {
        "name": "Jane Doe Updated",
        "email": "jane.updated@example.com",
        "username": "janedoeupdated"
    }
    response = client.put(url_for('user.update', user_id=user['_id']), json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json['name'] == updated_data['name']
    assert response.json['email'] == updated_data['email']
    assert response.json['username'] == updated_data['username']


def test_delete_user(client, headers):
    user_data = {
        "name": "Jake Doe",
        "email": "jake@example.com",
        "username": "jakedoe",
        "password": "112233"
    }
    create_response = client.post(url_for('user.create'), json=user_data, headers=headers)
    user = json.loads(create_response.data)

    response = client.delete(url_for('user.delete', user_id=user['_id']), headers=headers)
    assert response.status_code == 204

    get_response = client.get(url_for('user.get_by_id', user_id=user['_id']), headers=headers)
    assert get_response.status_code == 404
