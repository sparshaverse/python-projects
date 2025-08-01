import requests

url = 'https://libretranslate.com/translate'

headers = {
    'Content-Type': 'application/json'
}

payload = {
    'q': 'Hello, how are you?',
    'source': 'en',
    'target': 'es'
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Full Response:", response.json())  # Debugging tip

print("Translated Text:", response.json()['translatedText'])
