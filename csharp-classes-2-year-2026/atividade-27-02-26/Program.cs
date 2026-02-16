using atividade_27_02_26.Models;
// trazendo para esse arquivo para que eu possa substituir a "," por "." na exibição da resposta no exercicio 2
using System.Globalization;

while (true)
{
    Console.ReadKey();
    Console.Clear();

    Console.WriteLine("Escolha uma opção:");
    Console.WriteLine("1 - Gasto de Combustível");
    Console.WriteLine("2 - Intervalo");
    Console.WriteLine("3 - Média 2");
    Console.WriteLine("0 - Sair");
    var opcao = int.Parse(Console.ReadLine());

    if (opcao == 1)
    {
        Console.WriteLine("== Gasto de Combustível ==");
        Console.WriteLine("Digite o tempo gasto na viagem:");
        var tempoGasto = int.Parse(Console.ReadLine());
        Console.WriteLine("Digite a velocidade média (em km/h):");
        var velocidadeMedia = float.Parse(Console.ReadLine());

        var attUm = new Exercise1();
        var resposta = attUm.solucao(tempoGasto, velocidadeMedia);
        // :F2 limita em 2 casas decimais a minha váriavel
        // Console.WriteLine($"{resposta:F2}");
        // CultureInfo.InvariantCulture permite que substitua a , por . na hora da exibição do valor decimal e f3 limita as casas decimais em 3
        Console.WriteLine(resposta.ToString("F3", CultureInfo.InvariantCulture));
    }
    else if (opcao == 2)
    {
        Console.WriteLine("=== Intervalo ===");
        Console.WriteLine("Digite o número:");
        // obs: meu sistema está configurado em pt-br, então tive de usar "," na hora dos valores decimais para obter as mesmas respostas do exercício (25,01 - 25,00 etc...)
        double numero = double.Parse(Console.ReadLine());

        var att2 = new Exercise2();
        var resposta = att2.solucao(numero);
        Console.WriteLine($"{resposta}");
    }
    else if (opcao == 3)
    {
        Console.WriteLine("=== Média 2 ===");
        // obs: meu sistema está configurado em pt-br, então tive de usar "," na hora dos valores decimais para obter as mesmas respostas do exercício (25,01 - 25,00 etc...)
        Console.WriteLine("Digite o valor da nota 1:");
        double a = double.Parse(Console.ReadLine());
        Console.WriteLine("Digite o valor da nota 2:");
        double b = double.Parse(Console.ReadLine());
        Console.WriteLine("Digite o valor da nota 3:");
        double c = double.Parse(Console.ReadLine());

        if (a >= 0 && a <= 10.0 && b >= 0 && b <= 10.0 && c >= 0 && c <= 10.0)
        {
            var att3 = new Exercise3();
            double resultado = att3.solucao(a, b, c);
            Console.WriteLine($"MEDIA = {resultado:F1}");
        }
        else
        {
            Console.WriteLine("Notas inválidas, tente novamente.");
            Console.WriteLine("Intervalo Permitido: 0 - 10.0");
        }
    } else
    {
        Console.WriteLine("Obrigado por usar minha aplicação!");
        break;
    }
}
