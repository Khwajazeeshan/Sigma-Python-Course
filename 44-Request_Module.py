# Using Requests Module In Python...........//////////////


import requests
result = requests.get("http://www.google.com")
print(result.text)
