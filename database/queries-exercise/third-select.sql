SELECT COUNT(*) AS total_produtos FROM produtos;

SELECT SUM(quantidade) AS soma_estoques FROM produtos;

SELECT AVG(preco) AS preco_medio FROM produtos;

SELECT MIN(preco) AS menor_preco, MAX(preco) AS maior_preco FROM produtos;

