import requests

headers = {"Authorization": "Bearer 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"}
url = 'https://api.github.com/graphql'

query = '''
query {
  search(query: "stars:>100", type: REPOSITORY, first: 100) {
    edges {
      node {
        ... on Repository {
        nameWithOwner
          pullRequests(states: MERGED) {
            totalCount
          }
        }
      }
    }
  }
}
'''

response = requests.post(url, json={'query': query}, headers=headers)

data = response.json()

for i, repo in enumerate(data["data"]["search"]["edges"]):
    nameWithOwner = repo['node']['nameWithOwner']
    pr = repo['node']['pullRequests']['totalCount']
    print(f"{i + 1}. Nome com autor: {nameWithOwner} - {pr} pull requests aceitas ")