import requests
import json

headers = {"Authorization": "Bearer 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"}
url = 'https://api.github.com/graphql'

query = """
query {
  search(query: "stars:>1000", type: REPOSITORY, first: 100) {
    edges {
      node {
        ... on Repository {
          nameWithOwner
          issues{
            totalCount
          }
          closedIssues: issues (states: CLOSED){
            totalCount
          }
        }
      }
    }
  }
}
"""


response = requests.post(url, json={'query': query}, headers=headers)
data = response.json()

for i, repo in enumerate(data["data"]["search"]["edges"]):
    nameWithOwner = repo['node']['nameWithOwner']
    issues = repo['node']['issues']['totalCount']
    closedIssues = repo['node']['closedIssues']['totalCount']
    print(f"{i + 1}. Nome com autor: {nameWithOwner} - Total de issues: {issues} - Issues fechadas: {closedIssues} ")


