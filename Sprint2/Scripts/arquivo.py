import csv
import requests
from datetime import datetime

headers = {"Authorization": "Bearer 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"}
url = 'https://api.github.com/graphql'

query = '''
query {
  search(query: "stars:>100", type: REPOSITORY, first: 20, after: null) {
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
        issues(first: 1) {
            totalCount
          }
        closedIssues: issues (states: CLOSED){
            totalCount
          }
        updatedAt
      }
    }
    pageInfo {
        endCursor
        hasNextPage
    }
  }
}
'''

count = 0
endCursor = None

with open('script.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['nameWithOwner', 'stargazerCount', 'age', 'pullRequests', 'releases', 'primaryLanguage',
                  'issues', 'closedIssues', 'issuesRatio', 'updatedAt']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    while count < 1000:
        if count > 19:
            query.replace('after: null', 'after: "%s"' % endCursor)

        response = requests.post(url, headers=headers, json={"query": query})
        endCursor = response.json()['data']['search']['pageInfo']['endCursor']

        data = response.json()['data']['search']['nodes']

        for repo in data:
            language = repo['primaryLanguage']['name'] if repo['primaryLanguage'] is not None else ""
            created_at = datetime.strptime(repo['createdAt'], "%Y-%m-%dT%H:%M:%SZ")
            age = (datetime.now() - created_at).days
            issues = repo['issues']['totalCount'] if 'issues' in repo else 0
            closed_issues = repo['closedIssues']['totalCount'] if 'closedIssues' in repo else 0
            issues_ratio = closed_issues / issues if issues != 0 else 'N/A'
            writer.writerow({'nameWithOwner': repo['nameWithOwner'], 'stargazerCount': repo['stargazerCount'],
                             'age': age, 'pullRequests': repo['pullRequests'],
                             'releases': repo['releases'], 'primaryLanguage': repo['primaryLanguage'],
                             'issues': repo['issues'], 'closedIssues': repo['closedIssues'],
                             'issuesRatio': issues_ratio, 'updatedAt': repo['updatedAt']})
            count += 1

