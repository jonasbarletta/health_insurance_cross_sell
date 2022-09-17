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

![image](https://user-images.githubusercontent.com/102927918/190503730-8ecea895-24f4-4158-999e-a08c308e7015.png)

- A quantidade de cliente que não querem aderir ao novo seguro é muito maior do que as que gostariam de aderir.
- Pessoas mais novas são a maioria dentro da pesquisa.
- A maior parte possui habilitação para dirigir.
- A quantidade de clientes que já possuem seguro de automóvel é quase igual a dos que não possuem.
- A maior parte dos cliente possuem carros novos (menos de 2 anos).
- A quantidade de clientes que já sofreram acidentes de carros é praticamente igual a dos que nunca sofreram.
- A variável Anual Premium possui outliers muito distante da mediana.
- A variável Vintage é bastante balanceada.
- Não possuímos grandes informações variáveis Region Code e Policy Sales Channel, mas dentro de uma análise inicial as regiões dos clientes são ligeiramente balanceadas (com exceção de algumas regiões). Mas os canais de comunicação são bastante desbalanceados.


### 3.5.2 Análise Bivariada
Analisamos várias hipóteses, aqui apresentaremos apenas os 6 Insights mais interessantes.

- H1: Clientes mais velhos tem mais interesse em obter seguro de automóvel.

![image](https://user-images.githubusercontent.com/102927918/190512101-6ac1e212-69de-4a08-be1b-db76bcecd4cf.png)

Falso. Clientes na meia idade (entre 30 e 50 anos) possuem mais interesse em obter seguro de automóvel.

- H2: Clientes mulheres tem mais interesse em obter seguro de automóvel.

![image](https://user-images.githubusercontent.com/102927918/190512198-3814d3ea-22f2-4b37-8a81-52df64999f28.png)

Falso. Clientes mulheres tem menos interesse em obter seguro de automóvel.

- H5: Clientes mais antigos possuem mais interesse em obter seguro de automóvel.

![image](https://user-images.githubusercontent.com/102927918/190512303-c34b1e74-7f51-4dcd-94aa-5f306667f14c.png)

Falso Não há diferença significativa com relação ao tempo que o cliente possui o seguro de vida

- H6: Clientes com veículos mais antigos tem menos interesse em obter seguro de automóvel.

![image](https://user-images.githubusercontent.com/102927918/190512407-8624f51b-ce5c-4fd5-98e7-e5034055a0e2.png)

Falso Clientes com veículos mais antigos tem mais interesse em obter seguro de automóve

- H7: Clientes com veículos que já foram danificados tem mais interesse em obter seguro de automóvel.

![image](https://user-images.githubusercontent.com/102927918/190512533-95a57d0f-9a13-4891-90ee-8baf012122bf.png)

Verdade Clientes com veículos que já foram danificados tem MUITO mais interesse em obter seguro de automóvel

- H8: Clientes que já possuem seguro de automóvel em outra seguradora possuem menos interesse em obter seguro de automóvel.

![image](https://user-images.githubusercontent.com/102927918/190512571-ea616fb5-80f7-4a49-9b4d-af9c36a91d52.png)

Verdade Clientes que já possuem seguro de automóvel em outra seguradora possuem EXTREMAMENTE MENOS interesse em obter um novo seguro.

## 3.6 Preparação dos Dados

Para a preparação dos dados tilizamos duas estratégias de "rescaling" e algumas de "encoding", alguns atributos já tinham sofrido alterações na etapa de Features Engineering tais como:

- Gender: M e F foram substituídos por 1 e 0, respectivamente;
- Vehicle Age: '< 1 Year', '1-2 Year' e '> 2 Year' foram substituídos por, 0.5, 1.5 e 2.5, respectivamente;
- Vehicle Damage: Yes e No foram susbtituídos por 1 e 0, respectivamente.

As demais variáveis foram feitos os seguintes procedimentos:
- Annual Premium: possui distribuição próxima da normal, então optamos por uma padronização (Standard Scaler)
- Age e Vintage: não possuem distribuição próxima da normal, então optamos pelo normalização min-max (MinMaxScaler)
- Region Code: optamos pelo 'Target Encoding'
- Policy Sales Channel: optamos pelo 'Frequency Encoding'

## 3.7 Seleção dos Atributos

A seleção dos atributos que farão parte do modelo de Machine Learning foi feita a partir da feature_importance da ExtraTreeClassifier

Feature ranking:
|feature|  importance|
|-------|------------|
|vintage|0.280894|               
|annual_premium    |0.248784|        
|age     |0.153679|                  
|region_code    |0.106334|           
|vehicle_damage     |0.079504|
|policy_sales_channel     |0.060078|  
|previously_insured     |0.047978|    
|vehicle_age     |0.016770|           
|gender     |0.005482|                
|driving_license     |0.000498|  

![image](https://user-images.githubusercontent.com/102927918/190712511-fc96877d-051b-4ed3-a382-e4d35bbb98a0.png)

Dessa forma optamos pelos 7 melhores atributos: 'vintage', 'annual_premium', 'age', 'region_code', 'vehicle_damage', 'policy_sales_channel', 'previously_insured'.

## 3.8 Algoritmos de Machine Learning

Agora com as variáveis ajustadas e selecionadas, estamos prontos para aplicar os algoritmos de Machine Learning. Mas antes de analisarmos os modelos, é importante lembrar que problema não se trata de classificar os clientes com 1 ou 0 (irá contratar ou não irá contratar o seguro), mas sim ranqueá-los com relação a probabilidade de contratar o serviço (Learning to Rank). Nesse projeto testamos cinco modelos:

- KNN (K-Nearest Neighbors)
- Regressão Logística 
- Extra Tree 
- Random Forest 
- Light Gradiente Boost Machine (LGBM). 

Para cada modelo, fizemos dois gráficos: A Curva de Ganho Acumulativo e A Curva Lift.
A primeira é um gráfico de 'porcentagem da amostra' x 'porcentagem de interessados (ganho)', ou seja, quanto mais "rápido" essa curva chegar no topo (y = 1) melhor ela é.
A segunda é um gráfico de 'porcentagem da amostra' x 'lift' , que mostra quantas vezes o modelo é superior com relação ao modelo aleatório para cada porcentagem da amostra.

### 3.8.1 KNN (K-Nearest Neighbors)

![image](https://user-images.githubusercontent.com/102927918/190857010-5c304b7a-d977-4097-8b78-af8e99b98d9a.png)
![image](https://user-images.githubusercontent.com/102927918/190857025-ff9bd7e6-e045-4b64-95c3-de2bcaeba692.png)

### 3.8.2 Regressão Logística

![image](https://user-images.githubusercontent.com/102927918/190857085-2cb89395-51ea-4df5-adc2-a66122cd1c99.png)
![image](https://user-images.githubusercontent.com/102927918/190857089-2006b5ed-9ca6-4481-a8fe-15e6ab52bc38.png)

### 3.8.3 Extra Tree 

![image](https://user-images.githubusercontent.com/102927918/190857289-dbc51753-f9a5-45c3-b3aa-0739ffddd602.png)
![image](https://user-images.githubusercontent.com/102927918/190857298-842d6b48-846d-4650-b4f7-cbb10e4cc891.png)

### 3.8.4 Random Forest

![image](https://user-images.githubusercontent.com/102927918/190857315-165cee2d-bd5f-43ba-8942-52919322b23d.png)
![image](https://user-images.githubusercontent.com/102927918/190857503-d0dc67b6-67a1-4063-86a2-43038a51cb92.png)

### 3.8.5 Light Gradiente Boost Machine (LGBM)

![image](https://user-images.githubusercontent.com/102927918/190857519-6a3b30b2-60fc-4de2-9fdb-373ff4c19c6d.png)
![image](https://user-images.githubusercontent.com/102927918/190857524-39edfcc1-7dfc-44ad-8325-d4f48a323fb8.png)



## 3.9 Avaliação do Algoritmo

### 3.9.1 Performance de Negócio



### 3.9.2 Performance do Modelo


## 3.10 Deploy do Modelo em Produção

Entedemos que o modelo gerou grandes resultados, superando muito o modelo aleatório, mas ao final desse ciclo optamos por não colocar o modelo em produção. Fizemos apenas alguns testes locais. Dessa forma faremos mais um ciclo onde serão acrescentadas novas análises, testadas novas features, outros encoders, realizaremos Cross-Validation do modelo e faremos o fine-tunning dos parâmetros do modelo. Ao final do próximo ciclo esperamos colocar o modelo em produção.

# 4 Conclusão


# 5 Próximos Passos
 


# 6 Referências
Gráficos:
[1] https://www.python-graph-gallery.com/

[2] https://www.python-graph-gallery.com/stacked-and-percent-stacked-barplot

Sobre as métricas de Ranking
[3] https://queirozf.com/entries/evaluation-metrics-for-ranking-problems-introduction-and-examples

[4] https://stats.stackexchange.com/questions/159657/metrics-for-evaluating-ranking-algorithms

[5] https://archive.siam.org/meetings/sdm10/tutorial1.pdf

[6] https://brianmcfee.net/papers/mlr.pdf

Curvas Ranking e Lift
[7] https://towardsdatascience.com/meaningful-metrics-cumulative-gains-and-lyft-charts-7aac02fc5c14

Exemplos de Problemas de Métrica

[8] https://towardsdatascience.com/20-popular-machine-learning-metrics-part-2-ranking-statistical-metrics-22c3e5a937b6

[9] Bias and Variance Book Machine Learning: An Algorithmic Perspective, by Stephen Marsland - Capítulo 02 YouTube: StatQuest

[10] Random Forest Model Book Machine Learning: An Algorithmic Perspective, by Stephen Marsland - Capítulo 13

[11] https://stats.stackexchange.com/questions/262794/why-does-a-decision-tree-have-low-bias-high-variance

[12] Paper Original da Random Forest https://link.springer.com/article/10.1023/A:1010933404324

