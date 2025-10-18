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
