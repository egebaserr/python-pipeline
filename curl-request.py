import requests

data = {
  'id': '123',
  'verbosity': 'high'
}

response = requests.post('http://localhost:8081/Job/t/buildWithParameters', data=data, auth=('USER', 'TOKEN'))
