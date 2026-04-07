using System;

namespace model
{
    public class Atividade2
    {
        public void Executar()
        {
            int n = int.Parse(Console.ReadLine());

            for (int i = 0; i < n; i++)
            {
                string linha = Console.ReadLine();

                int abertos = 0;
                int diamantes = 0;

                foreach (char c in linha)
                {
                    if (c == '<')
                    {
                        abertos++;
                    }
                    else if (c == '>' && abertos > 0)
                    {
                        diamantes++;
                        abertos--;
                    }
                }

                Console.WriteLine(diamantes);
            }
        }
    }
}