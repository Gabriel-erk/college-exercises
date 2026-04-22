namespace LinqActivity
{
    public class AlunoConsulta
    {
        private List<Aluno> _alunos;
        public AlunoConsulta()
        {
            _alunos = Seeder.GetAlunos();
        }

        /// <summary>
        /// Retorna a lista de alunos cujo e-mail termina com "@gmail.com". Por exemplo, 
        /// se um aluno tem o e-mail "aluno@gmail.com", ele deve ser incluído na lista retornada, 
        /// mas um aluno com e-mail "gmail.com@hotmail.com" e "email@gmail.com.br" .não devems ser incluídos.
        /// </summary>
        /// <returns>Lista de alunos cujo e-mail é "@gmail.com"</returns>
        public List<Aluno> BuscaAlunosComGmail()
        {
            return _alunos
            .Where(a => a.Email.EndsWith("@gmail.com"))
            .ToList();
        }

        /// <summary>
        /// Retorna a lista de alunos cuja idade é maior que a idade fornecida.
        /// </summary>
        /// <param name="idade">Idade a ser comparada</param>
        /// <returns>Lista de alunos com idade maior que a fornecida</returns>
        public List<Aluno> BuscaAlunosComIdadeMaiorQue(int idade)
        {
            return _alunos
            .Where(a => a.Idade > idade)
            .ToList();
        }

        /// <summary>
        /// Retorna o ano de nascimento do aluno mais velho.
        /// Por exemplo, se o aluno mais velho nasceu em 1990, o método deve retornar 1990.
        /// </summary>
        /// <returns>Ano de nascimento do aluno mais velho</returns>
        public int RetornaAnoDoAlunoMaisVelho()
        {
            return _alunos
            .OrderBy(a => a.DataNascimento)
            .First()
            .DataNascimento.Year;
        }

        /// <summary>
        /// Retorna apenas os códigos dos 5 alunos cuja inicial do nome seja igual à string passada como parâmetro. 
        /// Por exemplo, se a string for "A", os códigos dos alunos com nome "Ana Silva" e "André Souza" devem ser retornados, 
        /// mas não o código do aluno com nome "João Pereira".
        /// </summary>
        /// <param name="inicial">Inicial a ser pesquisada</param>
        /// <returns>Lista de códigos dos alunos cuja inicial do nome corresponde à inicial fornecida</returns>
        public List<string> Retorna5CodigosQueIniciamCom(string inicial)
        {
            return _alunos
            .Where(a => a.Nome.StartsWith(inicial))
            .Take(5)
            .Select(a => a.Codigo)
            .ToList();
        }

        /// <summary>
        /// Retorna todos os alunos cujo nome ou e-mail contém o texto digitado, sem considerar maiúsculas ou minúsculas. 
        /// Por exemplo, se o texto digitado for "ana", os alunos com nome "Ana Silva" ou e-mail "ana@email.com" devem ser retornados, 
        /// assim como os alunos com nome "Joana Souza" ou e-mail "joana@email.com".
        /// </summary>
        /// <param name="texto">Texto a ser pesquisado no nome ou e-mail dos alunos</param>
        /// <returns>Lista de alunos cujo nome ou e-mail contém o texto fornecido</returns>
        public List<Aluno> BuscaAlunosContendo(string texto)
        {
            texto = texto.ToLower();

            return _alunos
                .Where(a => a.Nome.ToLower().Contains(texto) ||
                            a.Email.ToLower().Contains(texto))
                .ToList();
        }
        /// <summary>
        /// Busca 5 alunos por página, ordenados por idade e por nome, do mais velho para o mais novo. A primeira página é a página 1,
        /// a segunda página é a página 2, e assim por diante. Por exemplo, se houver 12 alunos, a página 1 retornará os 5 alunos mais velhos,
        /// </summary>
        /// <param name="page">Número da página começando em 1</param>
        /// <returns>Retorna a lista correspondente aos 5 alunos ordenados daquela página</returns>
        public List<Aluno> Retorna5AlunosMaisVelhosPorPagina(int page)
        {
            return _alunos
            .OrderBy(a => a.DataNascimento)
            .ThenBy(a => a.Nome)
            .Skip((page - 1) * 5)
            .Take(5)
            .ToList();
        }
    }
}
