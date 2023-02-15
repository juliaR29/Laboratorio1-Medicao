from datetime import datetime

import requests

headers = {"Authorization": "Bearer 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"}
url = 'https://api.github.com/graphql'

query = """
query { 
  search(
    type:REPOSITORY,
    query: "stars:>100"
    first: 100
  ) {
    edges{
      node{
        ... on Repository {
          name,
          createdAt,
          updatedAt
        }
      }
    },
  }
}
"""

response = requests.post(url, headers=headers, json={"query": query})
data = response.json()

for i, repo in enumerate(data["data"]["search"]["edges"]):
    repoName = repo['node']['name']
    createdAt = repo['node']['createdAt']
    updatedAt = repo['node']['updatedAt']
    created_date = datetime.strptime(createdAt, '%Y-%m-%dT%H:%M:%SZ').date()
    updated_date = datetime.strptime(updatedAt, '%Y-%m-%dT%H:%M:%SZ').date()

    differenceInDays = updated_date - created_date

    print(f"{i + 1}. Data de criação: {createdAt} - Última atualização: {updatedAt}  "
          f"Dias de diferença: {differenceInDays} - Nome: {repoName}")



