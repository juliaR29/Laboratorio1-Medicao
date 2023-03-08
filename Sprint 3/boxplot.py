import pandas as pd
import matplotlib.pyplot as plt
import traceback

# Lê o arquivo CSV e converte para um dataframe
df = pd.read_csv('dadosTratadosCsv.csv', sep=';')

# Seleciona as colunas que serão usadas no boxplot
# colocar o nome da coluna desejada
data = df[['issuesRatio']]




fig, ax = plt.subplots()
try:
    ax.boxplot(data.values, labels=data.columns)
except Exception as e:
    traceback.print_exc()

ax.set_title('Distribuição dos dados')
plt.show()



