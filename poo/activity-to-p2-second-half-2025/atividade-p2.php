Cadastro.php

<?php

interface Cadastro
{
    public function cadastrar();
}

// Pessoa.php

abstract class Pessoa
{
    protected $nome;
    protected $email;
    protected $telefone;

    public function __construct($nome, $email, $telefone)
    {
        $this->nome = $nome;
        $this->email = $email;
        $this->telefone = $telefone;
    }

    abstract public function exibirInformacoes();
}

// Profissional.php

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

// Vaga.php

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

// exemplo.php (arquivo para execução das demais classes atrás)

require_once 'Vaga.php';
require_once 'Profissional.php';

// Criando vaga
$vaga1 = new Vaga("Desenvolvedor PHP", "Vaga para desenvolvedor PHP pleno.");
$vaga1->cadastrar();

// Criando profissionais
$prof1 = new Profissional("Gabriel", "gabriel@email.com", "999999999", "Desenvolvedor PHP");
$prof2 = new Profissional("Ana", "ana@email.com", "988888888", "Front-end Developer");

// Aplicando profissionais na vaga
$prof1->aplicarEmVaga($vaga1);
$prof2->aplicarEmVaga($vaga1);

// Listando profissionais aplicados
$vaga1->listarProfissionais();

// link para meu repositório do GitHub contendo esta atividade para caso tenha interesse em acessa-la:
// https://github.com/seu_usuario/seu_repositorio