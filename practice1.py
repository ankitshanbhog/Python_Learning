import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : "Python backend learning",
    "body" : "I am Learning to build backend applications",
    "userId" : 5
}

response = requests.post(url,json = data)
print(response.status_code)
print(response.json())