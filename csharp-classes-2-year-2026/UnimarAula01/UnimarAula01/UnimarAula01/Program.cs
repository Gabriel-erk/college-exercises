// See https://aka.ms/new-console-template for more information
// chamando nossa clase Aluno para poder realizar a instância de objetos a partir dela
using UnimarAula01.Models;

var service = new AlunoService();
while (true)
{
    Console.ReadKey();
    Console.Clear();
    Console.WriteLine("Digite uma opção: ");
    Console.WriteLine("1 - Criar aluno");
    Console.WriteLine("2 - Listar alunos");
    var opcao = int.Parse(Console.ReadLine());

    if (opcao == 1)
    {
        Console.WriteLine("Digite o nome:");
        var nome = Console.ReadLine();

        Console.WriteLine("Digite o código:");
        var codigo = Console.ReadLine();

        Console.WriteLine("Digite a data de nascimento:");
        // DateTime.Parse converte o retorno de Console.ReadLine para o tipo data
        var dataNascimento = DateTime.Parse(Console.ReadLine());

        Console.WriteLine("Digite o email:");
        var email = Console.ReadLine();

        // primeira forma de atribuir valores a objetos, onde o = chama automaticamente o set - aqui estamos criando o objeto e na linha abaixo definindo o primeiro atributo/propriedade dele,as propriedades aqui não são definidas em sua criação
        var aluno = new Aluno();
        aluno.Nome = nome;

        var aluno2 = new Aluno
        {
            // idade existe porém não preciso defini-la aqui pois ela não possui o set, logo, não irei passa-la na criação do objeto
            // aqui também o = chama o método set, porém, aqui estamos o chamando na criação do objeto
            Nome = nome,
            Codigo = codigo,
            DataNascimento = dataNascimento,
            Email = email
        };
        aluno2.printDados();
        service.Criar(aluno2);
    } else if (opcao == 2)
    {
        var alunos = service.Listar();

        foreach(var aluno in alunos)
        {
            aluno.printDados();
            Console.WriteLine("===============");
        }
    } 
}