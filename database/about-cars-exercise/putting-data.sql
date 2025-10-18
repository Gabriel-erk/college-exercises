INSERT INTO clientes (nome, cpf, telefone, endereco)
VALUES
('João Silva', '123.456.789-00', '11999999999', 'Rua das Flores, 123'),
('Maria Oliveira', '987.654.321-00', '21988888888', 'Av. Paulista, 456'),
('Carlos Souza', '555.444.333-22', '31977777777', 'Rua Central, 789');

INSERT INTO funcionarios (nome, cargo, email)
VALUES
('Ana Pereira', 'Atendente', 'ana@seguradora.com'),
('Ricardo Lima', 'Gerente', 'ricardo@seguradora.com'),
('Fernanda Rocha', 'Analista', 'fernanda@seguradora.com');

INSERT INTO veiculos (id_cliente, marca, modelo, ano, placa)
VALUES
(1, 'Toyota', 'Corolla', 2020, 'ABC1A23'),
(2, 'Honda', 'Civic', 2019, 'XYZ9B88'),
(3, 'Ford', 'Fiesta', 2021, 'JHK3D45');

INSERT INTO apolices (id_veiculo, id_funcionario, valor, data_inicio, data_fim)
VALUES
(1, 1, 2500.00, '2025-01-01', '2025-12-31'),
(2, 2, 2800.00, '2025-02-10', '2026-02-10'),
(3, 3, 3000.00, '2025-03-15', '2026-03-15');

INSERT INTO sinistros (id_veiculo, data_ocorrencia, descricao, valor_prejuizo)
VALUES
(1, '2025-06-10', 'Batida leve na traseira', 1200.00),
(2, '2025-07-05', 'Vidro quebrado por vandalismo', 800.00),
(3, '2025-08-20', 'Perda total por colisão', 15000.00);
