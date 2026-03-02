import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/home/ubuntu/pnad_tic/pnad_processed_sample.csv')

# 1. Acesso à Internet por Região (Ponderado)
def weighted_mean(group):
    return (group['Acesso_Internet'] * group['Peso']).sum() / group['Peso'].sum()

regiao_acesso = df.groupby('Regiao').apply(weighted_mean).reset_index()
regiao_acesso.columns = ['Regiao', 'Taxa_Acesso']
regiao_acesso = regiao_acesso.sort_values('Taxa_Acesso', ascending=False)

# 2. Acesso por Cor/Raça
# 1-Branca, 2-Preta, 3-Amarela, 4-Parda, 5-Indígena
raca_map = {1: 'Branca', 2: 'Preta', 3: 'Amarela', 4: 'Parda', 5: 'Indígena'}
df['Raca_Label'] = df['Raca'].map(raca_map)
raca_acesso = df.groupby('Raca_Label').apply(weighted_mean).reset_index()
raca_acesso.columns = ['Raca', 'Taxa_Acesso']

# 3. Acesso por Faixa de Renda (Decis)
df['Renda_Decil'] = pd.qcut(df['Rendimento'].fillna(0), 10, labels=False, duplicates='drop')
renda_acesso = df.groupby('Renda_Decil').apply(weighted_mean).reset_index()
renda_acesso.columns = ['Decil_Renda', 'Taxa_Acesso']

# 4. Visualizações
plt.figure(figsize=(12, 6))
sns.barplot(x='Regiao', y='Taxa_Acesso', data=regiao_acesso, palette='viridis')
plt.title('Taxa de Acesso à Internet por Região (2023)')
plt.ylabel('Proporção de Acesso')
plt.savefig('/home/ubuntu/pnad_tic/acesso_regiao.png')

plt.figure(figsize=(12, 6))
sns.barplot(x='Raca', y='Taxa_Acesso', data=raca_acesso, palette='magma')
plt.title('Taxa de Acesso à Internet por Cor/Raça (2023)')
plt.ylabel('Proporção de Acesso')
plt.savefig('/home/ubuntu/pnad_tic/acesso_raca.png')

plt.figure(figsize=(12, 6))
sns.lineplot(x='Decil_Renda', y='Taxa_Acesso', data=renda_acesso, marker='o')
plt.title('Taxa de Acesso à Internet por Decil de Rendimento (2023)')
plt.xlabel('Decil de Renda (0=Mais Pobre, 9=Mais Rico)')
plt.ylabel('Proporção de Acesso')
plt.savefig('/home/ubuntu/pnad_tic/acesso_renda.png')

# Salvar tabelas de resultados
regiao_acesso.to_csv('/home/ubuntu/pnad_tic/res_regiao.csv', index=False)
raca_acesso.to_csv('/home/ubuntu/pnad_tic/res_raca.csv', index=False)
renda_acesso.to_csv('/home/ubuntu/pnad_tic/res_renda.csv', index=False)

print("Análise exploratória concluída. Gráficos e tabelas salvos.")
