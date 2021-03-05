import requests

data = {
  'id': '123',
  'verbosity': 'high'
}

response = requests.post('http://JENKINS_URL/job/JOB_NAME/buildWithParameters', data=data, auth=('USER', 'TOKEN'))
