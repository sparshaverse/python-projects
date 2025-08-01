import requests

url = 'https://jsonplaceholder.typicode.com/posts'
payload = {
    'title' : 'My Post',
    'body' : 'This is my post content.',
    'userId' : 1
}

response = requests.post(url, json=payload)
print("Status:", response.status_code)
print("Response:", response.json())