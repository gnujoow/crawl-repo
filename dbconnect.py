import json
import pymysql
from repocrawl import repo_crawl

db_info = json.loads(open('db_info.json', 'r').read())
db_connect = pymysql.connect(
    host=db_info['host'],
    user=db_info['username'],
    password=db_info['password'],
    db=db_info['db'],
    charset='utf8'
)

curs = db_connect.cursor(pymysql.cursors.DictCursor)
sql = "select * from owner"
curs.execute(sql)
rows = curs.fetchall()

for row in rows:
    print(row)
    repos = repo_crawl(row['name'], row['type'])
    sql = """insert ignore into repo(name,description,language,owner_id,repo_id)
         values (%s, %s, %s, %s, %s)"""
    for repo in repos:
        curs.execute(sql, (repo['name'],repo['description'], repo['language'], row['id'], repo['id']))
        print(repo['name'],repo['description'])
    db_connect.commit()

db_connect.close()
