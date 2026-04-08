using UnimarAula1;
using UnimarAula1.Models;

var service = new AlunoService();
var cursoService = new CursoService();
var inscricaoService = new InscricaoService(service, cursoService);

while (true)
{
    Console.ReadKey();
    Console.Clear();
    Console.WriteLine("Digite uma opção: ");

    int opcao;
    try
    {
        opcao = int.Parse(Console.ReadLine()); // int(input())
    }
    catch (FormatException excecao)
    {
        Console.WriteLine("Opção inválida: {0}", excecao.Message);
        continue;
    }
    catch (Exception excecao)
    {
        Console.WriteLine("Erro desconhecido: {0}", excecao.Message);
        continue;
    }
    // try: except:

    if (opcao == 1)
    {
        Console.WriteLine("Aluno bolsista?");
        var resposta = Console.ReadLine();
        Aluno aluno;

        if (resposta.ToLower() == "s")
        {
            Console.WriteLine("Digite o desconto: ");
            var desconto = int.Parse(Console.ReadLine());
            aluno = new Bolsista
            {
                PorcentagemDesconto = desconto
            };

        }
        else
        {
            aluno = new Aluno();
        }


        Console.WriteLine("Digite o nome:");
        var nome = Console.ReadLine();

        Console.WriteLine("Digite o codigo:");
        var codigo = Console.ReadLine();

        Console.WriteLine("Digite a data de nascimento:");
        var dataNascimento = DateTime.Parse(Console.ReadLine());


        Console.WriteLine("Digite o email:");
        var email = Console.ReadLine();

        aluno.Nome = nome;
        aluno.Codigo = codigo;
        aluno.DataNascimento = dataNascimento;
        aluno.Email = email;

        aluno.PrintDados();

        var sucesso = service.Criar(aluno, out var erros);

        if (!sucesso)
        {
            Console.WriteLine("Erros ao cadastrar:");

            foreach (var erro in erros)
            {
                Console.WriteLine($"{erro.MemberNames.First()}: {erro.ErrorMessage}");
            }
        }

    }

    else if (opcao == 2)
    {
        var alunos = service.Listar();

        foreach (var item in alunos)
        {
            item.PrintDados();
            Console.WriteLine("====================");
        }
    }
    else if (opcao == 3)
    {
        Console.WriteLine("Digite o codigo:");
        var busca = Console.ReadLine();
        var alunoEncontrado = service.Buscar(busca);
        if (alunoEncontrado == null)
        {
            Console.WriteLine("Aluno não encontrado");
        }
        else
        {
            alunoEncontrado.PrintDados();
            Console.WriteLine("Digite o nome:");
            var nome = Console.ReadLine();
            Console.WriteLine("Digite o email:");
            var email = Console.ReadLine();
            alunoEncontrado.Nome = nome;
            alunoEncontrado.Email = email;
        }

        // foreach (var aluno in service.Listar())
        // {
        //     if (aluno.Codigo == busca)
        //     {
        //         alunoEncontrado = aluno;
        //     }
        // }
    }
    else if (opcao == 10)
    {
        Console.Write("Pesquisa: ");
        var pesquisa = Console.ReadLine();
        var alunosEncontrados = service.Pesquisa(pesquisa);
        if (alunosEncontrados.Count == 0)
        {
            Console.WriteLine("Nenhum aluno encontrado");
        }
        else
        {
            foreach (var aluno in alunosEncontrados)
            {
                aluno.PrintDados();
                Console.WriteLine("====================");
            }
        }
    }
}
