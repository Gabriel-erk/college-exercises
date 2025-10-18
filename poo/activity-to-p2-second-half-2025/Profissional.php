<?php
require_once 'Pessoa.php';

class Profissional extends Pessoa
{
    private $profissao;

    public function __construct($nome, $email, $telefone, $profissao)
    {
        parent::__construct($nome, $email, $telefone);
        $this->profissao = $profissao;
    }

    public function exibirInformacoes()
    {
        echo "Nome: {$this->nome} <br>";
        echo "Email: {$this->email} <br>";
        echo "Telefone: {$this->telefone} <br>";
        echo "Profissão: {$this->profissao} <br>";
    }

    public function aplicarEmVaga($vaga)
    {
        $vaga->adicionarProfissional($this);
    }
}
