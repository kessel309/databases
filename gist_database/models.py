class Gist(object):
    def __init__(self, gist):
        self.id = gist[0]
        self.github_id = gist[1]
        self.html_url = gist[2]
        self.git_pull_url = gist[3]
        self.git_push_url = gist[4]
        self.commits_url = gist[5]
        self.forks_url = gist[6]
        self.public = gist[7]
        self.created_at = gist[8]
        self.updated_at = gist[9]
        self.comments = gist[10]
        self.comments_url = gist[11]

    def __str__(self):
        return 'Gist: {}'.format(self.github_id)
