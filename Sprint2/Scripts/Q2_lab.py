import time

import requests

headers = {"Authorization": "Bearer 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"}
url = 'https://api.github.com/graphql'

search_string = "is:pr is:merged repo:org_name/*"
page_size = 100

query = '''
query($queryString: String!, $cursor: String) {
  search(query: $queryString, type: ISSUE, first: $pageSize, after: $cursor) {
    issueCount
    edges {
      node {
        ... on PullRequest {
          id
        }
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
'''

endCursor = None

pr_ids = []

while True:
    variables = {"queryString": search_string, "pageSize": 100, "cursor": endCursor}
    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    time.sleep(0.5)

    if response.status_code != 200:
        raise ValueError(f'Response error: {response.status_code}, {response.text}')

    try:
        data = response.json()['data']
    except KeyError:
        raise ValueError(f"Resposta JSON inválida: {response.text}")

    pr_edges = data['search']['edges']
    pr_ids += [edge['node']['id'] for edge in pr_edges]
    has_next_page = data['search']['pageInfo']['hasNextPage']
    endCursor = data['search']['pageInfo']['endCursor']

    if has_next_page:
        print(f"Buscando próxima página (endCursor={endCursor})...")
    else:
        print("Nenhuma página foi encontrada.")
        break

print(f"Total de pull requests encontradas: {len(pr_ids)} .")
