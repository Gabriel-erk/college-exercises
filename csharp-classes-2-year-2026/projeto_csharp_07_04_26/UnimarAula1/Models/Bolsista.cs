namespace UnimarAula1.Models;

// Bolsista extends Aluno
public class Bolsista : Aluno
{
    public int PorcentagemDesconto { get; set; }

    public override void PrintDados()
    {
        // Printar todos os dados do bolsista
        // super.metodo()
        base.PrintDados();
        Console.WriteLine("Desconto: {0}%", PorcentagemDesconto);
    }
}