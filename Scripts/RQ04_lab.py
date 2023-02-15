from datetime import datetime

import requests

headers = {"Authorization": "Bearer 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"}
url = 'https://api.github.com/graphql'

query = """
query { 
  search(
    type:REPOSITORY,
    query:"is:public sort:updated",
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

    print(f"{i + 1}. Última atualização: {updatedAt} - Data de criação: {createdAt} - Nome: {repoName}")



