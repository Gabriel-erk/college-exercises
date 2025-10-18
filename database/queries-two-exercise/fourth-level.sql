UPDATE produtos
SET preco = preco * 1.08
WHERE quantidade < 20;

UPDATE produtos
SET preco = 0.00
WHERE preco < 0;

UPDATE produtos
SET preco = preco * 1.12
WHERE nome LIKE '%Logitech%';

UPDATE produtos
SET quantidade = quantidade - 1
WHERE nome = 'PS5 Pro';

UPDATE produtos
SET preco = preco * 0.95
WHERE nome LIKE '%Memória%';

-- UPDATE produtos
-- SET categorias_id = 1
-- WHERE categorias_id IS NULL;

UPDATE produtos
SET quantidade = 100;
