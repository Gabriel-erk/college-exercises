using System;
using System.Collections.Generic;
using System.Text;

namespace UnimarAula01
{
    internal class ComandosBasicosDaLinguagem
    {
        public static void Executar()
        {
            Console.WriteLine("Hello, World! I'm the best coder of unimar.");

            //var nome = Console.ReadLine();
            // {0} indica que quero o parâmetro da posição 0, ou seja, o que será considerado o "parâmetro da posição 0" será a primeira váriavel após a "," após o fechamenteo das aspas da nossa string
            // \n aplica uma quebra de linha
            // ctrl + f5 para executar o arquivo gerará um arquivo.exe e o executará na mesma hora (o que vemos ao executar esse comando e abrir o nosso terminal)
            // Console.WriteLine("Seu nome é: {0} \n {0}", nome);

            var x = 10;
            //{0:tipoDeFormatacaoAqui} tudo que vier depois dos : é um tipo de formatação, em n3 trago uma format para o valor de x e C trago outra
            Console.WriteLine("Valor de x é: {0:}", x);
            Console.WriteLine("Valor de x é: {0:N3}", x);
            Console.WriteLine("Valor de x é: {0:C}", x);


            var data = new DateTime(2026, 2, 4);
            var agora = DateTime.Now;
            var hoje = DateTime.Today;
            // pegando a data de amanha, onde a função addDays adiciona um dia (valor passado de parâmetro), retornando o dia de amanha
            var amanha = DateTime.Today.AddDays(1);
            // pegando a hora 12
            var meioDia = DateTime.Today.AddHours(12);
            // aplicando formatãção/mascara (do tipo data) para o primeiro parametro passado(0) que é do tipo data
            Console.WriteLine("{0:dd/MM/yyyy}", data);
            Console.WriteLine("-- Acessando métodos disponíveis dentro da váriavel dia --");
            Console.WriteLine("{0} {1} {2} {3} {4}", hoje.Year, hoje.Month, hoje.Day, hoje.DayOfWeek, hoje.DayOfYear);

            Console.WriteLine("--  Exibindo números ímpares e pares de 1 a 10 --");
            for (int i = 1; i <= 10; i++)
            {
                if (i % 2 == 0)
                {
                    Console.WriteLine($"Número {i} é par.");
                }
                else
                {
                    Console.WriteLine($"Número {i} é ímpar.");
                }
            }

            var numeros = new int[10]; // cria um vetor/array para 10 números INTEIROS (suportará apenas isso, não mais e nem nada de outro tipo, como string, float etc)
            var numList = new List<int>(); // lista de números (não possui limite)
            numList.Add(1);
        }
    }

}


