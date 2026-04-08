using UnimarDesktop.Componentes;

namespace UnimarDesktop
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            button1 = new PrimaryButton(components);
            primaryButton1 = new PrimaryButton(components);
            panel1 = new Panel();
            SuspendLayout();
            // 
            // button1
            // 
            button1.FlatAppearance.BorderSize = 0;
            button1.FlatStyle = FlatStyle.Flat;
            button1.Font = new Font("Segoe UI", 16F);
            button1.Location = new Point(3, 3);
            button1.Name = "button1";
            button1.Size = new Size(185, 52);
            button1.TabIndex = 0;
            button1.Text = "Criar Aluno";
            button1.UseVisualStyleBackColor = false;
            button1.Click += onclick_botaoCadastrarAluno;
            // 
            // primaryButton1
            // 
            primaryButton1.FlatAppearance.BorderSize = 0;
            primaryButton1.FlatStyle = FlatStyle.Flat;
            primaryButton1.Font = new Font("Segoe UI", 16F);
            primaryButton1.Location = new Point(3, 61);
            primaryButton1.Name = "primaryButton1";
            primaryButton1.Size = new Size(185, 52);
            primaryButton1.TabIndex = 1;
            primaryButton1.Text = "Listar Aluno";
            primaryButton1.UseVisualStyleBackColor = false;
            primaryButton1.Click += primaryButton1_Click;
            // 
            // panel1
            // 
            panel1.BackColor = Color.DarkGray;
            panel1.Location = new Point(3, 3);
            panel1.Name = "panel1";
            panel1.Size = new Size(185, 445);
            panel1.TabIndex = 1;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(primaryButton1);
            Controls.Add(button1);
            Controls.Add(panel1);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
        }

        #endregion

        private PrimaryButton button1;
        private PrimaryButton primaryButton1;
        private Panel panel1;
    }
}
