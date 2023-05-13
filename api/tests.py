
import requests

cookies = {
    'sessionid': 'uwkbk1hdmfwa5c2ixu5i9mvc5kcybf0g',
    'csrftoken': 'rHIDo2ttXuPZZq23rxrYGm8UuloYrJ3G',
}

headers = {
    # 'Cookie': 'sessionid=uwkbk1hdmfwa5c2ixu5i9mvc5kcybf0g; csrftoken=rHIDo2ttXuPZZq23rxrYGm8UuloYrJ3G',
    'csrftoken': 'rHIDo2ttXuPZZq23rxrYGm8UuloYrJ3G',
    'X-CSRFToken': 'rHIDo2ttXuPZZq23rxrYGm8UuloYrJ3G',
    'Content-Type': 'application/json',
}

json_data = {
    'csrfmiddlewaretoken': '84CZxS3k7tIcrDAOMwtBEt2sD884bRlSpBasLKmDUNn1gTsH3TKpaF0cXjmSsqeo',
    'bb': 3,
    'author': 'admin',
    'content': 'api',
}

response = requests.post('http://localhost:8000/api/bbs/3/comments/', cookies=cookies, headers=headers, json=json_data)

print(response.json())