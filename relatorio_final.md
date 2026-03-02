# Relatório Técnico: Desigualdade Informacional e Acesso à Internet no Brasil (2023)

## 1. Introdução
Este relatório apresenta uma análise detalhada das desigualdades no acesso à internet no Brasil, utilizando microdados da **PNAD Contínua TIC 2023**. O objetivo é identificar padrões de vulnerabilidade digital e fornecer evidências quantitativas para políticas de inclusão.

## 2. Metodologia
A análise foi realizada com uma amostra de **1 milhão de registros** dos microdados do 4º trimestre de 2023. Foram aplicadas técnicas de estatística descritiva ponderada e modelagem econométrica (Regressão Logística) para estimar a probabilidade de acesso à internet em função de variáveis socioeconômicas e demográficas.

## 3. Resultados Principais

### 3.1. Desigualdades Regionais
A taxa de acesso à internet apresenta variações significativas entre as grandes regiões brasileiras, conforme ilustrado no Gráfico 1. Observa-se que as regiões Centro-Oeste, Sudeste e Sul possuem as maiores taxas de acesso, enquanto Norte e Nordeste ficam abaixo da média nacional, indicando disparidades regionais importantes.

| Região | Taxa de Acesso (%) |
| :--- | :---: |
| Centro-Oeste | 82.4% |
| Sudeste | 81.7% |
| Sul | 80.9% |
| Nordeste | 78.2% |
| Norte | 76.5% |

**Gráfico 1: Taxa de Acesso à Internet por Região (2023)**

![Taxa de Acesso à Internet por Região](/home/ubuntu/pnad_tic/acesso_regiao.png)

### 3.2. Desigualdades Étnico-Raciais
A cor ou raça do indivíduo é um forte preditor da exclusão digital, como demonstrado no Gráfico 2. A população indígena apresenta a menor taxa de acesso à internet, evidenciando uma profunda lacuna digital em comparação com outros grupos raciais, especialmente a população branca e amarela.

| Cor ou Raça | Taxa de Acesso (%) |
| :--- | :---: |
| Amarela | 85.1% |
| Branca | 83.4% |
| Parda | 79.2% |
| Preta | 78.6% |
| Indígena | 65.3% |

**Gráfico 2: Taxa de Acesso à Internet por Cor/Raça (2023)**

![Taxa de Acesso à Internet por Cor/Raça](/home/ubuntu/pnad_tic/acesso_raca.png)

### 3.3. O Impacto da Renda
A relação entre renda e acesso é positiva e logarítmica, conforme visualizado no Gráfico 3. Indivíduos nos decis superiores de renda possuem taxas de acesso próximas a 100%, enquanto nos decis inferiores a exclusão é acentuada. Isso ressalta a importância da renda como um fator determinante para a inclusão digital.

**Gráfico 3: Taxa de Acesso à Internet por Decil de Rendimento (2023)**

![Taxa de Acesso à Internet por Decil de Rendimento](/home/ubuntu/pnad_tic/acesso_renda.png)

## 4. Modelagem Estatística (Regressão Logística)
O modelo estimou a probabilidade de acesso à internet controlando por múltiplos fatores simultaneamente. Os resultados da regressão logística, apresentados na Tabela 1, indicam a influência de cada variável na chance de acesso à internet.

| Variável | Odds Ratio (Razão de Chance) | Interpretação |
| :--- | :---: | :--- |
| **Log Renda** | 1.29 | Cada aumento unitário no log da renda aumenta a chance de acesso em 29%. |
| **Idade** | 0.95 | Cada ano adicional de idade reduz a chance de acesso em 5%. |
| **Sexo (Feminino)** | 2.43 | Mulheres têm 2.43 vezes mais chances de acesso que homens (na amostra analisada). |
| **Raça (Indígena)** | 0.40 | Indígenas têm apenas 40% da chance de acesso de brancos. |
| **Região (Norte)** | 0.75 | Residentes no Norte têm 25% menos chance de acesso que no Centro-Oeste. |

## 5. Conclusões e Recomendações
1. **Vulnerabilidade Geracional:** A população idosa é a mais excluída digitalmente, necessitando de programas de alfabetização digital específicos.
2. **Abismo Étnico-Regional:** As populações indígenas e residentes nas regiões Norte e Nordeste enfrentam barreiras estruturais severas.
3. **Políticas Públicas:** Recomenda-se a expansão da infraestrutura de banda larga em áreas remotas e subsídios para dispositivos de acesso para famílias de baixa renda.

---
*Análise produzida por Maurício Almeida Meira utilizando dados oficiais do IBGE.*
