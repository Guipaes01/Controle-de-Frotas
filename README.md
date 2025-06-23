# 📊 Sistema de Controle de Vendas e Financeiro com Power BI e PostgreSQL

Este projeto tem como objetivo centralizar, analisar e visualizar informações operacionais e financeiras relacionadas à gestão de frotas de veículos, como manutenções, abastecimentos, custos fixos e alertas preventivos, com dados gerados automaticamente via Python e visualizações em Power BI.

---

## 📌 Visão Geral do Projeto

O sistema simula um ambiente de gestão de vendas realista, permitindo **análises estratégicas** por meio de **dashboards dinâmicos**.

### 🧰 Tecnologias Utilizadas:

* 🐘 **PostgreSQL** — Banco de dados relacional
* 🐍 **Python (Faker + psycopg2)** — Geração automatizada de dados fictícios
* 📊 **Power BI Desktop** — Análise e visualização de KPIs
* 🖥️ **Power Query + DAX** — Para tratamento de dados e criação de medidas
* 🕒 **Agendador de Tarefas do Windows** — Para rodar o script de forma automatizada

---

## 📂 Estrutura do Projeto

### 🔧 Backend (Python + PostgreSQL)

Geração de dados para as seguintes tabelas:

* `clientes` → Cadastro de clientes
* `mesas` → Controle de mesas (status: livre, ocupada, reservada)
* `produtos` → Catálogo de produtos com categorias e preços
* `pedidos` → Histórico de pedidos por cliente e mesa
* `itens_pedido` → Detalhamento dos itens vendidos por pedido
* `pagamentos` → Formas de pagamento por pedido
* `reservas` → Controle de reservas de mesas

> Script responsável pela injeção dos dados:
> [`injetar_dados.py`](./injetar_dados.py)

---

## 🖥️ Frontend (Power BI)

### Telas Desenvolvidas:

#### 1. **Visão Geral**

* Total de Vendas
* Total de Pedidos
* Produtos Ativos
* Total de Clientes
* Evolução de Vendas por Mês
* Produtos Mais Vendidos
* Pedidos Recentes (com status e data)


---

#### 2. **Financeiro**

* Total Recebido
* Total Faturado
* Total em Aberto
* % de Inadimplência
* Custo Total
* Lucro Bruto
* Lucro Líquido
* Distribuição de Receitas por Forma de Pagamento
* Evolução Financeira Mensal


---

#### 3. **Estoque / Manutenção**

* Total de Manutenções
* Custo Total de Manutenções
* Quantidade Total de Peças Utilizadas
* Valor Total em Peças
* Tipo de Manutenção (Corretiva x Preventiva)
* Peças Mais Utilizadas
* Alertas (ex.: Troca de Óleo, Revisões, Seguro)
* Veículos por Ano, Modelo e Quilometragem Atual


---

## 🧑‍💻 Autor

**Guilherme Paes**
🔗 [LinkedIn](https://www.linkedin.com/in/paesgui/)

