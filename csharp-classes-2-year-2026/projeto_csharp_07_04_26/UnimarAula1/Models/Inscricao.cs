using System.ComponentModel.DataAnnotations;

namespace UnimarAula1.Models;

public class Inscricao
{
    public Inscricao()
    {
        DataInscricao = DateTime.Now;
    }
    public int Id { get; set; }
    public DateTime DataInscricao { get; private set; }
    [Required]
    public Aluno Aluno { get; set; }
    [Required]
    public Curso Curso { get; set; }
}