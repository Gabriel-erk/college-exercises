using System;
using System.Collections.Generic;
using System.Text;

namespace UnimarAula02
{
    class Atividade1
    {
        public int solucao(int a1, int a2, int a3)
        {
            // andar um sempre vai ser o mais distante do a3
            // se for o andar 3 o andar andar 1 andará 4 casas (2 indo e 2 voltando, ou seja, ele mesmo * 4), ignorando ele mesmo (pois quem está no 3, não gasta tempo com elevador até a máquina) e o do meio anda 2 casas (uma pra ir e outra pra voltar)
            // se for no andar 2, andar 3 * 2 (ida e volta) e andar 1 * 2 (ida e volta) 
            // se for andar 1, andar 3 * 4 (ida e volta) e andar 2 * 2 (ida e volta)      
            int resultado = a3 * 4 + a2 * 2;
            int resultado2 = a1 * 2 + a3 * 2;
            int resultado3 = a1 * 4 + a2 * 2;
            if (resultado <= resultado2 && resultado <= resultado3)
            {
                return resultado;
            } else if (resultado2 <= resultado && resultado2 <= resultado3)
            {
                return resultado2;
            } else
            {
                return resultado3;
            }
        }
    }
}
