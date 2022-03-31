from operator import index
import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Process results.
print("\nKey values:")
[print(f"- {i.strip()}") for i in response_dict]

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"\nRepositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}\n{[i for i in sorted(repo_dict.keys())]}")

for i, repo_dict in enumerate(repo_dicts[:3]):
    print(f"\nSelected information about {i+1} repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")