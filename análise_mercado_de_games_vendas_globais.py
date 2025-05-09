# -*- coding: utf-8 -*-
"""Análise Mercado de Games - Vendas Globais.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fjyQ9piBkINNZmrU1-cWNNyWmpm_HbwG

# Lendo e Tratando os dados
"""

#Importando Bibliotecas
#Bibliotecas para modelagem e matrizes
import numpy as np
import pandas as pd

#Biliotecas para análises gráficas
import matplotlib.pyplot as plt
import seaborn as sns

#Biblioteca para ignorar avisos
import warnings

#Desabilitanto avisos
warnings.filterwarnings('ignore')

Base_Dados = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Projetos Práticos - Curso DataV/ Projeto Análise Mercado de Games/Video_Games_Sales_as_at_22_Dec_2016.csv')

Base_Dados.head()

#Obtendo a dimensão da base de dados (Linhas e colunas)
Base_Dados.shape

#Analisando campos nulos na base de dados
Base_Dados.isnull().sum()

#Visualização gráfica dos campos nulos
plt.figure(figsize=(15,5))
sns.heatmap(Base_Dados.isnull(), cbar=False, cmap='viridis');

#Removendo colunas
Base_Dados.drop(['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer',	'Rating'], axis=1, inplace=True)

Base_Dados.head()

#Renomeando colunas
Base_Dados.rename( columns={
    'Name' : 'Nome',
    'Platform' : 'Plataforma',
    'Year_of_Release' : 'Ano_Lancamento',
    'Genre' : 'Genero',
    'Publisher' : 'Publicadora',
    'NA_Sales': 'Vendas_America_Norte',
    'EU_Sales': 'Vendas_Europa',
    'JP_Sales': 'Vendas_Japao',
    'Other_Sales': 'Vendas_Outras_Regioes',
    'Global_Sales': 'Vendas_Global'
}, inplace=True )
Base_Dados.head()

#Removendo as linhas com valores nulos da coluna Ano_Lancamento
Base_Dados.dropna(subset=['Ano_Lancamento'], inplace=True)

"""# Análise Gráfica"""

#Criando uma paleta de cores para os gráficos
Paleta_Cores = sns.color_palette('Set2', 10)
Paleta_Cores

#Criando um dataframe que agrupa as vendas globais de jogos
Analise_Jogos = Base_Dados.groupby(['Nome'])['Vendas_Global'].sum().reset_index()
#Organizando o dataframe análise em ordem
Analise_Jogos.sort_values(by='Vendas_Global', ascending=False, inplace=True)
Analise_Jogos.reset_index(drop=True, inplace=True)
Analise_Jogos.head()

#Criando gráfico
#Tamanho da Imagem
plt.figure(figsize=(15,5))

#Título
plt.title('Top 5 Jogos mais vendidos globalmente', loc='left', fontsize=14)

#Gráfico de barras usando as vendas globais de jogos
ax = sns.barplot(data=Analise_Jogos.head(5), x='Nome', y='Vendas_Global', ci=None, color=Paleta_Cores[0], estimator=sum)
ax.bar_label(ax.containers[0], fmt='%.2fM', fontsize=10)
#Label
plt.ylabel('Quantidade de vendas (em milhões)');

#Criando um dataframe que agrupa as vendas globais por plataforma
Analise_Plataformas = Base_Dados.groupby(['Plataforma'])['Vendas_Global'].sum().reset_index()

# Convertendo de milhões para bilhões
Analise_Plataformas['Vendas_Global'] = Analise_Plataformas['Vendas_Global'] / 1000

#Organizando o dataframe análise em ordem
Analise_Plataformas.sort_values(by='Vendas_Global', ascending=False, inplace=True)
Analise_Plataformas.head()

#Criando gráfico
#Tamanho da Imagem
plt.figure(figsize=(15,5))

#Título
plt.title('Top 5 plataformas com mais jogos vendidos', loc='left', fontsize=14)

#Gráfico de barras usando as vendas globais por plataformas
ax = sns.barplot(data=Analise_Plataformas.head(5), x='Plataforma', y='Vendas_Global', ci=None, color=Paleta_Cores[3], estimator=sum)
ax.bar_label(ax.containers[0], fmt='%.2fB', fontsize=10)
#Label
plt.ylabel('Quantidade de vendas (em bilhões)');

#Criando um dataframe que agrupa as vendas globais de jogos por gênero
Analise_Generos = Base_Dados.groupby(['Genero'])['Vendas_Global'].sum().reset_index()
#Organizando o dataframe análise em ordem
Analise_Generos.sort_values(by='Vendas_Global', ascending=False, inplace=True)

# Convertendo de milhões para bilhões
Analise_Generos['Vendas_Global'] = Analise_Generos['Vendas_Global'] / 1000

Analise_Generos.reset_index(drop=True, inplace=True)
Analise_Generos.head()

#Tamanho da Imagem
plt.figure(figsize=(15,5))

#Título
plt.title('Top 5 Gêneros mais vendidos', loc='left', fontsize=14)

#Gráfico de barras usando as vendas por gênero
ax = sns.barplot(data=Analise_Generos.head(5), x='Genero', y='Vendas_Global', ci=None, color=Paleta_Cores[2], estimator=sum)
ax.bar_label(ax.containers[0], fmt='%.2fB', fontsize=10)
#Label
plt.ylabel('Quantidade de vendas (Em bilhões)');

#Criando um dataframe que agrupa as vendas globais por publicadora
Analise_Publicadoras = Base_Dados.groupby(['Publicadora'])['Vendas_Global'].sum().reset_index()
#Organizando o dataframe análise em ordem
Analise_Publicadoras.sort_values(by='Vendas_Global', ascending=False, inplace=True)
Analise_Publicadoras.reset_index(drop=True, inplace=True)
Analise_Publicadoras.head()

# Plot geral do Top 5 Publicadoras
plt.figure(figsize=(15, 6))
plt.title('Top 5 Publicadoras com mais vendas')
plt.pie(
    Analise_Publicadoras['Vendas_Global'].head(5),  #Apenas os 5 primeiros registros da coluna de vendas globais
    labels=Analise_Publicadoras['Publicadora'].head(5),  #Apenas os 5 primeiros valores da coluna plataforma
    startangle=90,
    autopct='%1.1f%%',
    colors=Paleta_Cores,
);

"""# Análise Geral - Vendas por Região"""

#Criando um dataframe que agrupa as vendas globais de jogos por região
Analise_Global = Base_Dados.groupby(['Ano_Lancamento'])[['Vendas_America_Norte', 'Vendas_Europa', 'Vendas_Japao', 'Vendas_Outras_Regioes', 'Vendas_Global']].sum()
Analise_Global.head()

#Barras do gráfico
America = Analise_Global['Vendas_America_Norte'].sum()/1000 #America recebera a soma de todas as vendas em Vendas_America_Norte e converte para bilhões
Europa = Analise_Global['Vendas_Europa'].sum()/1000
Japao = Analise_Global['Vendas_Japao'].sum()/1000
Outras_Regioes = Analise_Global['Vendas_Outras_Regioes'].sum()/1000

Largura_Barra = 0.85
Rotulos = ['América do Norte', 'Europa', 'Japão', 'Outras Regiões']
Valores = [America, Europa, Japao, Outras_Regioes]

#Tamanho da Imagem
plt.figure(figsize=(15,5))

#Título
plt.title('Vendas de jogos por Região', loc='left', fontsize=14)

for i in range(len(Rotulos)):
    plt.bar(Rotulos[i], Valores[i], label=Rotulos[i], width=Largura_Barra, color=Paleta_Cores[i])
    plt.text(Rotulos[i], Valores[i] + 0, f'{Valores[i]:.2f}B', ha='center', va='bottom', fontsize=10)

plt.xlabel('Região')
plt.ylabel('Quantidade de vendas (Em bilhões)')
plt.grid(False);

#Df para armazenar as vendas por publicadoras ao longo dos anos
publicadoras = ['Nintendo', 'Electronic Arts', 'Activision', 'Sony Computer Entertainment', 'Ubisoft']

# Criando um dicionário para armazenar os DataFrames processados
Dicionario_Publicadoras = {}

for publicadora in publicadoras:
    df = (Base_Dados[Base_Dados['Publicadora'] == publicadora]
          .groupby('Ano_Lancamento')['Vendas_Global']
          .sum()
          .reset_index()
          .set_index('Ano_Lancamento'))

    Dicionario_Publicadoras[publicadora] = df

#Criando gráfico de linhas com as vendas das publicadoras ao longo dos anos utilizando o dicionário criado na célula anterior

# Criando a figura e o eixo
plt.figure(figsize=(12, 6))

# Percorrendo o dicionário e plotando cada publicadora
for publicadora, df in Dicionario_Publicadoras.items():
    plt.plot(df.index, df['Vendas_Global'], label=publicadora, color=Paleta_Cores[publicadoras.index(publicadora)], linewidth=2.5)

# Personalizando o gráfico
plt.xlabel('Ano de Lançamento')
plt.ylabel('Vendas Globais (milhões)')
plt.title('Vendas Globais por Publicadora')
plt.legend()  # Adiciona legenda para diferenciar as publicadoras

# Exibir o gráfico
plt.show()

"""# Relatório final"""

# Tamanho da Imagem
fig, ax = plt.subplots( figsize=(18, 15) )
plt.xticks(fontsize=0) #Removendo os valores dos eixos x e y que o subplots cria por padrão, para que fiquem somente os valores dos gráficos criados abaixo
plt.yticks(fontsize=0)

# Cor de fundo
Cor_Fundo = '#f5f5f5'
ax.set_facecolor( Cor_Fundo )
fig.set_facecolor( Cor_Fundo )


# Titulo da figura
plt.suptitle('Projeto Prático \n Análise do Mercado de Games - Vendas de jogos (1980 a 2020)', fontsize=22, color='#404040', fontweight=600)

# Parametros para o grid
Linhas = 3
Colunas = 2

# Acessando gráfico 1
plt.subplot(Linhas, Colunas, 1)
plt.title('Top 5 Jogos mais vendidos globalmente', loc='left', fontsize=14)
ax = sns.barplot(data=Analise_Jogos.head(5), x='Nome', y='Vendas_Global', ci=None, color=Paleta_Cores[0], estimator=sum)
ax.bar_label(ax.containers[0], fmt='%.2fM', fontsize=10)
plt.ylabel('Quantidade de vendas (Em milhões)');


# Acessando gráfico 2
plt.subplot(Linhas, Colunas, 2)
plt.title('Top 5 plataformas com mais jogos vendidos', loc='left', fontsize=14)
ax = sns.barplot(data=Analise_Plataformas.head(5), x='Plataforma', y='Vendas_Global', ci=None, color=Paleta_Cores[3], estimator=sum)
ax.bar_label(ax.containers[0], fmt='%.2fB', fontsize=10)
plt.ylabel('Quantidade de vendas (Em bilhões)')



# Acessando gráfico 3
plt.subplot(Linhas, Colunas, 3)
plt.title('Top 5 Gêneros mais vendidos', loc='left', fontsize=14)
ax = sns.barplot(data=Analise_Generos.head(5), x='Genero', y='Vendas_Global', ci=None, color=Paleta_Cores[2], estimator=sum)
ax.bar_label(ax.containers[0], fmt='%.2fB', fontsize=10)
plt.ylabel('Quantidade de vendas (Em bilhões)')


# Acessando gráfico 4
plt.subplot(Linhas, Colunas, 4)
plt.title('Vendas de jogos por Região', loc='left', fontsize=14)

for i in range(len(Rotulos)):
    plt.bar(Rotulos[i], Valores[i], label=Rotulos[i], width=Largura_Barra, color=Paleta_Cores[i])
    plt.text(Rotulos[i], Valores[i] + 0, f'{Valores[i]:.2f}B', ha='center', va='bottom', fontsize=10)

plt.xlabel('Região')
plt.ylabel('Quantidade de vendas (Em bilhões)')
plt.grid(False)

# Acessando gráfico 5
plt.subplot(Linhas, Colunas, 5)
plt.title('Top 5 Publicadoras com mais vendas')
plt.pie(
    Analise_Publicadoras['Vendas_Global'].head(5),  #Apenas os 5 primeiros registros da coluna de vendas globais
    labels=Analise_Publicadoras['Publicadora'].head(5),  #Apenas os 5 primeiros valores da coluna plataforma
    startangle=90,
    autopct='%1.1f%%',
    colors=Paleta_Cores,
)


# Acessando gráfico 6
plt.subplot(Linhas, Colunas, 6)
for publicadora, df in Dicionario_Publicadoras.items():
    plt.plot(df.index, df['Vendas_Global'], label=publicadora, color=Paleta_Cores[publicadoras.index(publicadora)], linewidth=2.5)
plt.xlabel('Ano de Lançamento')
plt.ylabel('Quantidade de vendas (mi)')
plt.title('Vendas Globais por Publicadora', loc='left', fontsize=14)
plt.legend()
plt.grid(False)


# Ajustar o layout
plt.subplots_adjust( hspace=0.4, wspace=0.3 )

#Rodapé
Rodape = '''
Esse relatório foi elaborado por Jeferson da Silva Carmo
@jefersoncarmoo
'''

# Incluindo o rodape no relatorio
fig.text( 0.5, -0.02, Rodape, ha='center', va='bottom', size=12, color='#938ca1');