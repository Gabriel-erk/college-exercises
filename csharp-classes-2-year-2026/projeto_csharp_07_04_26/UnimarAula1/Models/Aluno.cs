using System.ComponentModel.DataAnnotations;

namespace UnimarAula1.Models
{
    public class Aluno
    {
        // @required
        [Required(ErrorMessage = "O nome do aluno é obrigatório")]
        [StringLength(100, MinimumLength = 10)]
        [RegularExpression("^[A-Z][A-zA-z]+ [A-Z][A-zA-z ]+[^ ]$")]
        public string Nome { get; set; }
        [Required, StringLength(10)]
        [RegularExpression("^[0-9]+$")]
        public string Codigo { get; set; }
        public DateTime DataNascimento { get; set; }

        [Range(16, 99)]
        public int Idade
        {
            get
            {
                var hoje = DateTime.Today;
                var anos = hoje.Year - DataNascimento.Year;
                var diaAnoNascimento = hoje.AddYears(-anos);
                if (DataNascimento > diaAnoNascimento)
                {
                    anos--;
                }
                return anos;
            }
        }
        private string email;
        public string Email
        {
            get { return email; }
            set { email = value.ToLower(); }
        }

        //public string GetEmail()
        //{
        //    return this.email;
        //}

        //public void SetEmail(string value)
        //{
        //    this.email = value;
        //}

        public virtual void PrintDados()
        {
            Console.WriteLine("Nome: {0}", Nome);
            Console.WriteLine("Codigo: {0}", Codigo);
            Console.WriteLine("Data de Nascimento: {0:dd/MM/yyyy}", DataNascimento);
            Console.WriteLine("Idade: {0}", Idade);
            Console.WriteLine("Email: {0}", Email);
        }
    }
}
