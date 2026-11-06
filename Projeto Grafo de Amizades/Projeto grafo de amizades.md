# Caderno do Estudante
# Projeto ConectaUDF: redes sociais com grafos
**Disciplina:** Algoritmos / Matemática Discreta / Ciência de Dados

## 1. O desafio
Você faz parte da equipe que analisa a rede social fictícia **ConectaUDF**. Sua missão é representar as amizades em um grafo, realizar cálculos e usar Python para interpretar a estrutura da rede.

## 2. Conceitos essenciais
- **Vértice (ou nó):** representa um usuário.
- **Aresta:** representa uma amizade entre dois usuários.
- **Grau:** quantidade de conexões diretas de um usuário.
- **Caminho:** sequência de usuários em que cada par consecutivo está conectado.
- **Densidade:** proporção entre as amizades existentes e todas as amizades possíveis.

Neste projeto, a amizade é recíproca. Portanto, usamos um **grafo não direcionado**.

## 3. Conheça os usuários
| Código | Usuário |
|---|---|
| A | Ana |
| B | Bruno |
| C | Carla |
| D | Diego |
| E | Elisa |
| F | Felipe |

As amizades são:
1. Ana — Bruno
2. Ana — Carla
3. Bruno — Carla
4. Bruno — Diego
5. Carla — Elisa
6. Diego — Elisa
7. Diego — Felipe
8. Elisa — Felipe

## 4. Passo a passo: desenhe o grafo
1. Desenhe seis círculos, um para cada usuário.
2. Escreva o nome de cada pessoa dentro do círculo.
3. Para cada amizade da lista, desenhe uma linha entre os dois usuários.
4. Não desenhe duas linhas para a mesma amizade.
5. Confira se todas as oito amizades aparecem.

<img width="1288" height="968" alt="Image" src="https://github.com/user-attachments/assets/adf07b35-b06c-48e1-9606-87537cd5a883" />

## 5. Passo a passo: calcule o grau
Conte quantas linhas chegam a cada círculo. Registre o resultado.

| Usuário | Amigos diretos | Grau |
|---|---|---:|
| Ana | Bruno, Carla | 2 |
| Bruno | Ana, Carla, Diego | 3 |
| Carla | Ana, bruno, Elisa | 3 |
| Diego | Bruno, Elisa, Felipe | 3 |
| Elisa | Carla, Diego, Felipe | 3 |
| Felipe | Diego, Elisa | 2 |

**Pergunta 1:** quem tem mais conexões diretas?  
Resposta: Bruno, Carla, Diego e Elisa tem mais conexões diretas, sendo 3 conexões cada um.

## 6. Passo a passo: calcule o número de amizades
Some todos os graus. Como cada amizade conecta dois usuários, cada aresta é contada duas vezes.

**Fórmula:**  
`Número de arestas = soma dos graus ÷ 2`

1. Soma dos graus: 16
2. Divida por 2: 16 ÷ 2 = 8
3. Quantas amizades existem no grafo? 8

## 7. Passo a passo: calcule a densidade
A densidade compara as amizades existentes com o total de amizades possíveis.

Para um grafo simples não direcionado:

`D = 2 × E / (V × (V − 1))`

Em que:
- `D` = densidade;
- `E` = número de arestas;
- `V` = número de vértices.

Substitua os valores:
`D = 2 × 8 / (6 × (6 − 1))`

Resultado decimal: 0,53333  
Resultado percentual: 53,33%

**Interprete:** a rede tem poucas ou muitas das conexões possíveis? Explique com suas palavras.

A rede possui aproximadamente a metade das conexões possíveis, considerando que o cálculo resultou em 53,33%, então ela possui uma quantidade moderada de conexões, não tendo sido feitas muitas, mas também não tendo sido feitas poucas das possíveis. Então, acredito que tenha uma quantidade moderada.

## 8. Passo a passo: represente o grafo em Python
A lista de adjacência registra, para cada usuário, os nomes de seus amigos. Digite o código em Python (por exemplo, no Google Colab ou em outro ambiente disponível).

```python
rede = {
    "Ana": ["Bruno", "Carla"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe"],
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa"]
}

# Quantidade de usuarios
n = len(rede)

# Calcule o grau de cada usuario
for usuario, amigos in rede.items():
    print(usuario, "tem", len(amigos), "conexoes")

# A soma dos graus conta cada amizade duas vezes
soma_graus = sum(len(amigos) for amigos in rede.values())
arestas = soma_graus // 2

print("Total de usuarios:", n)
print("Total de amizades:", arestas)

# Densidade do grafo
densidade = (2 * arestas) / (n * (n - 1))
print(f"Densidade: {densidade:.2%}")
```

### Entenda o código
1. `rede` guarda os usuários e suas listas de amigos.
2. `len(rede)` conta os usuários.
3. `len(amigos)` calcula o grau de cada usuário.
4. `sum(...)` soma os graus.
5. `// 2` divide a soma por dois para contar cada amizade uma única vez.
6. A fórmula final calcula a densidade.

## 9. Passo a passo: encontre um caminho
Encontre um caminho de Ana até Felipe. Cada passagem por uma linha corresponde a uma aresta.

Exemplo de registro:
`Ana → Bruno → Diego → Felipe`

- Quantas arestas há no caminho? 3 arestas
- Você encontrou outro caminho com a mesma quantidade de arestas? Qual?

Sim. `Ana → Carla → Elisa → Felipe`

## 10. Desafio em grupo
Amplie a rede social:
1. Adicione pelo menos quatro usuários fictícios.
2. Crie no mínimo cinco novas amizades.
3. Atualize a lista de adjacência no Python.
4. Recalcule os graus, o total de arestas e a densidade.
5. Compare a densidade antes e depois da ampliação.
6. Identifique os usuários com mais conexões.
7. Explique como a rede poderia recomendar uma nova amizade.

## 11. Entrega
Entregue:
- desenho do grafo;

<img width="2248" height="1928" alt="Image" src="https://github.com/user-attachments/assets/e0804ae3-6db1-4c76-93d1-eee78372c73a" />

- tabela com os graus;

| Usuário | Amigos diretos | Grau |
|---|---|---:|
| Ana | Bruno, Carla, Gabriel, Isabella | 4 |
| Bruno | Ana, Carla, Diego, Isabella | 4 |
| Carla | Ana, bruno, Elisa, Gabriel, Heloisa | 5 |
| Diego | Bruno, Elisa, Felipe, Isabella, João | 5 |
| Elisa | Carla, Diego, Felipe, Heloisa | 4 |
| Felipe | Diego, Elisa, Heloisa, João | 4 |
| Gabriel | Ana, Carla | 2 |
| Heloisa | Carla, Elisa, Felipe | 3 |
| Isabella | Ana, Bruno, Diego | 3 |
| João | Diego, Felipe | 2 |

**Pergunta 1:** quem tem mais conexões diretas?
No grafo novo, agora são Carla e Diego, com 5 conexões cada um.

- cálculos de arestas e densidade;

**Fórmula:**  
`Número de arestas = soma dos graus ÷ 2`

1. Soma dos graus: 36
2. Divida por 2: 36 ÷ 2 = 18
3. Quantas amizades existem no grafo? 18

`D = 2 × E / (V × (V − 1))`

Em que:
- `D` = densidade;
- `E` = número de arestas;
- `V` = número de vértices.

Substitua os valores:
`D = 2 × 18 / (10 × (10 − 1))`

Resultado decimal: 0,4  
Resultado percentual: 40%

**Interprete:** a rede tem poucas ou muitas das conexões possíveis? Explique com suas palavras.
A rede tem uma quantidade aproximadamente pequena das conexões possíveis. Considerando que o cálculo da densidade do grafo de amizades atualizado resultou em 40% das conexões possíveis, está abaixo da metade das conexões possíveis. Então, em minha interpretação, tem uma quantidade pequena, por estar abaixo da metade.

- código Python executável;
```Python
rede = {
    "Ana": ["Bruno", "Carla", "Gabriel", "Isabella"],
    "Bruno": ["Ana", "Carla", "Diego", "Isabella"],
    "Carla": ["Ana", "Bruno", "Elisa", "Gabriel", "Heloisa"],
    "Diego": ["Bruno", "Elisa", "Felipe", "Isabella", "João"],
    "Elisa": ["Carla", "Diego", "Felipe", "Heloisa"],
    "Felipe": ["Diego", "Elisa", "Heloisa", "João"],
    "Gabriel": ["Ana", "Carla"],
    "Heloisa": ["Carla", "Elisa", "Felipe"],
    "Isabella": ["Ana", "Bruno", "Diego"],
    "João": ["Diego", "Felipe"]

}

# Quantidade de usuarios
n = len(rede)

# Calcule o grau de cada usuario
for usuario, amigos in rede.items():
    print(usuario, "tem", len(amigos), "conexoes")

# A soma dos graus conta cada amizade duas vezes
soma_graus = sum(len(amigos) for amigos in rede.values())
arestas = soma_graus // 2

print("Total de usuarios:", n)
print("Total de amizades:", arestas)

# Densidade do grafo
densidade = (2 * arestas) / (n * (n - 1))
print(f"Densidade: {densidade:.2%}")

```

- respostas às perguntas e breve conclusão.

Explique como a rede poderia recomendar uma nova amizade.

Resposta: A rede pode recomendar as pessoas que já são amigos dos seus amigos, mas que você não possui nenhuma relação com eles ainda. Então, ela te recomendaria uma amizade nova baseada nas amizades que você já tem e que estariam em comum com vocês.

## 12. Pergunta de reflexão
Duas pessoas ainda não são amigas, mas têm três amigos em comum. Como essa informação poderia ser usada para sugerir uma nova conexão? Quais cuidados de privacidade devem ser considerados ao analisar redes sociais?

Resposta: A rede social pode sugerir que as duas pessoas tentem se conhecer, devido a já terem 3 amigos em comum, tem mais chance deles terem compatibilidade parecida um com o outro. 
E, ao analisar as redes sociais, deve-se ter cuidado com a privacidade das pessoas pois muitas postam coisas que não querem que se tornem públicas, tal qual pessoas que deixam os perfis privados ou tem contas secundárias. Então deve-se tomar cuidado com a maneira tal qual esse conteúdo vai ser usado, mesmo que para sugerir uma nova amizade para outra pessoa com amigos em comum.
