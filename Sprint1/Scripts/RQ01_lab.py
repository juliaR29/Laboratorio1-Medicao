import requests
from datetime import datetime

headers = {"Authorization": "Bearer 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"}
url = 'https://api.github.com/graphql'

query = """
query {
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
    edges {
      node {
        ... on Repository {
          nameWithOwner
          createdAt
        }
      }
    }
  }
}
"""

response = requests.post(url, headers=headers, json={"query": query})
data = response.json()

for i, repo in enumerate(data["data"]["search"]["edges"]):
    nameWithOwner = repo['node']['nameWithOwner']
    createdAt = repo['node']['createdAt']
    created_date = datetime.strptime(createdAt, '%Y-%m-%dT%H:%M:%SZ').date()
    age = (datetime.now().date() - created_date).days
    print(f"{i + 1}. Nome com autor: {nameWithOwner} - Data de criação: {createdAt} - Idade: {age} dias")



