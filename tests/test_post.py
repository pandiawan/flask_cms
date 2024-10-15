import json
import io
from flask import url_for
from datetime import datetime


def test_add_post(client, headers):
    new_category = {'name': 'New Category'}
    category_response = client.post(url_for('category.create'), data=json.dumps(new_category), headers=headers)
    assert category_response.status_code == 201
    category_id = category_response.json['_id']

    upload_dir = '{}/{}/{:02d}/{:02d}'.format('images', datetime.now().year, datetime.now().month, datetime.now().day)
    filename = 'test_image.jpg'
    post_data = {
        'title': 'Test Create Post',
        'content': 'This is a test create post.',
        'image': (io.BytesIO(b"fake image data"), filename),
        'category_id': category_id,
        'tags': 'tag1, tag2',
        'author': '605c72f1b22362b8f0d4e703',
    }

    response = client.post(url_for('post.create'), data=post_data, headers=headers, content_type='multipart/form-data')
    print(response.data)
    assert response.status_code == 201
    assert response.json['title'] == post_data['title']
    assert response.json['content'] == post_data['content']
    assert response.json['image'] == '{}/{}'.format(upload_dir, filename)


def test_get_all_posts(client, headers):
    response = client.get(url_for('user.get_all'), headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_post_by_id(client, headers):
    new_category = {'name': 'New Category'}
    category_response = client.post(url_for('category.create'), data=json.dumps(new_category), headers=headers)
    assert category_response.status_code == 201
    category_id = category_response.json['_id']

    upload_dir = '{}/{}/{:02d}/{:02d}'.format('images', datetime.now().year, datetime.now().month, datetime.now().day)
    filename = 'test_image.jpg'
    post_data = {
        'title': 'Test Get Post',
        'content': 'This is a test get post.',
        'image': (io.BytesIO(b"fake image data"), filename),
        'category_id': category_id,
        'tags': 'tag1, tag2',
        'author': '605c72f1b22362b8f0d4e703',
    }
    response = client.post(url_for('post.create'), data=post_data, headers=headers, content_type='multipart/form-data')
    post = json.loads(response.data)

    response = client.get(url_for('post.get_by_id', post_id=post['_id']), headers=headers)
    assert response.status_code == 200
    assert response.json['_id'] == post['_id']
    assert response.json['title'] == post_data['title']
    assert response.json['image'] == '{}/{}'.format(upload_dir, filename)


def test_update_post(client, headers):
    new_category = {'name': 'New Category'}
    category_response = client.post(url_for('category.create'), data=json.dumps(new_category), headers=headers)
    assert category_response.status_code == 201
    category_id = category_response.json['_id']

    upload_dir = '{}/{}/{:02d}/{:02d}'.format('images', datetime.now().year, datetime.now().month, datetime.now().day)
    filename = 'test_image.jpg'
    post_data = {
        'title': 'Test Update Post',
        'content': 'This is a test update post.',
        'image': (io.BytesIO(b"fake image data"), filename),
        'category_id': category_id,
        'tags': 'tag 1, tag 2',
        'author': '605c72f1b22362b8f0d4e703',
    }
    response = client.post(url_for('post.create'), data=post_data, headers=headers, content_type='multipart/form-data')
    post = json.loads(response.data)

    updated_filename = 'test_image2.jpg'
    updated_data = {
        'title': 'Updated Title',
        'content': 'Updated content of the post.',
        'image': (io.BytesIO(b"fake image data"), updated_filename),
        'category_id': category_id,
        'tags': 'tag 1, tag 2',
        'author': '605c72f1b22362b8f0d4e703',
    }

    response = client.put(url_for('post.update', post_id=post['_id']), data=updated_data, headers=headers, content_type='multipart/form-data')

    assert response.status_code == 200
    assert response.json['title'] == updated_data['title']
    assert response.json['content'] == updated_data['content']
    assert response.json['image'] == '{}/{}'.format(upload_dir, updated_filename)


def test_delete_post(client, headers):
    new_category = {'name': 'New Category'}
    category_response = client.post(url_for('category.create'), data=json.dumps(new_category), headers=headers)
    assert category_response.status_code == 201
    category_id = category_response.json['_id']

    filename = 'test_image.jpg'
    post_data = {
        'title': 'Test Post 4',
        'content': 'This is a test post 4.',
        'image': (io.BytesIO(b"fake image data"), filename),
        'category_id': category_id,
        'tags': 'tag 1, tag 2',
        'author': '605c72f1b22362b8f0d4e703',
    }
    create_response = client.post(url_for('post.create'), data=post_data, headers=headers, content_type='multipart/form-data')
    post = json.loads(create_response.data)

    response = client.delete(url_for('post.delete', post_id=post['_id']), headers=headers)
    assert response.status_code == 204

    get_response = client.get(url_for('post.get_by_id', post_id=post['_id']), headers=headers)
    assert get_response.status_code == 404
