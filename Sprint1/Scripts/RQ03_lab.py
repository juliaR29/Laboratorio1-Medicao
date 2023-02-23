import requests

headers = {"Authorization": "Bearer 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"}
url = 'https://api.github.com/graphql'

#coloquei os primeiros 40 porque sempre que coloco mais dá erro, acredito ser algo relacionado a limite de requisições 
query = '''
query {
  search(query: "stars:>100", type: REPOSITORY, first: 40) {
    edges {
      node {
        ... on Repository {
        nameWithOwner
          releases(first:0) {
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
    releases = repo['node']['releases']['totalCount']
    print(f"{i + 1}. Nome com autor: {nameWithOwner} - {releases} releases ")

