CREATE DATABASE biblioteca
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;
USE biblioteca;

-- Tabela de autores
CREATE TABLE autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50)
);
-- Tabela de categorias
CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(255)
);
-- Tabela de livros
CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    ano_publicacao INT,
    autor VARCHAR(100),
    categoria VARCHAR(50)
);
-- Tabela de usuários
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20)
);
-- Tabela de empréstimos
CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100),
    livro VARCHAR(150),
    data_emprestimo DATE,
    data_devolucao DATE
);
-- Autores
INSERT INTO autores (nome, nacionalidade) VALUES
('Machado de Assis', 'Brasileiro'),
('George Orwell', 'Inglês'),
('J. K. Rowling', 'Britânica');
-- Categorias
INSERT INTO categorias (nome, descricao) VALUES
('Romance', 'Livros de ficção e drama'),
('Ficção Científica', 'Livros com temas futuristas ou tecnológicos'),
('Fantasia', 'Livros com elementos mágicos e imaginários');
-- Livros
INSERT INTO livros (titulo, ano_publicacao, autor, categoria) VALUES
('Dom Casmurro', 1899, 'Machado de Assis', 'Romance'),
('1984', 1949, 'George Orwell', 'Ficção Científica'),
('Harry Potter e a Pedra Filosofal', 1997, 'J. K. Rowling', 'Fantasia');
-- Usuários
INSERT INTO usuarios (nome, email, telefone) VALUES
('Ana Souza', 'ana@gmail.com', '(14) 99999-1111'),
('Carlos Lima', 'carlos@gmail.com', '(14) 98888-2222'),
('Fernanda Reis', 'fernanda@gmail.com', '(14) 97777-3333');
-- Empréstimos
INSERT INTO emprestimos (usuario, livro, data_emprestimo, data_devolucao) VALUES
('Ana Souza', 'Dom Casmurro', '2025-10-10', '2025-10-20'),
('Carlos Lima', '1984', '2025-10-12', '2025-10-22'),
('Fernanda Reis', 'Harry Potter e a Pedra Filosofal', '2025-10-15', '2025-10-25');

-- Listar todos os livros cadastrados
SELECT * FROM livros;
-- Mostrar todos os usuários da biblioteca
SELECT * FROM usuarios;
-- Buscar livros publicados depois de um determinado ano (ex: 1950)
SELECT * FROM livros WHERE ano_publicacao > 1950;


