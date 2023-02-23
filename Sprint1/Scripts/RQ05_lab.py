import requests

headers = {"Authorization": "Bearer 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"}
url = 'https://api.github.com/graphql'

query = """
query {
  search(query: "stars:>1000", type: REPOSITORY, first: 100) {
    edges {
      node {
        ... on Repository {
          nameWithOwner
          primaryLanguage {
            name
          }
        }
      }
    }
  }
}
"""

response = requests.post(url, json={"query": query}, headers=headers)
data = response.json()

for i, repo in enumerate(data["data"]["search"]["edges"]):
    nameWithOwner = repo['node']['nameWithOwner']
    language = repo['node']['primaryLanguage']
    print(f"{i + 1}. Nome com autor: {nameWithOwner}")
    if language:
        print(f"Linguagem: {language['name']}")
    else:
        print("Linguagem: Não definida")

