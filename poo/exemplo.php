<?php
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
