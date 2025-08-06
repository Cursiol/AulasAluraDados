# Aula 01.1 - Analise da dados com Pandas

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df.head(15)

df.info()

df.describe()

df.shape

linhas, colunas = df.shape[0], df.shape[1]
print ("linhas: ", linhas)
print ("colunas: ", colunas)

df.columns

# Translate column names
df.columns = [
    'ano', 'experiencia', 'contrato', 'cargo',
    'salario', 'moeda', 'usd', 'residencia',
    'remoto', 'empresa', 'tamanho_empresa'
]

print("Column names translated successfully.")
display(df.columns)

df.columns

df['contrato'].value_counts()

df['experiencia'].value_counts()

df['remoto'].value_counts()

df['tamanho_empresa'].value_counts()

# Translate values in the 'contrato' column
df['contrato'] = df['contrato'].replace({
    'FT': 'Tempo Integral',
    'CT': 'Contrato',
    'PT': 'Tempo Parcial',
    'FL': 'Freelancer'
})

print("Values in 'contrato' column translated successfully.")
display(df['contrato'].value_counts())

# Translate values in the 'experiencia' column
df['experiencia'] = df['experiencia'].replace({
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
})

print("Values in 'experiencia' column translated successfully.")
display(df['experiencia'].value_counts())

# Translate values in the 'remoto' column
df['remoto'] = df['remoto'].replace({
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
})

print("Values in 'remoto' column translated successfully.")
display(df['remoto'].value_counts())

# Translate values in the 'tamanho_empresa' column
df['tamanho_empresa'] = df['tamanho_empresa'].replace({
    'S': 'Pequena',
    'M': 'Média',
    'L': 'Grande'
})

print("Values in 'tamanho_empresa' column translated successfully.")
display(df['tamanho_empresa'].value_counts())

df.head(15)

# Display the most frequent job titles
display(df['cargo'].value_counts().head(20))

df.describe(include='object')

df.describe()

import matplotlib.pyplot as plt
import seaborn as sns

# Calculate the average salary for each job title
average_salaries = df.groupby('cargo')['usd'].mean().sort_values(ascending=False)

# Select the top N job titles for better visualization (optional)
top_n = 20
average_salaries = average_salaries.head(top_n)

# Create the bar chart
plt.figure(figsize=(12, 8))
sns.barplot(x=average_salaries.index, y=average_salaries.values, palette='viridis')
plt.xticks(rotation=90)
plt.xlabel('Cargo')
plt.ylabel('Média Salarial (USD)')
plt.title('Média Salarial por Cargo (Top 20)')
plt.tight_layout()
plt.show()



import matplotlib.pyplot as plt
import pandas as pd

# Count employees by country
country_counts = df['residencia'].value_counts()

# Select top N countries and group the rest as 'Other'
top_n = 10
if len(country_counts) > top_n:
    top_countries = country_counts.head(top_n)
    other_count = country_counts.iloc[top_n:].sum()
    country_data = top_countries._append(pd.Series([other_count], index=['Other']))
else:
    country_data = country_counts

# Create a donut chart
plt.figure(figsize=(10, 10))
plt.pie(country_data, labels=country_data.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))
plt.title('Distribuição de Funcionários por País')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Aula 02 - Limpeza e preparação dos Dados

df.isnull()

# Traz informações da tabela
df.head()

# realizou a soma de todos os dados que não estão preenchidos
df.isnull().sum()

# metodoq para procurar quais linhas estão faltando preencher os dados, comando unique traz quais os valores unicos - NAN (note a number) seguida valor nulo no python
df['ano'].unique()

# traz tudo que é nulo (df.isnull()) 
# e filtrou todos os valors nulos (any(axis = 1))
df[df.isnull().any(axis = 1)]

# criando uma base nova para testar calculos
# numpy é uma biblioteca para modelagem de dados
import numpy as np

#criação de um novo dataFrame, duas colunas contendo nomes e salarios
df_salarios = pd.DataFrame({
    'nome' : ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
    'salario' : [4000, np.nan, 5000, np.nan, 100000]
})

# cria uma coluna para o salario media - o valor é o salario - preenche os valos nulos com a media do salarios e arredonda
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

# agora com mediana, sem arredondar
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())

df_salarios

# cria um dataframe de uma tabela de temperatura dos dias
df_temperaturas = pd.DataFrame({
    "Dia" : ["segunda", "terça", "quarta", "quinta", "sexta"],
    "Temperatura" : [30, np.nan, np.nan, 28, 27]
})

#ffill ele completar com o valor enterior a as celulas da tabela
df_temperaturas["Preenchido_ffill"] = df_temperaturas["Temperatura"].ffill()
df_temperaturas

# cria um dataframe de uma tabela de temperatura dos dias
df_temperaturas = pd.DataFrame({
    "Dia" : ["segunda", "terça", "quarta", "quinta", "sexta"],
    "Temperatura" : [30, np.nan, np.nan, 28, 27]
})

#ffill ele completar com o prixmo valor a as celulas da tabela
df_temperaturas["Preenchido_bfill"] = df_temperaturas["Temperatura"].bfill()
df_temperaturas

#cria uma tabela com nomes e cidades
df_cidades = pd.DataFrame ({
    "nome" : ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
    "Cidade" : ["São Paulo", np.nan , "Belo Horizonte", np.nan, "Rio de Janeiro"]
})

# o fillna preenche com um valor predeterminado nas celular nulas
df_cidades['cidade_preenchida'] = df_cidades["Cidade"].fillna("Não Informado")

df_cidades

df_limpo = df.dropna()

df_limpo.isnull().sum()

df_limpo.head()

df_limpo.info()

df_limpo = df_limpo.assign(ano = df_limpo["ano"].astype("int64"))

df_limpo.head()

df_limpo.info()
