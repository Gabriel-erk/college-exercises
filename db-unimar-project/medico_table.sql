CREATE TABLE profissional (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(100),
    registro_profissional VARCHAR(50) UNIQUE NOT NULL
);


