import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:

    response = requests.get(url,timeout =5)

    response.raise_for_status()

    data = response.json()

    print(data["title"])

except requests.exceptions.Timeout as e:
    print("Timeput error ",e)
except requests.exceptions.HTTPError as e:
    print("Http error ",e)
except requests.exceptions.RequestException as e:
    print("Other Request error ",e)

