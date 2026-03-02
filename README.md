# Desigualdade Informacional e Acesso à Internet no Brasil

## Título do Projeto
**Desigualdade Informacional e Vulnerabilidade Digital no Brasil: Uma Análise com Microdados da PNAD Contínua TIC**

## Objetivo do Projeto
Este projeto tem como objetivo investigar as desigualdades regionais, socioeconômicas e demográficas no acesso e uso da internet no Brasil. A análise é realizada a partir dos microdados da Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD Contínua) Suplemento Tecnologia da Informação e Comunicação (TIC), visando identificar padrões de vulnerabilidade informacional e digital.

Os objetivos específicos incluem:
*   Medir a desigualdade no acesso à internet em diferentes estratos sociais e geográficos.
*   Identificar grupos populacionais com maior vulnerabilidade digital.
*   Estimar modelos estatísticos para explicar os fatores determinantes do acesso e uso da internet.
*   Mapear heterogeneidades regionais no acesso à internet.
*   Produzir evidências quantitativas que possam subsidiar políticas públicas de inclusão digital.

## Fonte dos Dados
Os dados utilizados neste projeto são os microdados da **PNAD Contínua - Suplemento TIC (Tecnologia da Informação e Comunicação)**, referentes ao 4º trimestre de 2023, disponibilizados pelo Instituto Brasileiro de Geografia e Estatística (IBGE).

## Metodologia
1.  **Coleta e Preparação dos Dados:** Os microdados foram baixados diretamente do servidor FTP do IBGE. Uma amostra de 1 milhão de registros foi utilizada para o processamento, que incluiu limpeza, recodificação de variáveis e construção de novas variáveis, como a binária de acesso à internet e a categorização regional.
2.  **Análise Exploratória:** Foram calculadas estatísticas descritivas ponderadas para analisar a taxa de acesso à internet por região, cor/raça e decis de rendimento. Gráficos de barras e de linha foram gerados para visualizar essas desigualdades.
3.  **Modelagem Estatística:** Um modelo de Regressão Logística foi estimado para avaliar a probabilidade de acesso à internet em função de variáveis como renda (logaritmizada), idade, sexo, raça e região. Os Odds Ratios foram calculados para interpretar a magnitude do efeito de cada variável.

## Resultados Principais
O relatório técnico detalhado (`relatorio_final.pdf`) apresenta as conclusões completas, mas os principais achados incluem:
*   **Disparidades Regionais:** Regiões Norte e Nordeste apresentam as menores taxas de acesso à internet.
*   **Impacto da Renda:** A renda é um dos fatores mais críticos, com uma forte correlação positiva com o acesso à internet.
*   **Vulnerabilidade Étnico-Racial:** Populações indígenas demonstram uma exclusão digital significativamente maior em comparação com outros grupos.
*   **Fator Idade:** A idade é um preditor negativo do acesso, indicando uma vulnerabilidade geracional.

## Estrutura do Repositório
*   `PNADC_2023_trimestre4_20251010.zip`: Arquivo original dos microdados (compactado).
*   `dicionario_PNADC_microdados_trimestre4_20251010.xls`: Dicionário de variáveis dos microdados.
*   `input_PNADC_trimestre4_20251010.txt`: Arquivo de input para leitura dos dados.
*   `pnad_processed_sample.csv`: Amostra dos dados processados e limpos.
*   `process_pnad.py`: Script Python para processamento e limpeza dos microdados.
*   `analyze_pnad.py`: Script Python para análise exploratória e geração de gráficos.
*   `model_pnad.py`: Script Python para modelagem de regressão logística.
*   `acesso_regiao.png`: Gráfico da taxa de acesso à internet por região.
*   `acesso_raca.png`: Gráfico da taxa de acesso à internet por cor/raça.
*   `acesso_renda.png`: Gráfico da taxa de acesso à internet por decil de rendimento.
*   `model_summary.txt`: Sumário completo do modelo de regressão logística.
*   `odds_ratios.csv`: Tabela com os Odds Ratios do modelo.
*   `relatorio_final.md`: Relatório técnico em formato Markdown.
*   `relatorio_final.pdf`: Relatório técnico final em formato PDF.

## Como Reproduzir a Análise
1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/mauriciomeira85/Desigualdade-Informacional-e-acesso-a-informacao-digital-nas-regioes-brasileiras-PNAD-Continua.git
    cd Desigualdade-Informacional-e-acesso-a-informacao-digital-nas-regioes-brasileiras-PNAD-Continua
    ```
2.  **Instale as Dependências:**
    ```bash
    pip install pandas numpy matplotlib seaborn statsmodels
    ```
3.  **Execute os Scripts:**
    *   Para processar os dados:
        ```bash
        python process_pnad.py
        ```
    *   Para realizar a análise exploratória e gerar os gráficos:
        ```bash
        python analyze_pnad.py
        ```
    *   Para rodar o modelo de regressão logística:
        ```bash
        python model_pnad.py
        ```

## Autor
Maurício Almeida Meira

---
*Este projeto foi desenvolvido como parte de uma análise sobre desigualdade informacional no Brasil.*
