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

