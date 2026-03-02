import pandas as pd
import numpy as np

# Posições corrigidas baseadas no input_PNADC_trimestre4_20251010.txt
# @0001 Ano $4. -> (0, 4)
# @0006 UF $2. -> (5, 7)
# @0050 V1028 15. -> (49, 64)
# @0095 V2007 $1. -> (94, 95)
# @0104 V2009 3. -> (103, 106)
# @0107 V2010 $1. -> (106, 107)
# @0223 V403412 8. -> (222, 230)
# @0508 S07001 $1. -> (507, 508) (Acesso Geral Internet)
# @0510 S070021 $1. -> (509, 510) (Internet PC)
# @0512 S070023 $1. -> (511, 512) (Internet Celular)
# @0513 S070024 $1. -> (512, 513) (Internet TV)
# @0540 S07006 $1. -> (539, 540) (Tem celular pessoal)

cols = [
    ('Ano', 0, 4),
    ('UF', 5, 7),
    ('Peso', 49, 64),
    ('Sexo', 94, 95),
    ('Idade', 103, 106),
    ('Raca', 106, 107),
    ('Rendimento', 222, 230),
    ('Acesso_Internet_Geral', 507, 508),
    ('Internet_PC', 509, 510),
    ('Internet_Celular', 511, 512),
    ('Internet_TV', 512, 513),
    ('Tem_Celular', 539, 540)
]

col_names = [c[0] for c in cols]
col_specs = [(c[1], c[2]) for c in cols]

print("Lendo microdados (amostra de 1 milhão de linhas)...")
df = pd.read_fwf('/home/ubuntu/pnad_tic/PNADC_2023_trimestre4.txt', 
                 colspecs=col_specs, 
                 names=col_names, 
                 nrows=1000000)

# Limpeza e Recodificação
df['Idade'] = pd.to_numeric(df['Idade'], errors='coerce')
df['Rendimento'] = pd.to_numeric(df['Rendimento'], errors='coerce')
df['Peso'] = pd.to_numeric(df['Peso'], errors='coerce')

# Criar variável binária de acesso à internet
# Na PNAD, 1 = Sim, 2 = Não
df['Acesso_Internet'] = np.where(df['Acesso_Internet_Geral'] == 1, 1, 0)

# Mapear UF para Região
uf_to_region = {
    11: 'Norte', 12: 'Norte', 13: 'Norte', 14: 'Norte', 15: 'Norte', 16: 'Norte', 17: 'Norte',
    21: 'Nordeste', 22: 'Nordeste', 23: 'Nordeste', 24: 'Nordeste', 25: 'Nordeste', 26: 'Nordeste', 27: 'Nordeste', 28: 'Nordeste', 29: 'Nordeste',
    31: 'Sudeste', 32: 'Sudeste', 33: 'Sudeste', 35: 'Sudeste',
    41: 'Sul', 42: 'Sul', 43: 'Sul',
    50: 'Centro-Oeste', 51: 'Centro-Oeste', 52: 'Centro-Oeste', 53: 'Centro-Oeste'
}
df['Regiao'] = df['UF'].map(uf_to_region)

# Salvar amostra processada
df.to_csv('/home/ubuntu/pnad_tic/pnad_processed_sample.csv', index=False)
print("Processamento concluído. Amostra salva.")
