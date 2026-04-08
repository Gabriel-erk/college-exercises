
using System.ComponentModel.DataAnnotations;
using UnimarAula1.Models;

namespace UnimarAula1
{
    public class AlunoService
    {
        private List<Aluno> list = new List<Aluno>();

        public bool Criar(Aluno aluno, out List<ValidationResult> erros)
        {
            if (!Validar(aluno, out erros))
            {
                return false;
            }
            list.Add(aluno);
            return true;
        }
        public bool Validar(Aluno a, out List<ValidationResult> erros)
        {
            var contexto = new ValidationContext(a);
            erros = new List<ValidationResult>();
            var objetoValido = Validator.
                    TryValidateObject(
                        a,
                        contexto,
                        erros,
                        true
                    );
            if (!string.IsNullOrEmpty(a.Codigo))
            {
                var codigoExistente = list.Any(item => item.Codigo == a.Codigo);
                if (codigoExistente)
                {
                    erros.Add(new ValidationResult("Já existe outro aluno com esse código",
                    new[] { "Codigo" }));
                    objetoValido = false;
                }
            }

            foreach (var erro in erros)
            {
                Console.WriteLine("{0}: {1}",
                    erro.MemberNames.First(),
                    erro.ErrorMessage);
            }

            return objetoValido;
        }

        public List<Aluno> Listar()
        {
            return list.ToList();
        }

        public Aluno Buscar(string codigo)
        {
            // LINQ = Language Integrated Query
            var aluno = list.FirstOrDefault(
                (item) => item.Codigo == codigo
            );
            return aluno;
        }

        public List<Aluno> Pesquisa(string texto)
        {
            // var resultado = new List<Aluno>();
            // foreach (var aluno in list)
            // {
            //     if (aluno.Nome.Contains(texto) 
            //     || aluno.Email.Contains(texto)
            //     || aluno.Codigo == texto
            //     )
            //     {
            //         resultado.Add(aluno);
            //     }
            // }
            var resultado = list
                .Where(
                (item) => item.Nome.Contains(texto)
                    || item.Email.Contains(texto)
                    || item.Codigo == texto
                )
                .OrderBy(item =>
                {
                    return item.Codigo;
                });

            var resultado2 = from item in list
                             where item.Nome.Contains(texto)
                                 || item.Email.Contains(texto)
                                 || item.Codigo == texto
                             orderby item.Codigo
                             select item;
            // .Take(5)
            // .Select(a => a.Nome);
            return resultado.ToList();
        }
        // Listar(int, int)
        public List<Aluno> Listar(int pageSize, int page)
        {
            var take = pageSize;
            var skip = (page - 1) * pageSize;
            return list.Skip(skip).Take(take).ToList();
        }


        public List<Aluno> Listar(string a, int b)
        {
            return list;
        }
    }
}
