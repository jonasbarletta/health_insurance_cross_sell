# Projeto Insurance All

O Projeto Insurance All é um projeto de Ciências de Dados para a classificação e ranqueamento de possível clientes em uma nova modalidade de seguro da empresa Insurance All.

Esse projeto é uma proposta de Projeto do Aluno (PA), da Comunidade DS, baseado no desafio 'Health Insurance Cross Sell Prediction ' da plataforma Kaggle. O enunciado ofical do problema está disponível em [Kaggle](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction).

# 1 Questão de Negócio

O Contexto a seguir, é completamente fictício, a empresa, o contexto, o CEO, as perguntas de negócio existem somente na minha imaginação. 

A Insurance All é uma empresa que fornece seguro de saúde para seus clientes e o time de produtos está analisando a possibilidade de oferecer aos assegurados, um novo produto: Um seguro de automóveis.

Assim como o seguro de saúde, os clientes desse novo plano de seguro de automóveis precisam pagar um valor anualmente à Insurance All para obter um valor assegurado pela empresa, destinado aos custos de um eventual acidente ou dano ao veículo.

A Insurance All fez uma pesquisa com cerca de 380 mil clientes sobre o interesse em aderir a um novo produto de seguro de automóveis, no ano passado. Todos os clientes demonstraram interesse ou não em adquirir o seguro de automóvel e essas respostas ficaram salvas em um banco de dados junto com outros atributos dos clientes.

O time de produtos selecionou 127 mil novos clientes que não responderam a pesquisa para participar de uma campanha, no qual receberão a oferta do novo produto de seguro de automóveis. A oferta será feita pelo time de vendas através de ligações telefônicas.

Contudo, o time de vendas tem uma capacidade de realizar 20 mil ligações dentro do período da campanha.

# 2 Planejamento da Solução

Para solução do desafio dividimos em algumas etapas cíclicas (como mostra a imagem abaixo) de forma que apresentaremos aqui um cíclo completo dessas etapas. Começando na 'Questão de Negócio' até a 'Avaliação do Algoritmo' onde analisaremos a performance do modelo e decidiremos se é necessário realizar mais um ciclo antes de colocar o 'Modelo em Produção'.

![alt text](https://github.com/jonasbarletta/ds_em_producao/blob/main/img/Questao%20de%20Negocio%20(1).png)

### 2.1 Produto Final
- Insights de negócio realizados a partir da Análise Exploratória de Dados
- Bot no Telegram que indica a previsão de vendas de qualquer loja

## 2.2 Ferramentas Utilizadas
- Python 3.10
- Jupyter Notebook
- Github
- SQLite
- Banco de Dados AWS

Vamos entender um pouco melhor como foi cada etapa do projeto.

# 3 Etapas do Primeiro Ciclo do Projeto

## 3.1 Entendimento do Negócio



## 3.2 Coleta de Dados

Por se tratar de um desafio da plataforma Kaggle, os dados já estão coletados bastando assim acessá-los. Tais dados podem ser acessados pelo. Nessa página estão disponíveis quatro arquivos: 

Os atributos apresentados nos conjunto de dados são:

| Atributo                          | Descrição |  
| --------------------------------  | --------- |
| ID                                | Representa uma loja em  uma data específica que foram relaizadas as vendas |   
| Store                             | Número único de cada loja |
| Sales                             | Total de vendas realizada em dia |
| Date                              | Data |
| DayOfWeek                         | Dia da semana |
| Customers                         | Número de clientes de um dia |
| Open                              | Indica se a loja estava ou não aberta naquela data (0: fechada ou 1: aberta) |
| StateHoliday                      | Indica um feriado de estado (a: public holiday, b: Easter holiday, c: Christmas, 0: None) |
| SchoolHoliday                     | Indica se a loja foi afetada pelo fechamento das escolas públicas naquela data |
| StoreType                         | Diferencia as lojas em quatro tipos: a, b, c, d |
| Assortment                        | Descreve o nível de estoque das lojas (a: basic, b: extra, c: extended) |
| CompetitionDistance               | Distância em metros do competidor mais pŕoximo |
| CompetitionOpenSince[Month/Year]  | A data (mês/ano) aproximada de quando o competidor mais próximo abriu |
| Promo                             | Indica se a lojas está com promoção no dia |
| Promo2                            | É uma promoção contínua e consecutiva para algumas lojas (0: não está participando, 1: está participando) |
| Promo2Since[Year/Week]            | Descreve a semana e ano em que a loja começou a participar da Promo2 |
| PromoInterval                     | Descreve os intervalos consecutivos em que a Promo2 é iniciada, nomeando os meses em que a promoção é iniciada novamente |

Agora que os dados estão coletados partiremos para a limpeza dos dados.

## 3.3 Limpeza dos Dados


## 3.4 Análise Exploratória dos Dados

Aqui começamos fazendo o Mapa Mental de Hipóteses abaixo. Fizemos as análises univariadas, bivariadas e multivariadas. Para as bivariadas, redigimos algumas hipóteses de negócios e verificamos a veracidade delas. 

![alt text](https://github.com/jonasbarletta/ds_em_producao/blob/main/img/mindmap_hypoteses.png)

### 3.4.1 Análise Univariada



#### 3.4.1.1 Variável Resposta



#### 3.4.1.2 Variáveis Numéricas



#### 3.4.1.3 Variáveis Categóricas



### 3.4.2 Análise Bivariada
Analisamos várias hipóteses, aqui apresentaremos apenas os cinco Insights mais interessantes



## 3.5 Modelagem dos Dados

Começamos essa etapa com a preparação dos dados para a implementação dos modelos de Machine Learning. Para os dados númericos e não ciclícos utilizamos algumas estratégias de *rescaling* como *RobustScaler* e *MinMaxScaler*. Já para os dados categóricos fizemos o *encoding* dessas variáveis, entre as estratégias utilizadas estão: *One Hot Encoding*, *Label Encoding* e *Ordinal Encoding*. Para a variável resposta ('sales') fizemos uma transformação logarítimica e para as variáveis de natureza cíclica realizamos transformações trigonométricas.

Após as transformações das variáveis, é necessário selecionar os melhores atributos para o treino dos modelos de ML. Para isso usamos o algoritmo Boruta, que é um métodos baseado Random Forest e funcionamento muito bem com modelos de árvore como Random Forest e XGBoost.

## 3.6 Algoritmos de Machine Learning


## 3.7 Avaliação do Algoritmo

### 3.7.1 Performance de Negócio

### 3.7.2 Performance do Modelo


## 3.8 Deploy do Modelo em Produção


# 4 Conclusão


# 5 Próximos Passos
 


# 6 Referências
[1] LOPES, Meigarom. Curso DS em Produção - Comunidade DS.

[2] Wikpédia. Cramér's V, https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_V, último acesso: 24/07/2022

[3] ROY, Baijayanta, All about Categorical Variable Encoding, https://towardsdatascience.com/all-about-categorical-variable-encoding-305f3361fd02, último acesso: 24/07/2022


