import requests

headers = {"Authorization": "Bearer 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"}
url = 'https://api.github.com/graphql'

query = '''
{
  search(query: "stars:>100", type: REPOSITORY, first: 10) {
    repositoryCount
    edges {
      node {
        ... on Repository {
          nameWithOwner
          createdAt
          pushedAt
          stargazers {
            totalCount
          }
          primaryLanguage {
            name
          }
          pullRequests(states: MERGED) {
            totalCount
          }
          releases(first: 1) {
            totalCount
          }
          issues(first: 1) {
            totalCount
          }
          closedIssues: issues (states: CLOSED){
            totalCount
          }
          updatedAt
        }
      }
    }
  }
}

'''

response = requests.post(url, json={'query': query}, headers=headers)
data = response.json()

for repo in data['data']['search']['edges']:
    print("Nome do repositório:", repo['node']['nameWithOwner'])
    print("Idade do repositório :", repo['node']['createdAt'])
    print("Total de pull requests aceitas:", repo['node']['pullRequests']['totalCount'])
    print("Total de releases:", repo['node']['releases']['totalCount'])
    print("Tempo até a última atualização:", repo['node']['updatedAt'])


    try:
        print("Linguagem primária:", repo['node']['primaryLanguage']['name'])
    except TypeError:
        print("Linguagem primária: Não especificada")

    try:
        ratio = repo['node']['closedIssues']['totalCount'] / repo['node']['issues']['totalCount']
        print("Razão entre issues fechadas e total de issues:", ratio)
    except (TypeError, ZeroDivisionError):
        print("Razão entre issues fechadas e total de issues: Não disponível")

    print("========================================")

