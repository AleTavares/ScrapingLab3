# Imports para manipulação, visualização e análise de dados
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg

# Carrega o arquivo csv com o conteúdo do web scraping
df_nba = pd.read_csv('dados/nba.csv')

# Visualiza uma amostra dos dados
print(df_nba.head(10))

# Idade média dos jogadores
print('Qual a idade média dos jogadores que disputaram a temporada 2019/2020 da NBA?')
print(df_nba['Age'].mean())

print('A idade média foi de 25 anos. Vamos criar um histograma e analisar a distribuição da variável idade.')
# Histograma
df_nba['Age'].plot.hist(bins=12, alpha=0.5)
plt.show()

# BoxPlot
ax = sns.boxplot(x = df_nba['Age'], palette = "Set2", orient = "h")
plt.ylabel('\nAtletas')
plt.xlabel('\nIdade')
plt.show()

# Teste de normalidade com Pingouin
x = df_nba['Age']
print(pg.normality(x))

# Agrupando os dados por jogador e total de pontos
df_nba_top10 = df_nba.groupby(['Player'])['PTS'].sum().reset_index().rename(columns = {'PTS': 'Total_Pontos'})

# Retornamos os Top 10
df_nba_top10 = df_nba_top10.nlargest(10, 'Total_Pontos')

# Visualiza os dados
print(df_nba_top10)

# Quantos jogos os jogadores com 35 anos de idade ou mais iniciaram (variável GS)?
def lista_jogadores35():
    print('\nJogadores com 35 ou mais anos de idade e jogos disputados.\n')
    print('Jogador:          | Jogos:')
    print('------------------+--------')
    for index, row in df_nba.iterrows():
        if row['Age'] >= 35:
            print('{:<17} | {:>6}'.format(row['Player'], row['GS']))

print(lista_jogadores35())

# Gráfico que mostra a relação entre rebotes ofensivos e minutos jogados.
# Função
def gera_grafico_reb_ofensivos():
    plt.figure(figsize = [10,10])
    sns.set()
    sns.regplot(x = df_nba['MP'], y = df_nba['ORB'], color = '#AA2F2F', marker = '+')
    plt.xlabel('\nMinutos Jogados (por jogo)\n', fontsize = 14, color = 'black')
    plt.ylabel('\nRebotes Ofensivos (por jogo)\n', fontsize = 14, color = 'black')
    plt.title('\nMinutos Jogados x Rebotes Ofensivos\n', fontsize = 20)
    plt.show()

print(gera_grafico_reb_ofensivos())

# Gráfico que mostra a relação entre rebotes defensivos e minutos jogados.
# Função
def gera_grafico_reb_defensivos():
    plt.figure(figsize = [10,10])
    sns.set()
    sns.regplot(x = df_nba['MP'], y = df_nba['DRB'], color = '#F244AA', marker = '*')
    plt.xlabel('\nMinutos Jogados (por jogo)\n', fontsize = 14, color = 'black')
    plt.ylabel('\nRebotes Defensivos (por jogo)\n', fontsize = 14, color = 'black')
    plt.title('\nMinutos Jogados x Rebotes Defensivos\n', fontsize = 20)
    plt.show()

print(gera_grafico_reb_defensivos())