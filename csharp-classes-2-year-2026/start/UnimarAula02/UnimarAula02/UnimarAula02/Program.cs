using UnimarAula02;

while (true)
{
    Console.ReadKey();
    Console.Clear();
    var opcao = int.Parse(Console.ReadLine());

    if (opcao == 1)
    {
        Console.WriteLine("Digite a qntd de pessoas no andar um:");
        var a1 = int.Parse(Console.ReadLine());
        Console.WriteLine("Digite a qntd de pessoas no andar dois:");
        var a2 = int.Parse(Console.ReadLine());
        Console.WriteLine("Digite a qntd de pessoas no andar três:");
        var a3 = int.Parse(Console.ReadLine());
        var att1 = new Atividade1();
        var resultado = att1.solucao(a1,a2,a3);
        Console.WriteLine(resultado);
    }
    else if (opcao == 2)
    {
        var att2 = new Atividade2();
        Console.WriteLine("Digite o valor de t:");
        var t = int.Parse(Console.ReadLine());
        att2.solucao(t);
    }
    else if (opcao == 3) { 
        // EXECUTA ATT 3
    }
    else
    {
        Console.WriteLine("Opção inválida");
    }
}