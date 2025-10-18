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
