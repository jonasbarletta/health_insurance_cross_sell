# Projeto Insurance All

<p align="center">
  <img src="https://user-images.githubusercontent.com/102927918/190490261-bbe4cc24-bb72-40f4-be6a-07ef1f7bc87c.png" />
</p>

O Projeto Insurance All é um projeto de Ciências de Dados para a classificação e ranqueamento de possível clientes em uma nova modalidade de seguro da empresa (fictícia) Insurance All.

Esse projeto é uma proposta de Projeto do Aluno (PA), da Comunidade DS, baseado no desafio 'Health Insurance Cross Sell Prediction ' da plataforma Kaggle. O enunciado ofical do problema está disponível em [Kaggle](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction).

# 1 Questão de Negócio

O Contexto a seguir, é completamente fictício, a empresa, o contexto, o CEO, as perguntas de negócio existem somente na minha imaginação. 

A Insurance All é uma empresa que fornece seguro de saúde para seus clientes e o time de produtos está analisando a possibilidade de oferecer aos assegurados, um novo produto: um seguro de automóveis.

Assim como o seguro de saúde, os clientes desse novo plano de seguro precisam pagar um valor anualmente à Insurance All para obter um valor assegurado pela empresa, destinado aos custos de um eventual acidente ou dano ao veículo.

Com a solução, o time de vendas espera conseguir priorizar as pessoas com maior interesse no novo produto e assim, otimizar a campanha realizando apenas contatos aos clientes mais propensos a realizar a compra.

Ao final do projeto algumas análises e perguntas deverão ser respondidas e entregues em um relatório:

- Principais Insights sobre os atributos mais relevantes de clientes interessados em adquirir um seguro de automóvel.
- Qual a porcentagem de clientes interessados em adquirir um seguro de automóvel, o time de vendas conseguirá contatar fazendo 20.000 ligações?
- E se a capacidade do time de vendas aumentar para 40.000 ligações, qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar?
- Quantas ligações o time de vendas precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro de automóvel?

# 2 Planejamento da Solução

Para solução do desafio dividimos em algumas etapas cíclicas (como mostra a imagem abaixo) de forma que apresentaremos aqui alguns cíclos completos dessas etapas. Começando na 'Questão de Negócio' até a 'Avaliação do Algoritmo' onde analisaremos a performance do modelo e decidiremos se é necessário realizar mais um ciclo antes de colocar o 'Modelo em Produção'.

![alt text](https://github.com/jonasbarletta/ds_em_producao/blob/main/img/Questao%20de%20Negocio%20(1).png)

### 2.1 Produto Final
- Insights de negócio realizados a partir da Análise Exploratória de Dados.
- As respostas das perguntas.
- Uma lista dos clientes ordenados de acordo com o interesse dos clientes, em que os mais interessados aparecem primeiro.

## 2.2 Ferramentas Utilizadas
- Python 3.10
- Jupyter Notebook
- Github
- SQLite

Vamos entender um pouco melhor como foi cada etapa do projeto.

# 3 Etapas do Primeiro Ciclo do Projeto

## 3.1 Entendimento do Negócio

A Insurance All fez uma pesquisa com cerca de 380 mil clientes sobre o interesse em aderir o de seguro de automóveis, no ano passado. Todos os clientes demonstraram interesse ou não em adquirir o seguro de automóvel e essas respostas ficaram salvas em um banco de dados junto com outros atributos dos clientes.

O time de produtos selecionou 127 mil novos clientes que não responderam a pesquisa para participar de uma campanha, no qual receberão a oferta do novo produto de seguro de automóveis. A oferta será feita pelo time de vendas através de ligações telefônicas.

Contudo, o time de vendas tem uma capacidade de realizar 20 mil ligações dentro do período da campanha.

Nesse contexto, o projeto consiste em construir um modelo que prediz se o cliente estaria ou não interessado no seguro de automóvel. Porem além de classificá-los será necessário ranquear os clientes com relação a probabilidade de contratar o seguro de automóvel.

## 3.2 Coleta de Dados

Por se tratar de um desafio da plataforma Kaggle, os dados já estão coletados bastando assim acessá-los. Tais dados podem ser acessados pelo [link](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction). Nessa página estão disponíveis dois arquivos relevantes para o problema:

 - train.csv (dados para treino, com dados de 380 mil clientes que responderam a pesquisa)
 - test.csv (dados de teste, com os dados 127 mill clientes que não responderam)

Os dados também podiam ser acessado por um banco da dados AWS, então apenas com a finalidade de praticar as consultas com SQL, inicialmente coletamos os dados via banco de dados. 

Os atributos apresentados nos conjunto de dados são:

| Atributo                          | Descrição |  
| --------------------------------  | --------- |
| id                                | identificador único do cliente |   
| Gender                            | gênero do cliente |
| Age                               | idade do cliente |
| Driving License                   | 0, o cliente não tem permissão para dirigir e 1, o cliente tem permissão para dirigir  |
| Region Code                       | código da região do cliente |
| Customers                         | Número de clientes de um dia |
| Previously Insured                | 0, o cliente não tem seguro de automóvel e 1, o cliente já tem seguro de automóvel |
| Vehicle Age                       | idade do veículo |
| Vehicle Damage                    | 0, cliente nunca teve seu veículo danificado no passado e 1, cliente já teve seu veículo danificado no passado |
| Anual Premium                     | quantidade que o cliente pagou à empresa pelo seguro de saúde anual |
| Policy sales channel              | código anônimo para o canal de contato com o cliente |
| Vintage                           | número de dias que o cliente se associou à empresa através da compra do seguro de saúde |
| Response                          | 0, o cliente não tem interesse e 1, o cliente tem interesse |

Agora que os dados estão coletados partiremos para a limpeza.

## 3.3 Análise Descritiva

Analisar os dados de uma forma global é importante para se entender que tipo de dados serão estudados e modelados. Nessa etapa, buscamos entender a quantidade de linhas e colunas do conjunto de dados, se há ou não valores faltantes, as tipos das variáveis, se a variáveis numéricas formam ou não uma distribuição normal  e como estão distribuidas a variáveis categóricas. Nessa etapa não é esperado encontrar grandes resultados ou insights, mas é essencial para o entendimento dos dados.

## 3.4 Limpeza dos Dados

Para esse problema não foi necessário limpar os dados. Não havia dados faltantes (Nan) nem informações mal inseridas. A única mudança que fizemos nessa etapa foi o nome dos atributos que começavam com letras maiúsculas e colocamos com letras minúsculas.

## 3.5 Análise Exploratória dos Dados

Aqui começamos fazendo o Mapa Mental de Hipóteses abaixo. Fizemos as análises univariadas, bivariadas e multivariadas. Para as bivariadas, redigimos algumas hipóteses de negócios e verificamos a veracidade delas. 

![Seguro_de_Vida](https://user-images.githubusercontent.com/102927918/190493798-88473d12-9055-4f45-a3c9-10892a20b0f4.png)

### 3.5.1 Análise Univariada



#### 3.5.1.1 Variável Resposta

![image](https://user-images.githubusercontent.com/102927918/190503474-f2803f8f-5308-4a8a-b8bd-69d988549435.png)

A quantidade de cliente que não querem aderir ao novo seguro é muito maior do que as que gostariam de aderir.

#### 3.5.1.2 Variáveis Numéricas

![image](https://user-images.githubusercontent.com/102927918/190503730-8ecea895-24f4-4158-999e-a08c308e7015.png)

- Pessoas mais novas são a maioria dentro da pesquisa.
- A maior parte possui habilitação para dirigir.
- A quantidade de clientes que já possuem seguro de automóvel é quase igual a dos que não possuem.
- A maior parte dos cliente possuem carros novos (menos de 2 anos).
- A quantidade de clientes que já sofreram acidentes de carros é praticamente igual a dos que nunca sofreram.
- A variável Anual Premium possui outliers muito distante da mediana.
- A variável Vintage é bastante balanceada.
- Não possuímos grandes informações variáveis Region Code e Policy Sales Channel, mas dentro de uma análise inicial as regiões dos clientes são ligeiramente balanceadas (com exceção de algumas regiões). Mas os canais de comunicação são bastante desbalanceados.

#### 3.5.1.3 Variáveis Categóricas



### 3.5.2 Análise Bivariada
Analisamos várias hipóteses, aqui apresentaremos apenas os XXXX Insights mais interessantes



## 3.6 Modelagem dos Dados

Começamos essa etapa com a preparação dos dados para a implementação dos modelos de Machine Learning. Para os dados númericos e não ciclícos utilizamos algumas estratégias de *rescaling* como *RobustScaler* e *MinMaxScaler*. Já para os dados categóricos fizemos o *encoding* dessas variáveis, entre as estratégias utilizadas estão: *One Hot Encoding*, *Label Encoding* e *Ordinal Encoding*. Para a variável resposta ('sales') fizemos uma transformação logarítimica e para as variáveis de natureza cíclica realizamos transformações trigonométricas.

Após as transformações das variáveis, é necessário selecionar os melhores atributos para o treino dos modelos de ML. Para isso usamos o algoritmo Boruta, que é um métodos baseado Random Forest e funcionamento muito bem com modelos de árvore como Random Forest e XGBoost.

## 3.7 Algoritmos de Machine Learning


## 3.8 Avaliação do Algoritmo

### 3.8.1 Performance de Negócio

### 3.8.2 Performance do Modelo


## 3.9 Deploy do Modelo em Produção

Entedemos que o modelo gerou grandes resultados, superando muito o modelo aleatório, mas ao final desse ciclo optamos por não colocar o modelo em produção. Fizemos apenas alguns testes locais. Dessa forma faremos mais um ciclo onde serão acrescentadas novas análises, testadas novas features, outros encoders, realizaremos Cross-Validation do modelo e faremos o fine-tunning dos parâmetros do modelo. Ao final do próximo ciclo esperamos colocar o modelo em produção.

# 4 Conclusão


# 5 Próximos Passos
 


# 6 Referências
[1] LOPES, Meigarom. Curso DS em Produção - Comunidade DS.

[2] Wikpédia. Cramér's V, https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_V, último acesso: 24/07/2022

[3] ROY, Baijayanta, All about Categorical Variable Encoding, https://towardsdatascience.com/all-about-categorical-variable-encoding-305f3361fd02, último acesso: 24/07/2022


