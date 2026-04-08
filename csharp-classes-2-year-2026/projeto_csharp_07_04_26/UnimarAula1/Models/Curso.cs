using System.ComponentModel.DataAnnotations;
using UnimarAula1.Enums;

namespace UnimarAula1.Models;

public class Curso
{
    public int Id { get; set; }
    [Required, StringLength(100)]
    public string Nome { get; set; }
    [Required]
    public string Descricao { get; set; }
    // Nível: Iniciante, Intermediário, Avançado e Expert
    public NivelCurso Nivel { get; set; }


    public void Validacao()
    {
        if (Nivel == NivelCurso.Iniciante)
        {
            
        }
        else if (Nivel == NivelCurso.Avancado)
        {
            
        }
    }
}