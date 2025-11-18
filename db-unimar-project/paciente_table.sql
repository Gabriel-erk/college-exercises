CREATE TABLE paciente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL,
    genero varchar(255) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100),
    endereco VARCHAR(150),
    tipo_sanguineo VARCHAR(5),
    peculiaridade BOOLEAN DEFAULT 0,
    descricao_peculiaridade VARCHAR(255)
);

