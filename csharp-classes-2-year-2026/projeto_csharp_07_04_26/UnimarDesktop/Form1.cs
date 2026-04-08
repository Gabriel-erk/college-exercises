using UnimarAula1;
using UnimarDesktop.Screens;

namespace UnimarDesktop
{
    public partial class Form1 : Form
    {
        public AlunoForm TelaCadastroAluno { get; private set; }
        public AlunoService Service { get; }

        public Form1()
        {
            Service = new AlunoService();
            InitializeComponent();
        }

        private void onclick_botaoCadastrarAluno(object sender, EventArgs e)
        {
            MessageBox.Show("Abrir tela de aluno"); // alert()
            TelaCadastroAluno = new AlunoForm(Service);
            TelaCadastroAluno.ShowDialog(this);
        }

        private void primaryButton1_Click(object sender, EventArgs e)
        {
            var listAluno = new AlunoList(Service);
            listAluno.ShowDialog(this);
        }
    }
}
