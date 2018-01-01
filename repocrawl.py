import requests
import json

def repo_crawl (owner, type='orgs'):
    url = 'https://api.github.com/%s/%s/repos' % (type, owner)
    r = requests.get(url)
    if(r.ok):
        repoItem = json.loads(r.text or r.content)
        return repoItem

    return False