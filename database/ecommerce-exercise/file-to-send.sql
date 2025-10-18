CREATE DATABASE ecommerce;
USE ecommerce;

-- Tabela de categorias
CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(255)
);
-- Tabela de produtos
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL,
    descricao TEXT
);
-- Categorias
INSERT INTO categorias (nome, descricao) VALUES
('Eletrônicos', 'Produtos eletrônicos em geral'),
('Roupas', 'Vestuário masculino e feminino'),
('Alimentos', 'Produtos alimentícios');
-- Produtos
INSERT INTO produtos (nome, preco, quantidade, descricao) VALUES
('Smartphone XYZ', 1500.00, 10, 'Smartphone com 128GB de armazenamento'),
('Notebook ABC', 3500.50, 5, 'Notebook 16GB RAM, 512GB SSD'),
('Camiseta Casual', 49.90, 30, 'Camiseta de algodão masculina'),
('Bolo de Chocolate', 25.00, 20, 'Bolo caseiro de chocolate 500g'),
('Fone de Ouvido', 199.99, 15, 'Fone bluetooth com cancelamento de ruído');

SELECT * FROM produtos;

SELECT * FROM categorias;