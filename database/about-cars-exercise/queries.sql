SELECT * FROM clientes;

SELECT v.id_veiculo, v.marca, v.modelo, v.ano, v.placa, c.nome AS cliente
FROM veiculos v
JOIN clientes c ON v.id_cliente = c.id_cliente;

SELECT a.id_apolice, v.modelo AS veiculo, a.valor, a.data_inicio, a.data_fim, f.nome AS funcionario
FROM apolices a
JOIN veiculos v ON a.id_veiculo = v.id_veiculo
JOIN funcionarios f ON a.id_funcionario = f.id_funcionario;

SELECT s.id_sinistro, v.modelo AS veiculo, s.data_ocorrencia, s.descricao, s.valor_prejuizo
FROM sinistros s
JOIN veiculos v ON s.id_veiculo = v.id_veiculo;
