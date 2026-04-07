using System;

namespace Model
{
    public class Atividade1
    {
        public void Executar()
        {
            while (true)
            {
                string entrada = Console.ReadLine();

                if (string.IsNullOrEmpty(entrada))
                    continue;

                string[] valores = entrada.Split(' ');

                int x1 = int.Parse(valores[0]);
                int y1 = int.Parse(valores[1]);
                int x2 = int.Parse(valores[2]);
                int y2 = int.Parse(valores[3]);

                if (x1 == 0 && y1 == 0 && x2 == 0 && y2 == 0)
                    break;

                if (x1 == x2 && y1 == y2)
                {
                    Console.WriteLine(0);
                }
                else if (x1 == x2 || y1 == y2 || Math.Abs(x1 - x2) == Math.Abs(y1 - y2))
                {
                    Console.WriteLine(1);
                }
                else
                {
                    Console.WriteLine(2);
                }
            }
        }
    }
}