import requests
import json
import ConfigParser, os

#login

config = ConfigParser.RawConfigParser()
config.read('photosynq.cfg')


payload = {'user[email]': config.get('Credentials', 'email'), 'user[password]': config.get('Credentials', 'password')}

r = requests.post(config.get('API', 'url')+'/api/v2/sign_in.json', params=payload)

print r.text

print r.status_code
print r.headers['content-type']

json_data = r.json()

user_data = json_data['user']


os.environ["AUTH_TOKEN"] = user_data['auth_token']

print os.environ["AUTH_TOKEN"]

#get projects
payload = {'user_email': config.get('Credentials', 'email'), 'user_token':  os.environ["AUTH_TOKEN"]}

r = requests.get(config.get('API', 'url')+'/api/v2/projects.json', params=payload)

print r.text

