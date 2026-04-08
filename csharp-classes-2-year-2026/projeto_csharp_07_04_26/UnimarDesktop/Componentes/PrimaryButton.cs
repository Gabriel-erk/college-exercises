using System.ComponentModel;

namespace UnimarDesktop.Componentes
{
    public partial class PrimaryButton : Button
    {
        public override Color BackColor { get => Color.Blue; }
        public override Color ForeColor { get => Color.White; }
        public PrimaryButton()
        {
            InitializeComponent();
        }

        public PrimaryButton(IContainer container)
        {
            container.Add(this);

            InitializeComponent();
        }
    }
}
