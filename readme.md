# 🌍 GlobalSIM - Serviço Internacional de Internet por eSIM

Projeto prático desenvolvido para a disciplina de Estruturas de Dados II do curso de Bacharelado em Sistemas de Informação da UNEB - DCET/I

O GlobalSIM é uma aplicação Web em Python/Flask para administrar países atendidos, clientes e eSIMs de uma rede internacional simulada, com o objetivo de aplicar na prática as estruturas de dados estudadas na disciplina

**Professora:** Maria Inés Restovic
**Equipe:**
- Victor César do Rosário Calheiros
- Rafael Fernandes Da Mata

---

## 🚀 Como Executar o Projeto

1. Clone o repositório para a sua máquina:
   ```bash
   git clone [https://github.com/rafaeldamata/Global-ESIM_ED2.git](https://github.com/rafaeldamata/Global-ESIM_ED2.git)
   cd Global-ESIM_ED2
   ```

2. Crie e ative um ambiente virtual (comandos para Windows / Git Bash):
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install Flask
   ```

4. Execute o servidor da aplicação:
   ```bash
   python app.py
   ```

5. Acesse o sistema pelo navegador na URL:
   `http://127.0.0.1:5000`

---

## 🧠 Estruturas de Dados Implementadas (Etapa 1)

Nesta primeira etapa, o foco foi a implementação do gerenciamento de Países Atendidos utilizando uma **Tabela Hash** construída do zero, garantindo a separação total entre a lógica da estrutura de dados e as rotas Web do Flask.

- **Mecanismo da Tabela Hash:** Foi criada a classe `TabelaHash`, onde a chave de espalhamento (hash) é a Abreviação do país (código de duas letras)[cite: 3]. O cálculo de posição foi projetado de forma determinística, somando os valores ASCII dos caracteres para garantir a estabilidade do índice de memória durante as execuções. O tratamento de colisões é feito por meio de encadeamento direto (listas internas).
- **Persistência de Dados:** Os dados são persistidos em um arquivo `paises.json`[cite: 3]. Durante a inicialização do Flask, o arquivo é lido e os registros são carregados em memória para a Tabela Hash. Todas as operações de busca, alteração e remoção manipulam exclusivamente a estrutura de dados em memória, refletindo o estado atualizado no arquivo JSON posteriormente, sem utilizar bibliotecas prontas como mecanismo principal de busca[cite: 3, 10].

---

## ⭐ Diferencial da Equipe

**Proposta Escolhida:** Identificação de países estratégicos da rede por métricas de conectividade[cite: 2].

**Descrição do Problema e Integração:**
Na Etapa 3 do projeto, a rede da GlobalSIM será modelada como um Grafo Ponderado, onde os vértices são os países e as arestas são as conexões com simulação de latência[cite: 6]. Em redes de telecomunicações reais, identificar quais nós (países) são essenciais para manter a resiliência da internet é um desafio crítico.

Para resolver este problema, implementaremos um algoritmo focado em **Métricas de Centralidade** (como a *Centralidade de Grau* ou *Centralidade de Intermediação/Betweenness*). O sistema terá um painel analítico que percorrerá o Grafo para classificar os países atendidos pela GlobalSIM. A funcionalidade informará ao usuário quais países atuam como os maiores "Hubs" da rede (países estratégicos por onde passa o maior volume de rotas mais curtas). 

**Decisões Algorítmicas:** 
A identificação não será visual ou manual, mas totalmente algorítmica. O diferencial iterará sobre os caminhos calculados pelo algoritmo de Dijkstra e tabulará a frequência com que cada vértice (país) é utilizado para conectar os demais pontos da infraestrutura, justificando de forma quantitativa a sua importância estratégica na rede.
