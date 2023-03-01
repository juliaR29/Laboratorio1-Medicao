import csv
import requests
from datetime import datetime

headers = {"Authorization": "Bearer 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"}
url = 'https://api.github.com/graphql'

query = '''
query {
  search(query: "stars:>100", type: REPOSITORY, first: 20) {
    nodes {
      ... on Repository {
        nameWithOwner
        stargazerCount
        createdAt
        pullRequests(states: MERGED) {
            totalCount
          }
        releases(first:0) {
            totalCount
          }
        primaryLanguage {
            name
          }
        closedIssues: issues (states: CLOSED){
            totalCount
          }
      }
    }
  }
}
'''

response = requests.post(url, headers=headers, json={"query": query})

data = response.json()['data']['search']['nodes']

with open('repos.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['nameWithOwner', 'stargazerCount', 'createdAt', 'pullRequests', 'releases', 'primaryLanguage',
                  'closedIssues']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for repo in data:
        writer.writerow({'nameWithOwner': repo['nameWithOwner'], 'stargazerCount': repo['stargazerCount'],
                         'createdAt': repo['createdAt'], 'pullRequests': repo['pullRequests'],
                         'releases': repo['releases'], 'primaryLanguage': repo['primaryLanguage'],
                         'closedIssues': repo['closedIssues']})


