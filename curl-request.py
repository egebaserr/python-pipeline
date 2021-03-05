import requests

data = {
  'id': '123',
  'verbosity': 'high'
}

response = requests.post('http://localhost:8080/Job/Test/buildWithParameters', data=data, auth=('USER', 'TOKEN'))
