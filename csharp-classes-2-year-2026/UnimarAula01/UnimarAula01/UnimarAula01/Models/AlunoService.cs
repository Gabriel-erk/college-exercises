using System;
using System.Collections.Generic;
using System.Text;

namespace UnimarAula01.Models
{
    internal class AlunoService
    {
        // campo (pois não posssui get e set, então não é uma propriedade), uma lista com o modificador de acesso "private" que recebe valores do tipo Aluno
        // após atribuição, estou dizendo que quero uma lista vazia com: "new List<Aluno>();
        private List<Aluno> list = new List<Aluno>();

        public bool Criar(Aluno aluno)
        {
            list.Add(aluno);
            return true;
        }

        public List<Aluno> Listar()
        {
            return list.ToList();
        }
    }
}
