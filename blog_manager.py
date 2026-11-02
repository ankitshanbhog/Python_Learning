import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_posts():
    response = requests.get(f"{BASE_URL}/posts", timeout=5)

    response.raise_for_status()

    return response.json()


def get_post(post_id):
    response = requests.get(
        f"{BASE_URL}/posts/{post_id}",
        timeout=5
    )

    response.raise_for_status()

    return response.json()