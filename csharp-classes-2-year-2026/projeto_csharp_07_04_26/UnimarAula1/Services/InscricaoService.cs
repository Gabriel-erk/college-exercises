
using System.ComponentModel.DataAnnotations;
using UnimarAula1.Models;

namespace UnimarAula1
{
    public class InscricaoService
    {
        private AlunoService alunoService;
        private CursoService cursoService;
        public InscricaoService(AlunoService alunoService, CursoService cursoServ)
        {
            this.alunoService = alunoService;
            cursoService = cursoServ;
        } 
        private List<Inscricao> list = new List<Inscricao>();
        private int contador = 1;
        public bool Criar(Inscricao inscr)
        {
            if (!Validar(inscr))
            {
                return false;
            }
            inscr.Id = contador++;
            list.Add(inscr);
            return true;
        }
        public bool Validar(Inscricao a)
        {
            // var alunoService = new AlunoService();

            a.Aluno = alunoService.Buscar(a.Aluno.Codigo); // se nao achar devolve null
            a.Curso = cursoService.Buscar(a.Curso.Id);

            var contexto = new ValidationContext(a);
            var erros = new List<ValidationResult>();
            var objetoValido = Validator.
                    TryValidateObject(
                        a,
                        contexto,
                        erros,
                        true
                    );


            var inscricaoExiste = list.Any(item => item.Aluno.Codigo == a.Aluno.Codigo &&
                                        item.Curso.Id == a.Curso.Id);
            if (inscricaoExiste)
            {
                erros.Add(new ValidationResult("Já existe essa incrição para esse aluno",
                new[] { "Codigo" }));
                objetoValido = false;
            }

            foreach (var erro in erros)
            {
                Console.WriteLine("{0}: {1}",
                    erro.MemberNames.First(),
                    erro.ErrorMessage);
            }
            return objetoValido;
        }

        public List<Inscricao> Listar()
        {
            return list.ToList();
        }

        public Inscricao Buscar(int codigo)
        {
            // LINQ = Language Integrated Query
            var aluno = list.FirstOrDefault(
                (item) => item.Id == codigo);
            return aluno;
        }
    }
}
