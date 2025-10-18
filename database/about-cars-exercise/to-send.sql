CREATE DATABASE seguradora
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;

USE seguradora;

CREATE TABLE clientes (
  id_cliente INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  cpf VARCHAR(14) UNIQUE NOT NULL,
  telefone VARCHAR(20),
  endereco VARCHAR(150)
);

CREATE TABLE veiculos (
  id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
  id_cliente INT,
  marca VARCHAR(50),
  modelo VARCHAR(50),
  ano INT,
  placa VARCHAR(10) UNIQUE,
  FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE funcionarios (
  id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  cargo VARCHAR(50),
  email VARCHAR(100)
);

CREATE TABLE apolices (
  id_apolice INT AUTO_INCREMENT PRIMARY KEY,
  id_veiculo INT,
  id_funcionario INT,
  valor DECIMAL(10,2),
  data_inicio DATE,
  data_fim DATE,
  FOREIGN KEY (id_veiculo) REFERENCES veiculos(id_veiculo),
  FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id_funcionario)
);

CREATE TABLE sinistros (
  id_sinistro INT AUTO_INCREMENT PRIMARY KEY,
  id_veiculo INT,
  data_ocorrencia DATE,
  descricao TEXT,
  valor_prejuizo DECIMAL(10,2),
  FOREIGN KEY (id_veiculo) REFERENCES veiculos(id_veiculo)
);

INSERT INTO clientes (nome, cpf, telefone, endereco)
VALUES
('João Silva', '123.456.789-00', '11999999999', 'Rua das Flores, 123'),
('Maria Oliveira', '987.654.321-00', '21988888888', 'Av. Paulista, 456'),
('Carlos Souza', '555.444.333-22', '31977777777', 'Rua Central, 789');

INSERT INTO funcionarios (nome, cargo, email)
VALUES
('Ana Pereira', 'Atendente', 'ana@seguradora.com'),
('Ricardo Lima', 'Gerente', 'ricardo@seguradora.com'),
('Fernanda Rocha', 'Analista', 'fernanda@seguradora.com');

INSERT INTO veiculos (id_cliente, marca, modelo, ano, placa)
VALUES
(1, 'Toyota', 'Corolla', 2020, 'ABC1A23'),
(2, 'Honda', 'Civic', 2019, 'XYZ9B88'),
(3, 'Ford', 'Fiesta', 2021, 'JHK3D45');

INSERT INTO apolices (id_veiculo, id_funcionario, valor, data_inicio, data_fim)
VALUES
(1, 1, 2500.00, '2025-01-01', '2025-12-31'),
(2, 2, 2800.00, '2025-02-10', '2026-02-10'),
(3, 3, 3000.00, '2025-03-15', '2026-03-15');

INSERT INTO sinistros (id_veiculo, data_ocorrencia, descricao, valor_prejuizo)
VALUES
(1, '2025-06-10', 'Batida leve na traseira', 1200.00),
(2, '2025-07-05', 'Vidro quebrado por vandalismo', 800.00),
(3, '2025-08-20', 'Perda total por colisão', 15000.00);

SELECT * FROM clientes;

SELECT v.id_veiculo, v.marca, v.modelo, v.ano, v.placa, c.nome AS cliente
FROM veiculos v
JOIN clientes c ON v.id_cliente = c.id_cliente;

SELECT a.id_apolice, v.modelo AS veiculo, a.valor, a.data_inicio, a.data_fim, f.nome AS funcionario
FROM apolices a
JOIN veiculos v ON a.id_veiculo = v.id_veiculo
JOIN funcionarios f ON a.id_funcionario = f.id_funcionario;

SELECT s.id_sinistro, v.modelo AS veiculo, s.data_ocorrencia, s.descricao, s.valor_prejuizo
FROM sinistros s
JOIN veiculos v ON s.id_veiculo = v.id_veiculo;
