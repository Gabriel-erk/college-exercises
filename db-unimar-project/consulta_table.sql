CREATE TABLE consulta (
    id_consulta INT AUTO_INCREMENT PRIMARY KEY,
    id_atendimento INT NOT NULL,
    id_profissional INT NOT NULL,
    data_hora DATETIME NOT NULL,

    FOREIGN KEY (id_atendimento) REFERENCES atendimento(id),
    FOREIGN KEY (id_profissional) REFERENCES profissional(id)
);
