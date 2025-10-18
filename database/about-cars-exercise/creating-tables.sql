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

