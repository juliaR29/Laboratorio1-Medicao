
import requests        //biblioteca para requisição

headers = {"Authorization": "Bearer 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"}      // header com token do git hub
url = 'https://api.github.com/graphql'

query = """      
query { 
  search(
    type: #escolherTipo,
    query: "stars:>100"
    first: 100
  ) {
    edges{
      node{  
        ... on Repository {
          #parâmetros
        }
      }
    },
  }
}
"""

response = requests.post(url, headers=headers, json={"query": query})    // requisição para o graphQL
data = response.json()  

for i, repo in enumerate(data["data"]["search"]["edges"]):    // imprimindo resultados no terminal

...    // print com as variaveis e/ou parâmetros



