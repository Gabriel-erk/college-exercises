-- 1. Atualizar nome da categoria “Hardware” para “Componentes de PC”
UPDATE categorias
SET nome = 'Componentes de PC'
WHERE nome = 'Hardware';
-- 2. Corrigir nome do produto “Mouse logitech G512”
UPDATE produtos
SET nome = 'Mouse Logitech G512'
WHERE nome = 'Mouse logitech G512';
-- 3. Atualizar preço do produto “PS5 Pro” para 6299.00
UPDATE produtos
SET preco = 6299.00
WHERE nome = 'PS5 Pro';
-- 4. Alterar quantidade do produto “Memoria RAM 32” para 40 unidades
UPDATE produtos
SET quantidade = 40
WHERE nome = 'Memoria RAM 32';
-- 5. Diminuir em 1 unidade a quantidade do produto “PS5 Pro”
UPDATE produtos
SET quantidade = quantidade - 1
WHERE nome = 'PS5 Pro';

SELECT * FROM categorias;
SELECT * FROM produtos;
