import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

data = {
    "id": 1,
    "title": "Python Backend",
    "body" : "Learning HTTP Methods",
    "userId": 1
}

response = requests.put(url,json=data)
print(response.json())
print(response.status_code)

data1 = {
    "title": "Learning FAST API"
}

response = requests.patch(url,json=data1)
print(response.json())
print(response.status_code)

response = requests.delete(url)
print(response.json())
print(response.status_code)