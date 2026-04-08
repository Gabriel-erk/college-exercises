
using System.ComponentModel.DataAnnotations;
using UnimarAula1.Models;

namespace UnimarAula1
{
    public class CursoService
    {
        private List<Curso> list = new List<Curso>();
        private int contador = 1;
        public bool Criar(Curso curso)
        {
            if (!Validar(curso))
            {
                return false;
            }
            curso.Id = contador++;
            list.Add(curso);
            return true;
        }
        public bool Validar(Curso a)
        {
            var contexto = new ValidationContext(a);
            var erros = new List<ValidationResult>();
            var objetoValido = Validator.
                    TryValidateObject(
                        a,
                        contexto,
                        erros,
                        true
                    );
            foreach (var erro in erros)
            {
                Console.WriteLine("{0}: {1}",
                    erro.MemberNames.First(),
                    erro.ErrorMessage);
            }
            return objetoValido; 
        }

        public List<Curso> Listar()
        {
            return list.ToList(); 
        }

        public Curso Buscar(int codigo)
        {
            // LINQ = Language Integrated Query
            var aluno = list.FirstOrDefault(
                (item) => item.Id == codigo);
            return aluno;
        }
    }
}
