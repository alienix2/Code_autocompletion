from github import Github
import os

ACCESS_TOKEN = open("token.txt", "r").read().strip()
g = Github(ACCESS_TOKEN)
print(g.get_user().login)
repo_number = 200

# Random day
query = f"language:python created:2024-10-01..2024-10-02"
result = g.search_repositories(query)
print(result.totalCount)

# I clone the n first repositories only
for repo in result[:repo_number]:
    os.system(f"git clone {repo.clone_url} repos/{repo.owner.login}/{repo.name}")
    print(repo.clone_url)

result = g.search_repositories(query)
