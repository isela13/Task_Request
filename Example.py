

import requests
response = requests.get('https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn')
print(response.url)

print(response.status_code)
