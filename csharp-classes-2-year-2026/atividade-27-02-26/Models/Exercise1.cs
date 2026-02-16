using System;
using System.Collections.Generic;
using System.Text;

namespace atividade_27_02_26.Models
{
    class Exercise1
    {
        // objetivo dessa função é retornar os litros necessários para realizar uma viagem, assumindo que o carro de joãozinho faz 12km/l
        public float solucao (int tempoGasto, float velocidadeMediaKm)
        {
            float kmLitros = 12;
            // descobrindo distância percorrida para os próximos cálculos
            float distanciaPercorrida = tempoGasto * velocidadeMediaKm;
            float litrosGastos = distanciaPercorrida / kmLitros;
            return litrosGastos;
        }
    }
}
