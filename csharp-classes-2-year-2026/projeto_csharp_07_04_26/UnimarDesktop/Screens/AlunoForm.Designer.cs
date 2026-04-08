namespace UnimarDesktop.Screens
{
    partial class AlunoForm
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
            components = new System.ComponentModel.Container();
            primaryButton1 = new UnimarDesktop.Componentes.PrimaryButton(components);
            textoNome = new TextBox();
            textBox2 = new TextBox();
            textBox3 = new TextBox();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            dateTimePicker1 = new DateTimePicker();
            SuspendLayout();
            // 
            // primaryButton1
            // 
            primaryButton1.BackColor = Color.Blue;
            primaryButton1.FlatAppearance.BorderColor = Color.FromArgb(192, 192, 255);
            primaryButton1.FlatAppearance.BorderSize = 0;
            primaryButton1.FlatStyle = FlatStyle.Flat;
            primaryButton1.Font = new Font("SansSerif", 12F);
            primaryButton1.ForeColor = Color.White;
            primaryButton1.Location = new Point(327, 362);
            primaryButton1.Name = "primaryButton1";
            primaryButton1.Size = new Size(90, 50);
            primaryButton1.TabIndex = 0;
            primaryButton1.Text = "Confirmar";
            primaryButton1.UseVisualStyleBackColor = false;
            primaryButton1.Click += primaryButton1_Click;
            // 
            // textoNome
            // 
            textoNome.Location = new Point(57, 42);
            textoNome.Name = "textoNome";
            textoNome.Size = new Size(360, 23);
            textoNome.TabIndex = 1;
            // 
            // textBox2
            // 
            textBox2.Location = new Point(57, 182);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(360, 23);
            textBox2.TabIndex = 3;
            // 
            // textBox3
            // 
            textBox3.Location = new Point(57, 112);
            textBox3.Name = "textBox3";
            textBox3.Size = new Size(360, 23);
            textBox3.TabIndex = 2;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(57, 22);
            label1.Name = "label1";
            label1.Size = new Size(90, 15);
            label1.TabIndex = 4;
            label1.Text = "Nome do aluno";
            label1.Click += label1_Click;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(57, 94);
            label2.Name = "label2";
            label2.Size = new Size(96, 15);
            label2.TabIndex = 5;
            label2.Text = "Codigo do aluno";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(57, 164);
            label3.Name = "label3";
            label3.Size = new Size(41, 15);
            label3.TabIndex = 6;
            label3.Text = "E-mail";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(57, 234);
            label4.Name = "label4";
            label4.Size = new Size(114, 15);
            label4.TabIndex = 7;
            label4.Text = "Data de Nascimento";
            // 
            // dateTimePicker1
            // 
            dateTimePicker1.Format = DateTimePickerFormat.Short;
            dateTimePicker1.Location = new Point(57, 252);
            dateTimePicker1.Name = "dateTimePicker1";
            dateTimePicker1.Size = new Size(360, 23);
            dateTimePicker1.TabIndex = 8;
            dateTimePicker1.ValueChanged += dateTimePicker1_ValueChanged;
            // 
            // AlunoForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(492, 450);
            Controls.Add(dateTimePicker1);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(textBox3);
            Controls.Add(textBox2);
            Controls.Add(textoNome);
            Controls.Add(primaryButton1);
            Name = "AlunoForm";
            Text = "AlunoForm";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Componentes.PrimaryButton primaryButton1;
        private TextBox textoNome;
        private TextBox textBox2;
        private TextBox textBox3;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private DateTimePicker dateTimePicker1;
    }
}