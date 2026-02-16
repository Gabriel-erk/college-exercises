using System;
using System.Collections.Generic;
using System.Text;

namespace UnimarAula01.Models
{
    // internal é um modificador de acesso, assim como: public, private protected....
    public class Aluno
    {
        public string Nome { get; set; }
        public string Codigo { get; set; }

        public DateTime DataNascimento { get; set; }
        // criando atributo publico do tipo inteiro chamado idade onde os métodos get e set já são definidos em sua criação { get e não precisa de set pois a idade será calculada a partir da data de nascimento }
        // como abrimos {} no nosso get, podemos personaliza-lo da forma que quisermos, aqui, estamos realizando o cálculo exato do nascimento do usuário com base na sua data de nascimento
        // método get daqui será chamado toda vez que tentarmos executar 
        public int Idade { get {
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
        // sem ter os 2 (get e set) não é uma propriedade, apenas um CAMPO
        private string email;
        public string Email { 
            get { return email; } 
            // personalizando o set, fazendo com que converte tudo ue ele digitar para minúsculo
            set { email = value.ToLower(); } 
        }

        public void printDados()
        {
            Console.WriteLine($"Nome: {Nome}");
            Console.WriteLine($"Código: {Codigo}");
            Console.WriteLine("{0:dd/MM/yyyy}", DataNascimento);
            Console.WriteLine($"Idade: {Idade}");
            Console.WriteLine($"Email: {Email}");
        }
    }
}
