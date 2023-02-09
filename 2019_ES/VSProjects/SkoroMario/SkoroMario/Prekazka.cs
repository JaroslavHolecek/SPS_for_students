using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Shapes;
using System.Drawing;

namespace SkoroMario
{
    class Prekazka
    {
        public Shape obrazek { get; private set; }
        public Point point { get; private set; }

        public Prekazka(int velikost, int pozice_x, int pozice_y)
        {
            obrazek = new System.Windows.Shapes.Ellipse();
            obrazek.Height = velikost;
            obrazek.Width = velikost;
            point = new Point(pozice_x, pozice_y);
            obrazek.Fill = System.Windows.Media.Brushes.Orange;
        }
    }
}
