import requests 
from datetime import datetime 


def get_all_posts():
    url = 'http://127.0.0.1:8000/posts/'
    response = requests.get(url, auth=('admin', '@admin123'))

    print(response.status_code)
    print(response.json())


def create_new_post():
    url = 'http://127.0.0.1:8000/posts/'
    data = {
        'title': 'New Post Title 3',
        'description': 'This is the content of the new post 3',
        'updated_at': datetime.now().isoformat()
    }
    response = requests.post(url, json=data, auth=('admin', '@admin123'))

    print(response.status_code)
    print(response.json())


def get_detail_post(post_id):
    url = f'http://127.0.0.1:8000/posts/{post_id}/'
    response = requests.get(url, auth=('admin', '@admin123'))

    print(response.status_code)
    print(response.json())


def update_detail_post(post_id):
    url = f'http://127.0.0.1:8000/posts/{post_id}/'
    data = {
        'title': 'Updated Post Title',
        'description': 'This is the updated content of the post',
        'updated_at': datetime.now().isoformat()
    }
    response = requests.put(url, json=data, auth=('admin', '@admin123'))

    print(response.status_code)
    print(response.json())


def update_partial_post(post_id):
    url = f'http://127.0.0.1:8000/posts/{post_id}/'
    data = {
        'description': "This is the updated partial of the post",
    }
    response = requests.patch(url, json=data, auth=('admin', '@admin123'))
    print(response.status_code)
    print(response.json())


def delete_post(post_id):
    url = f'http://127.0.0.1:8000/posts/{post_id}/'
    response = requests.delete(url, auth=('admin', '@admin123'))

    print(response.status_code)


print("Get all: ")
get_all_posts()
# print("Create new post: ")
# create_new_post()
# print("Get detail post: ")
# get_detail_post(post_id="2")
# print("Updated post: ")
# update_detail_post(post_id="2")
# print("Delete post: ")
# delete_post(post_id="2")
# print("Update partial post: ")
# update_partial_post(post_id="3")
