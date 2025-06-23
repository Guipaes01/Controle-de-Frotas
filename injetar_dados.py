import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('pt_BR')

# Conexão com o banco PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="Frota",
    user="USUARIO",
    password="SENHA" 
)
cursor = conn.cursor()

# ---------- VEÍCULOS ----------
veiculos = []
for i in range(10):
    placa = f"{fake.random_uppercase_letter()}{fake.random_uppercase_letter()}-{random.randint(1000,9999)}"
    modelo = random.choice(["Strada", "Hilux", "Fiorino", "HR", "Master"])
    marca = random.choice(["Fiat", "Toyota", "Renault", "Hyundai"])
    ano = random.randint(2015, 2023)
    tipo = random.choice(["Carga", "Passeio"])
    km = random.randint(20000, 150000)
    ativo = random.choice([True, True, False])
    cursor.execute("""
        INSERT INTO veiculos (placa, modelo, marca, ano, tipo, km_atual, ativo)
        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id
    """, (placa, modelo, marca, ano, tipo, km, ativo))
    veiculos.append(cursor.fetchone()[0])

# ---------- MOTORISTAS ----------
motoristas = []
for i in range(10):
    nome = fake.name()
    contato = fake.phone_number()
    status = random.choice(["ativo", "inativo"])
    cursor.execute("""
        INSERT INTO motoristas (nome, contato, status)
        VALUES (%s, %s, %s) RETURNING id
    """, (nome, contato, status))
    motoristas.append(cursor.fetchone()[0])

# ---------- MANUTENÇÕES + PEÇAS ----------
manutencoes = []
pecas_usadas = []
for i in range(30):
    veiculo_id = random.choice(veiculos)
    tipo = random.choice(["preventiva", "corretiva"])
    data = fake.date_between(start_date='-90d', end_date='today')
    custo_total = round(random.uniform(150, 1500), 2)
    observacao = fake.sentence()
    cursor.execute("""
        INSERT INTO manutencoes (id_veiculo, tipo, data, custo_total, observacao)
        VALUES (%s, %s, %s, %s, %s) RETURNING id
    """, (veiculo_id, tipo, data, custo_total, observacao))
    manut_id = cursor.fetchone()[0]
    manutencoes.append(manut_id)

    for _ in range(random.randint(1, 3)):
        nome_peca = random.choice(["Óleo", "Filtro", "Correia", "Pneu", "Bateria"])
        preco = round(random.uniform(50, 600), 2)
        quantidade = random.randint(1, 4)
        cursor.execute("""
            INSERT INTO pecas_usadas (id_manutencao, nome_peca, preco_unitario, quantidade)
            VALUES (%s, %s, %s, %s)
        """, (manut_id, nome_peca, preco, quantidade))

# ---------- ABASTECIMENTOS ----------
for _ in range(50):
    veiculo_id = random.choice(veiculos)
    data = fake.date_between(start_date='-60d', end_date='today')
    litros = round(random.uniform(20, 80), 2)
    valor_total = round(litros * random.uniform(4.5, 6.5), 2)
    km_registrado = random.randint(30000, 180000)
    cursor.execute("""
        INSERT INTO abastecimentos (id_veiculo, data, litros, valor_total, km_registrado)
        VALUES (%s, %s, %s, %s, %s)
    """, (veiculo_id, data, litros, valor_total, km_registrado))

# ---------- CUSTOS FIXOS ----------
for _ in range(40):
    veiculo_id = random.choice(veiculos)
    descricao = random.choice(["IPVA", "Seguro", "Licenciamento", "Rastreamento", "Aluguel"])
    valor = round(random.uniform(100, 900), 2)
    data_lancamento = fake.date_between(start_date='-90d', end_date='today')
    cursor.execute("""
        INSERT INTO custos_fixos (id_veiculo, descricao, valor, data_lancamento)
        VALUES (%s, %s, %s, %s)
    """, (veiculo_id, descricao, valor, data_lancamento))

# ---------- ALERTAS ----------
for _ in range(15):
    veiculo_id = random.choice(veiculos)
    tipo_alerta = random.choice(["Revisão", "Troca de óleo", "Vencimento do seguro"])
    mensagem = f"Alerta gerado: {tipo_alerta}"
    data_geracao = fake.date_between(start_date='-30d', end_date='today')
    resolvido = random.choice([True, False])
    cursor.execute("""
        INSERT INTO alertas (id_veiculo, tipo_alerta, mensagem, data_geracao, resolvido)
        VALUES (%s, %s, %s, %s, %s)
    """, (veiculo_id, tipo_alerta, mensagem, data_geracao, resolvido))

conn.commit()
cursor.close()
conn.close()
print("✅ Dados fictícios gerados e inseridos com sucesso no banco 'frota'.")
