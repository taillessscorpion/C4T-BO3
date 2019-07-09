import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

print(r.json())
# r.status_code
# 200
# 401

# r.headers['content-type']
# 'application/json; charset=utf8'

# r.encoding
# 'utf-8'

# r.text
# u'{"type":"User"...'
# {"message":"Bad credentials","documentation_url":"https://developer.github.com/v3"}

# r.json()
# {u'private_gists': 419, u'total_private_repos': 77, ...}
# {'message': 'Bad credentials', 'documentation_url': 'https://developer.github.com/v3'}