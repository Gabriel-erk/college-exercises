<?php
require_once 'Cadastro.php';
require_once 'Profissional.php';

class Vaga implements Cadastro
{
    private $titulo;
    private $descricao;
    private $profissionais = [];

    public function __construct($titulo, $descricao)
    {
        $this->titulo = $titulo;
        $this->descricao = $descricao;
    }

    public function cadastrar()
    {
        echo "Vaga '{$this->titulo}' cadastrada com sucesso! <br>";
    }

    public function adicionarProfissional(Profissional $profissional)
    {
        $this->profissionais[] = $profissional;
        echo "Profissional {$profissional->exibirInformacoes()} aplicado na vaga '{$this->titulo}' <br>";
    }

    public function listarProfissionais()
    {
        echo "<h3>Profissionais aplicados na vaga: {$this->titulo}</h3>";
        foreach ($this->profissionais as $prof) {
            $prof->exibirInformacoes();
            echo "<hr>";
        }
    }
}
