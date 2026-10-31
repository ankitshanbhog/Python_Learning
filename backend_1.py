import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json().get("title"))



url = "https://jsonplaceholder.typicode.com/posts"

data ={
    "title": "My first post",
    "body": "Learning Python APIs",
    "userId": 1
}

response = requests.post(url,json = data)

print(response.status_code)
print(response.json())