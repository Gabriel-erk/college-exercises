-- Categorias
INSERT INTO categorias (nome, descricao) VALUES
('Eletrônicos', 'Produtos eletrônicos em geral'),
('Roupas', 'Vestuário masculino e feminino'),
('Alimentos', 'Produtos alimentícios');

-- Produtos
INSERT INTO produtos (nome, preco, quantidade, descricao, categoria_id) VALUES
('Smartphone XYZ', 1500.00, 10, 'Smartphone com 128GB de armazenamento', 1),
('Notebook ABC', 3500.50, 5, 'Notebook 16GB RAM, 512GB SSD', 1),
('Camiseta Casual', 49.90, 30, 'Camiseta de algodão masculina', 2),
('Bolo de Chocolate', 25.00, 20, 'Bolo caseiro de chocolate 500g', 3),
('Mouse logitech G512', 25.00, 20, 'Mouse', 1),
('PS5 Pro', 25.00, 20, 'Console de última geração', 1),
('Memoria RAM 32', 25.00, 20, 'Peça de hardware', 1),
('Fone de Ouvido', 199.99, 15, 'Fone bluetooth com cancelamento de ruído', 1);

