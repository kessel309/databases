import requests
import sqlite3


INSERT_GIST_QUERY = """INSERT INTO gists (
    "github_id", "html_url", "git_pull_url",
    "git_push_url", "commits_url",
    "forks_url", "public", "created_at",
    "updated_at", "comments", "comments_url"
) VALUES (
    :github_id, :html_url, :git_pull_url,
    :git_push_url, :commits_url, :forks_url,
    :public, :created_at, :updated_at,
    :comments, :comments_url
);"""
URL_TEMPLATE = 'https://api.github.com/users/{username}/gists'
conn = sqlite3.connect('database.db')
c = conn.cursor()

def delete_table():
    c.execute('DELETE FROM gists')
    conn.commit()
    
def print_table(parms):
    c.execute('SELECT {} FROM gists'.format(str(parms)))
    rows = c.fetchone()
    for row in rows:
        print(row)
        
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS gists(
    "github_id", "html_url", "git_pull_url",
    "git_push_url", "commits_url",
    "forks_url", "public", "created_at",
    "updated_at", "comments", "comments_url")''')
    conn.commit()
    
  
def import_gists_to_database(db, username, commit=True):
    resp = requests.get(URL_TEMPLATE.format(username=username))
    resp.raise_for_status()

    gists_data = resp.json()
    print('Gitsts Data ==',gists_data)
    for gist in gists_data:
        params = {
            "github_id": gist['id'],
            "html_url": gist['html_url'],
            "git_pull_url": gist['git_pull_url'],
            "git_push_url": gist['git_push_url'],
            "commits_url": gist['commits_url'],
            "forks_url": gist['forks_url'],
            "public": gist['public'],
            "created_at": gist['created_at'],
            "updated_at": gist['updated_at'],
            "comments": gist['comments'],
            "comments_url": gist['comments_url'],
        }
        db.execute(INSERT_GIST_QUERY, params)
        if commit:
            db.commit()
create_table()
#delete_table()
import_gists_to_database(conn,'kessel309')


print_table('*')


#delete_table()