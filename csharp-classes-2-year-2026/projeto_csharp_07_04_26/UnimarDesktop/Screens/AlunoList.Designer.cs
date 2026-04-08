namespace UnimarDesktop.Screens
{
    partial class AlunoList
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            gridAlunos = new DataGridView();
            Codigo = new DataGridViewTextBoxColumn();
            Nome = new DataGridViewTextBoxColumn();
            DataNascimento = new DataGridViewTextBoxColumn();
            Email = new DataGridViewTextBoxColumn();
            label1 = new Label();
            panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)gridAlunos).BeginInit();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.Controls.Add(gridAlunos);
            panel1.Location = new Point(12, 152);
            panel1.Name = "panel1";
            panel1.Size = new Size(643, 266);
            panel1.TabIndex = 0;
            // 
            // gridAlunos
            // 
            gridAlunos.AllowUserToAddRows = false;
            gridAlunos.AllowUserToDeleteRows = false;
            gridAlunos.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            gridAlunos.Columns.AddRange(new DataGridViewColumn[] { Codigo, Nome, DataNascimento, Email });
            gridAlunos.Dock = DockStyle.Fill;
            gridAlunos.Enabled = false;
            gridAlunos.Location = new Point(0, 0);
            gridAlunos.Name = "gridAlunos";
            gridAlunos.ReadOnly = true;
            gridAlunos.RowHeadersVisible = false;
            gridAlunos.Size = new Size(643, 266);
            gridAlunos.TabIndex = 0;
            gridAlunos.CellContentClick += dataGridView1_CellContentClick;
            // 
            // Codigo
            // 
            Codigo.HeaderText = "Codigo";
            Codigo.Name = "Codigo";
            Codigo.ReadOnly = true;
            // 
            // Nome
            // 
            Nome.HeaderText = "Nome";
            Nome.Name = "Nome";
            Nome.ReadOnly = true;
            Nome.Width = 200;
            // 
            // DataNascimento
            // 
            DataNascimento.HeaderText = "Data de Nascimento";
            DataNascimento.Name = "DataNascimento";
            DataNascimento.ReadOnly = true;
            DataNascimento.Width = 200;
            // 
            // Email
            // 
            Email.AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill;
            Email.HeaderText = "Email";
            Email.Name = "Email";
            Email.ReadOnly = true;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Calibri", 36F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label1.Location = new Point(192, 26);
            label1.Name = "label1";
            label1.Size = new Size(316, 59);
            label1.TabIndex = 1;
            label1.Text = "Lista de Alunos";
            // 
            // AlunoList
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(684, 450);
            Controls.Add(label1);
            Controls.Add(panel1);
            Name = "AlunoList";
            Text = "AlunoList";
            panel1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)gridAlunos).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Panel panel1;
        private DataGridView gridAlunos;
        private Label label1;
        private DataGridViewTextBoxColumn Codigo;
        private DataGridViewTextBoxColumn Nome;
        private DataGridViewTextBoxColumn DataNascimento;
        private DataGridViewTextBoxColumn Email;
    }
}