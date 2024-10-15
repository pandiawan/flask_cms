import json
from flask import url_for


def test_add_tag(client, headers):
    tag_data = {'name': 'New Tag'}
    response = client.post(url_for('tag.create'), data=json.dumps(tag_data), headers=headers)
    assert response.status_code == 201
    assert response.json['_id'] is not None
    assert response.json['name'] == tag_data['name']


def test_get_all_tags(client, headers):
    response = client.get(url_for('tag.get_all'), headers=headers)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)


def test_get_tag_by_id(client, headers):
    new_tag = {'name': 'Test Tag'}
    response = client.post(url_for('tag.create'), data=json.dumps(new_tag), headers=headers)
    tag = json.loads(response.data)

    response = client.get(url_for('tag.get_by_id', tag_id=tag['_id']), headers=headers)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Test Tag'


def test_update_tag(client, headers):
    new_tag = {'name': 'Test Tag'}
    response = client.post(url_for('tag.create'), data=json.dumps(new_tag), headers=headers)
    tag = json.loads(response.data)

    updated_tag = {'name': 'Updated Tag'}
    response = client.put(url_for('tag.update', tag_id=tag['_id']), data=json.dumps(updated_tag), headers=headers)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Updated Tag'


def test_delete_tag(client, headers):
    new_tag = {'name': 'Test Tag'}
    response = client.post(url_for('tag.create'), data=json.dumps(new_tag), headers=headers)
    tag = json.loads(response.data)

    response = client.delete(url_for('tag.delete', tag_id=tag['_id']), headers=headers)
    assert response.status_code == 204
