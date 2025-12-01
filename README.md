# 🧠 Resolvendo Algoritmos com GitHub Copilot

Este projeto foi desenvolvido como parte do **Desafio da Digital Innovation One (DIO)**, com o objetivo de explorar como o **GitHub Copilot** pode auxiliar na resolução de problemas computacionais utilizando Python.

A proposta é recriar e/ou aprimorar um projeto utilizando algoritmos clássicos e avançados, aplicando boas práticas de programação, testes automatizados e documentando o raciocínio técnico.  
O resultado é um programa interativo que executa **diversos algoritmos**, desde matemática básica até estruturas de dados e algoritmos de grafos.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **GitHub Copilot** (auxílio na criação dos algoritmos)
- **Pytest** (testes automatizados)
- **Git & GitHub** (versionamento e publicação)

---

## 📊 Algoritmos Implementados

### 🔹 Algoritmos Básicos / Intermediários

| Nº | Algoritmo | Categoria |
|----|-----------|-----------|
| 1  | Fatorial (iterativo) | Matemática |
| 2  | Fibonacci | Sequência |
| 3  | Verificação de número primo | Matemática |
| 4  | Bubble Sort | Ordenação básica |
| 5  | Verificação de palíndromo | Strings |
| 6  | Cálculo de MDC e MMC | Matemática |
| 7  | Busca linear | Busca |
| 8  | QuickSort | Ordenação avançada |
| 9  | Contagem de vogais | Strings |
| 10 | Inversão de string | Strings |
| 11 | Cálculo de potência | Matemática |
| 12 | Número perfeito | Matemática |
| 13 | Busca binária | Busca |
| 14 | Fatorial (recursivo) | Recursão |
| 15 | Decimal → Binário | Conversão |
| 16 | MergeSort | Ordenação avançada |
| 17 | Torre de Hanói | Recursão |
| 18 | Pilha (Stack) | Estrutura de dados (LIFO) |

### 🔹 Algoritmos de Grafos e Otimização

| Nº | Algoritmo | Categoria |
|----|-----------|-----------|
| 19 | BFS (Busca em Largura) | Grafos |
| 19 | DFS (Busca em Profundidade) | Grafos |
| 20 | Dijkstra | Menor caminho em grafo ponderado |
| 21 | Kadane | Maior soma de subarray |

### 🔹 Algoritmos Especialistas (Avançados)

| Nº | Algoritmo | Categoria |
|----|-----------|-----------|
| 22 | KMP (Knuth–Morris–Pratt) | Busca eficiente em strings |
| 23 | Distância de edição (Levenshtein) | Programação Dinâmica |
| 24 | Floyd–Warshall | Todos os menores caminhos (grafos) |
| 25 | Union-Find (Disjoint Set Union) | Estrutura de dados para conjuntos disjuntos |
| 26 | Segment Tree | Estrutura de dados para intervalo (range sum) |

---

## 📂 Estrutura do Projeto

```text
resolvendo-algoritmos-com-github-copilot/
├─ src/
│  ├─ main.py
│  ├─ fatorial.py
│  ├─ fatorial_recursivo.py
│  ├─ fibonacci.py
│  ├─ primos.py
│  ├─ ordenacao.py
│  ├─ quicksort.py
│  ├─ mergesort.py
│  ├─ palindromo.py
│  ├─ contagem_vogais.py
│  ├─ inverter_string.py
│  ├─ potencia.py
│  ├─ numero_perfeito.py
│  ├─ busca_linear.py
│  ├─ busca_binaria.py
│  ├─ mdc_mmc.py
│  ├─ decimal_binario.py
│  ├─ hanoi.py
│  ├─ pilha.py
│  ├─ grafos.py
│  ├─ dijkstra.py
│  ├─ kadane.py
│  ├─ kmp.py
│  ├─ edit_distance.py
│  ├─ floyd_warshall.py
│  ├─ union_find.py
│  └─ segment_tree.py
├─ tests/
│  ├─ test_algoritmos.py
├─ requirements.txt
└─ README.md
```

## ▶️ Como Executar o Projeto
### 1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd resolvendo-algoritmos-com-github-copilot

2️⃣ Crie um ambiente virtual (recomendado)
python -m venv venv


Windows

.\venv\Scripts\activate


Linux/macOS

source venv/bin/activate

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Execute o programa
python src/main.py

### 🧪 Como Executar os Testes

Certifique-se de estar na pasta raiz do projeto e com o ambiente virtual ativado:

pytest


Ou:

python -m pytest


Se tudo estiver correto, algo como:

==================== 100% passed ====================

### 📌 Exemplo de Execução
=== Resolvendo Algoritmos com GitHub Copilot ===
1  - Calcular fatorial (iterativo)
2  - Gerar sequência de Fibonacci
...
26 - Demonstração de Segment Tree (soma em intervalo)
0  - Sair
Escolha uma opção:

### 🤖 Como o GitHub Copilot ajudou

Durante o desenvolvimento deste projeto, o GitHub Copilot foi utilizado para:

Sugerir implementações iniciais de funções a partir de descrições em linguagem natural;

Propor soluções para algoritmos clássicos (fatorial, Fibonacci, ordenação, busca, etc.);

Auxiliar na implementação de algoritmos avançados:

KMP, Levenshtein, Floyd–Warshall, Union-Find, Segment Tree, Dijkstra, Kadane;

Agilizar a escrita de testes automatizados com Pytest;

Ajudar na refatoração e melhoria da legibilidade do código.

Mesmo com o uso da IA, todo o código foi revisado e ajustado manualmente, reforçando o aprendizado dos algoritmos.

### 🔮 Melhorias Futuras

Algumas ideias para evolução do projeto:

Adicionar algoritmos de grafos adicionais (Kruskal, Prim, Bellman–Ford);

Implementar árvore binária de busca completa com remoção;

Criar uma interface gráfica ou web para visualizar a execução dos algoritmos;

Adicionar análise de complexidade (tempo e espaço) no README de cada algoritmo;

Transformar este projeto em um pacote Python e publicar no PyPI.

 ## 👨‍💻 Autor: Jhonathan Lucas

Projeto desenvolvido para o Desafio DIO – Resolvendo Algoritmos com GitHub Copilot.

Se este projeto foi útil, deixe uma ⭐ no repositório!

### 📄 Licença

Este projeto está sob a licença MIT – você pode usar, estudar, modificar e compartilhar livremente.