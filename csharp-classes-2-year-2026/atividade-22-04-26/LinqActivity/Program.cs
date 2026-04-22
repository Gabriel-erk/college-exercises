using LinqActivity;

Console.WriteLine("------------ Inicializando atividade ------------");
var alunoConsulta = new AlunoConsulta();

void ImprimirAlunos(string titulo, List<Aluno> alunos)
{
    Console.WriteLine($"\n{titulo}");
    foreach (var aluno in alunos)
    {
        Console.WriteLine($"{aluno.Codigo} - {aluno.Nome} - {aluno.Idade} anos - {aluno.Email}");
    }
}

void ImprimirCodigos(string titulo, List<string> codigos)
{
    Console.WriteLine($"\n{titulo}");
    foreach (var codigo in codigos)
    {
        Console.WriteLine(codigo);
    }
}

ImprimirAlunos("1) BuscaAlunosComGmail()", alunoConsulta.BuscaAlunosComGmail());
ImprimirAlunos("2) BuscaAlunosComIdadeMaiorQue(30)", alunoConsulta.BuscaAlunosComIdadeMaiorQue(30));
Console.WriteLine($"\n3) RetornaAnoDoAlunoMaisVelho() = {alunoConsulta.RetornaAnoDoAlunoMaisVelho()}");
ImprimirCodigos("4) Retorna5CodigosQueIniciamCom(\"A\")", alunoConsulta.Retorna5CodigosQueIniciamCom("A"));
ImprimirCodigos("5) Retorna5CodigosQueIniciamCom(\"B\")", alunoConsulta.Retorna5CodigosQueIniciamCom("B"));
ImprimirAlunos("6) BuscaAlunosContendo(\"ana\")", alunoConsulta.BuscaAlunosContendo("ana"));
ImprimirAlunos("7) BuscaAlunosContendo(\"gmail\")", alunoConsulta.BuscaAlunosContendo("gmail"));
ImprimirAlunos("8) Retorna5AlunosMaisVelhosPorPagina(1)", alunoConsulta.Retorna5AlunosMaisVelhosPorPagina(1));
ImprimirAlunos("9) Retorna5AlunosMaisVelhosPorPagina(2)", alunoConsulta.Retorna5AlunosMaisVelhosPorPagina(2));
ImprimirAlunos("10) Retorna5AlunosMaisVelhosPorPagina(3)", alunoConsulta.Retorna5AlunosMaisVelhosPorPagina(3));

Console.WriteLine("\n------------ Fim do teste ------------");
