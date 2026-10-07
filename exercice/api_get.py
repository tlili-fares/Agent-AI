import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)
#test#
print(response.status_code)
data = response.json()
print(data)
print(data["title"])