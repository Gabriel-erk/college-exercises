CREATE TABLE atendimento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    data_hora_inicio DATETIME NOT NULL,
    prioridade INT DEFAULT 0,
    status VARCHAR(20) DEFAULT 'aberto',

    FOREIGN KEY (id_paciente) REFERENCES paciente(id)
);
