CREATE DATABASE biblioteca_two
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;

USE biblioteca_two;

CREATE TABLE autores (
  id_autor INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  nacionalidade VARCHAR(50)
);
CREATE TABLE categorias (
  id_categoria INT AUTO_INCREMENT PRIMARY KEY,
  nome_categoria VARCHAR(50) NOT NULL
);
CREATE TABLE livros (
  id_livro INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(150) NOT NULL,
  ano_publicacao INT,
  id_autor INT,
  id_categoria INT,
  FOREIGN KEY (id_autor) REFERENCES autores(id_autor),
  FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);
CREATE TABLE usuarios (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  telefone VARCHAR(20)
);
CREATE TABLE emprestimos (
  id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT,
  id_livro INT,
  data_emprestimo DATE,
  data_devolucao DATE,
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
  FOREIGN KEY (id_livro) REFERENCES livros(id_livro)
);

INSERT INTO autores (nome, nacionalidade)
VALUES 
('Machado de Assis', 'Brasileiro'),
('George Orwell', 'Britânico'),
('J. K. Rowling', 'Britânica');

INSERT INTO categorias (nome_categoria)
VALUES 
('Romance'),
('Ficção Científica'),
('Fantasia');

INSERT INTO livros (titulo, ano_publicacao, id_autor, id_categoria)
VALUES
('Dom Casmurro', 1899, 1, 1),
('1984', 1949, 2, 2),
('Harry Potter e a Pedra Filosofal', 1997, 3, 3);

INSERT INTO usuarios (nome, email, telefone)
VALUES
('Ana Souza', 'ana@email.com', '11987654321'),
('Carlos Lima', 'carlos@email.com', '21999998888'),
('Fernanda Alves', 'fernanda@email.com', '11955554444');

INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo, data_devolucao)
VALUES
(1, 1, '2025-10-01', '2025-10-10'),
(2, 3, '2025-10-05', '2025-10-15'),
(3, 2, '2025-10-10', '2025-10-20');

SELECT 
  l.id_livro,
  l.titulo,
  l.ano_publicacao,
  a.nome AS autor,
  c.nome_categoria AS categoria
FROM livros l
JOIN autores a ON l.id_autor = a.id_autor
JOIN categorias c ON l.id_categoria = c.id_categoria;

SELECT * FROM usuarios;

SELECT * FROM livros WHERE ano_publicacao > 1950;

SELECT 
  e.id_emprestimo,
  u.nome AS usuario,
  l.titulo AS livro,
  e.data_emprestimo,
  e.data_devolucao
FROM emprestimos e
JOIN usuarios u ON e.id_usuario = u.id_usuario
JOIN livros l ON e.id_livro = l.id_livro;
