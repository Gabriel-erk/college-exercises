using System;
using System.Collections.Generic;
using System.Text;

namespace atividade_27_02_26.Models
{
    class Exercise3
    {
        public double solucao(double a, double b, double c)
        {
            int pesoNotaA = 2;
            int pesoNotaB = 3;
            int pesoNotaC = 5;
            int somaPesos = pesoNotaA + pesoNotaB + pesoNotaC;
            return ((a * pesoNotaA) + (b * pesoNotaB) + (c * pesoNotaC)) / somaPesos;
        }
    }
}
