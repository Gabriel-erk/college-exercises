using UnimarAula1;

namespace UnimarDesktop.Screens
{
    public partial class AlunoList : Form
    {

        public AlunoList(AlunoService service)
        {
            this.service = service;
            InitializeComponent();
            CarregarAlunosTable();
        }
        private readonly AlunoService service;

        private void CarregarAlunosTable()
        {
            foreach (var item in service.Listar())
            {
                gridAlunos.Rows.Add(
                    item.Codigo,
                    item.Nome,
                    item.DataNascimento.ToString("dd/MM/yyyy"),
                    item.Email
                );
            }
        }


        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
