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
