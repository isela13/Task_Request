
# import requests module
import requests

# Making a get request
response = requests.get('https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn')

# print request object
print(response.url)

# print status code
print(response.status_code)