DROP TABLE if exists gists;
CREATE TABLE gists (
  id INTEGER PRIMARY KEY autoincrement,
  github_id TEXT NOT NULL,
  html_url TEXT NOT NULL,

  git_pull_url TEXT NOT NULL,
  git_push_url TEXT NOT NULL,

  commits_url TEXT NOT NULL,
  forks_url TEXT NOT NULL,

  public BOOLEAN NOT NULL,

  created_at DATETIME NOT NULL,
  updated_at DATETIME NOT NULL,

  comments INTEGER NOT NULL,
  comments_url TEXT NOT NULL
);
