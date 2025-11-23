<?php

// ===============================
// 1. INTERFACE
// ===============================
interface AcoesPlataforma
{
    public function iniciarCurso();
    public function realizarAtividade();
}

// ===============================
// 2. CLASSE ABSTRATA USUARIO
// ===============================
abstract class Usuario
{

    protected string $nome;
    protected string $tipo;
    protected int $xp = 0;

    public function __construct($nome, $tipo)
    {
        $this->nome = $nome;
        $this->tipo = $tipo;
    }

    // Método protegido → não pode ser chamado de fora
    protected function adicionarXP(int $valor)
    {
        $this->xp += $valor;
    }

    // Métodos obrigatórios que as subclasses vão sobrescrever
    abstract public function registrarAcao(string $acao);
    abstract public function exibirStatus();
}

// ===============================
// 3. CLASSE ALUNO
// ===============================
class Aluno extends Usuario implements AcoesPlataforma
{

    public function __construct($nome)
    {
        parent::__construct($nome, "Aluno");
    }

    public function iniciarCurso()
    {
        $this->registrarAcao("curso");
    }

    public function realizarAtividade()
    {
        $this->registrarAcao("atividade");
    }

    // Polimorfismo
    public function registrarAcao(string $acao)
    {
        if ($acao === "curso") {
            $this->adicionarXP(50);
        } elseif ($acao === "atividade") {
            $this->adicionarXP(20);
        }
    }

    public function exibirStatus()
    {
        echo "Nome: {$this->nome} | Tipo: {$this->tipo} | XP: {$this->xp}\n";
    }
}

// ===============================
// 4. CLASSE PROFESSOR
// ===============================
class Professor extends Usuario implements AcoesPlataforma
{

    public function __construct($nome)
    {
        parent::__construct($nome, "Professor");
    }

    public function iniciarCurso()
    {
        $this->registrarAcao("criarCurso");
    }

    public function realizarAtividade()
    {
        $this->registrarAcao("criarAtividade");
    }

    // Polimorfismo
    public function registrarAcao(string $acao)
    {
        if ($acao === "criarCurso") {
            $this->adicionarXP(40);
        } elseif ($acao === "criarAtividade") {
            $this->adicionarXP(25);
        } elseif ($acao === "avaliacaoPositiva") {
            $this->adicionarXP(10);
        }
    }

    public function receberAvaliacaoPositiva()
    {
        $this->registrarAcao("avaliacaoPositiva");
    }

    public function exibirStatus()
    {
        echo "Nome: {$this->nome} | Tipo: {$this->tipo} | XP: {$this->xp}\n";
    }
}

// ===============================
// 5. SCRIPT DE TESTES
// ===============================

$aluno = new Aluno("Gabriel");
$professor = new Professor("Marcos");

// Simulações
$aluno->iniciarCurso();
$aluno->realizarAtividade();
$aluno->realizarAtividade();

$professor->iniciarCurso();
$professor->realizarAtividade();
$professor->receberAvaliacaoPositiva();
$professor->receberAvaliacaoPositiva();

// Status final
echo "\n--- STATUS FINAL ---\n";
$aluno->exibirStatus();
$professor->exibirStatus();
