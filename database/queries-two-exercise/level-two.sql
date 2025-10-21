-- 6. Aumentar preço dos produtos com valor < 1000 em 10%
UPDATE produtos
SET preco = preco * 1.10
WHERE preco < 1000.00 AND id IS NOT NULL;

-- 7. Diminuir a quantidade dos produtos com valor > 5000 em 2 unidades
UPDATE produtos
SET quantidade = quantidade - 2
WHERE preco > 5000.00;

-- 8. Corrigir produtos com preço igual a 0.00 para 100.00
UPDATE produtos
SET preco = 100.00
WHERE preco = 0.00;

-- 9. Altere o nome dos produtos que contenham “RAM” para “Memória RAM DDR4”
UPDATE produtos
SET nome = 'Memória RAM DDR4'
WHERE nome LIKE '%RAM%';

-- 10. Aumentar preço de todos os produtos com quantidade < 20 em 5%
UPDATE produtos
SET preco = preco * 1.05
WHERE quantidade < 20 ;

SELECT * FROM produtos;
