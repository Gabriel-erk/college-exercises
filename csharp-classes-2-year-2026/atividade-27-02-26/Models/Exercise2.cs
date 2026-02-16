using System;
using System.Collections.Generic;
using System.Text;

namespace atividade_27_02_26.Models
{
    class Exercise2
    {
        public string solucao(double numero)
        {
            // colocando vários 0 pois estava dessa forma no exercício
            if (numero >= 0 && numero <= 25.0000)
            {
                return "Intervalo [0,25]";
            }
            else if (numero >= 25.00001 && numero <= 50.0000000)
            {
                return "Intervalo (25,50]";
            }
            else if (numero >= 50.00001 && numero <= 75.0000000)
            {
                return "Intervalo (50,75]";
            }
            else if (numero >= 75.00001 && numero <= 100.0000000)
            {
                return "Intervalo (75,100]";
            }
            else
            {
                return "Fora de intervalo";
            }
        }
    }
}
