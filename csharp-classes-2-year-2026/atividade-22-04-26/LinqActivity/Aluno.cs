namespace LinqActivity
{
    public class Aluno
    {
        public string Codigo { get; set; }
        public string Nome { get; set; }
        public DateTime DataNascimento { get; set; }
        public int Idade
        {
            get
            {
                var hoje = DateTime.Today;
                var idade = hoje.Year - DataNascimento.Year;
                var hojeAnoNascimento = hoje.AddYears(-idade);
                if (DataNascimento.Date > hojeAnoNascimento) idade--;
                return idade;
            }
        }
        public string Email { get; set; }
    }
}
