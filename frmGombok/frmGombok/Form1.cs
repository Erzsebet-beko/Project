using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace frmGombok
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void elemFelrak(int dbx, int dby)
        {
            int x0 = 10;
            int y0 = 60;
            int meretx = 40;
            int merety = 30;
            int dx = 10;
            int dy = 10;
            Button tempgomb;

            for (int i = 1; i <= dbx; i++)
            {
                for (int j = 1; j <=dby; j++)
                {
                    tempgomb = new Button();
                    tempgomb.Name = "Gomb" + i + "_" + j;
                    tempgomb.Text = "("+ i + "," + j +")";
                    tempgomb.Size = new Size(meretx, merety);
                    tempgomb.Left = x0 + (j - 1) * (meretx+dx);
                    tempgomb.Top= y0 + (i - 1) * (merety+dy);
                    tempgomb.FlatStyle = FlatStyle.Flat;
                    tempgomb.BackColor = szinGeneral();
                    this.Controls.Add(tempgomb);

                }
            }
        }
        private Color szinGeneral()
        {
            Color szin;
            szin = Color.FromArgb(vel.Next(256), vel.Next(256), vel.Next(256));
            return szin;
        }
        private void btnFelrak_Click(object sender, EventArgs e)
        {
            elemFelrak(10, 8);
        }

        Random vel = new Random();
    }
}
