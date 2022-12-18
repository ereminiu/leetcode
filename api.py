import requests

response = requests.get("https://github.githubassets.com/images/icons/emoji/unicode/1f3dc.png?v8")
print(response.text)