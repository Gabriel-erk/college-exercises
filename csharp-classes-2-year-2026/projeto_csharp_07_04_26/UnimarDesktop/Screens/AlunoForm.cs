using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using UnimarAula1;
using UnimarAula1.Models;

namespace UnimarDesktop.Screens
{
    public partial class AlunoForm : Form
    {
        public AlunoForm()
        {
            InitializeComponent();
        }

        public AlunoService Service { get; }

        public AlunoForm(AlunoService service)
        {
            Service = service;
            InitializeComponent();
        }


        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void primaryButton1_Click(object sender, EventArgs e)
        {
            // metodo quando clica no botão confirmar
            var aluno = new Aluno();

            aluno.Nome = textoNome.Text;
            aluno.Email = textBox2.Text;
            aluno.Codigo = textBox3.Text;
            aluno.DataNascimento = dateTimePicker1.Value;

            var sucesso = Service.Criar(aluno, out var erros);
            if (!sucesso)
            {
                foreach (var erro in erros)
                {
                    MessageBox.Show($"{erro.MemberNames.First()}: {erro.ErrorMessage}");
                }
                MessageBox.Show("Erro ao cadastrar aluno!!");
            }
            else
            {
                MessageBox.Show("Aluno cadastrado!");
                Close();
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }
    }
}
