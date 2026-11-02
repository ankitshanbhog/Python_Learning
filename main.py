from blog_manager import get_post,get_posts
import requests

response = get_posts()

print(response)

result = get_post(5)
print(result["title"])
