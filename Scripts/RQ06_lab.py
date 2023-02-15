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
    print(f"{i + 1}. Nome com autor: {nameWithOwner} - Total de issues: {issues} - Issues fechadas: {closedIssues} - "
          f"Razão entre total e fechadas: {issues - closedIssues} ")
