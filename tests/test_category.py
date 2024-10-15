import json
from flask import url_for


def test_add_category(client, headers):
    new_category = {'name': 'New Category'}
    response = client.post(url_for('category.create'), data=json.dumps(new_category), headers=headers)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'name' in data
    assert data['name'] == 'New Category'


def test_get_all_categories(client, headers):
    response = client.get(url_for('category.get_all'), headers=headers)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)


def test_get_category_by_id(client, headers):
    new_category = {'name': 'Test Category'}
    response = client.post(url_for('category.create'), data=json.dumps(new_category), headers=headers)
    category = json.loads(response.data)

    response = client.get(url_for('category.get_by_id', category_id=category['_id']), headers=headers)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Test Category'


def test_update_category(client, headers):
    new_category = {'name': 'Test Category'}
    response = client.post(url_for('category.create'), data=json.dumps(new_category), headers=headers)
    category = json.loads(response.data)

    updated_category = {'name': 'Updated Category'}
    response = client.put(url_for('category.get_by_id', category_id=category['_id']), data=json.dumps(updated_category), headers=headers)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Updated Category'


def test_delete_category(client, headers):
    new_category = {'name': 'Test Category'}
    response = client.post(url_for('category.create'), data=json.dumps(new_category), headers=headers)
    category = json.loads(response.data)

    response = client.delete(url_for('category.get_by_id', category_id=category['_id']), headers=headers)
    assert response.status_code == 204
