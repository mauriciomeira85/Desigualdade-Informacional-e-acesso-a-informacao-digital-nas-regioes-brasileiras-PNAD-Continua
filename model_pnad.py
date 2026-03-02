import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_csv('/home/ubuntu/pnad_tic/pnad_processed_sample.csv')

# Preparar dados para o modelo
# Filtrar apenas quem tem rendimento e idade válida
df_model = df.dropna(subset=['Rendimento', 'Idade', 'Regiao', 'Sexo', 'Raca', 'Acesso_Internet']).copy()

# Recodificar variáveis categóricas
df_model['Sexo'] = df_model['Sexo'].astype(str)
df_model['Raca'] = df_model['Raca'].astype(str)
df_model['Regiao'] = df_model['Regiao'].astype(str)

# Modelo de Regressão Logística: Probabilidade de ter acesso à internet
# Variáveis: Renda (log), Idade, Sexo, Raça, Região
df_model['log_renda'] = np.log1p(df_model['Rendimento'])

model = smf.logit('Acesso_Internet ~ log_renda + Idade + C(Sexo) + C(Raca) + C(Regiao)', data=df_model).fit()

# Salvar sumário do modelo
with open('/home/ubuntu/pnad_tic/model_summary.txt', 'w') as f:
    f.write(model.summary().as_text())

# Calcular Odds Ratios
params = model.params
conf = model.conf_int()
conf['Odds Ratio'] = params
conf.columns = ['5%', '95%', 'Odds Ratio']
odds_ratios = np.exp(conf)
odds_ratios.to_csv('/home/ubuntu/pnad_tic/odds_ratios.csv')

print("Modelagem concluída. Sumário e Odds Ratios salvos.")
