CREATE DATABASE futcontra; 
USE futcontra;

CREATE TABLE tb_arena (
arena_id INT PRIMARY KEY AUTO_INCREMENT,
    endereco VARCHAR(255) NOT NULL,
    horario_funcionamento VARCHAR(100) NOT NULL,  
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tb_agendamento(
 agendamento_id INT PRIMARY KEY AUTO_INCREMENT,
    arena_id INT,  -- Relaciona com a tabela tb_arena
    data_agendamento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (arena_id) REFERENCES tb_arena(arena_id)
        ON DELETE CASCADE
);
