UPDATE produtos
SET nome = 'Mouse Gamer Logitech G Pro X',
    preco = 799.90
WHERE id = 1;

UPDATE produtos
SET nome = 'Memória RAM DDR5 32GB',
    quantidade = 25
WHERE nome = 'Memoria RAM 32';

UPDATE produtos
SET preco = preco * 1.08,
    quantidade = quantidade - 1;
