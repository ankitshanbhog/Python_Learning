# Path parameters are used to retrieve the data we want from the API , by using the unique ID given. 
# Query parameters are used to retrieve the data based on the certain conditions.
import requests


url = "https://jsonplaceholder.typicode.com/comments"

params ={
    "postId" : 5,
    "limit" : 3
}

response = requests.get(url,params=params)

print(response.url)

for comment in response.json():
    print(comment.get("email"))

print(len(response.json()))