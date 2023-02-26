using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Shapes;
using System.Drawing;

namespace SkoroMario
{
    class Zeton
    {
        public Shape obrazek { get; private set; }
        public Point point { get; private set; }
        public int hodnota;


        public Zeton(int zadana_hodnota, int pozice_x, int pozice_y)
        {
            hodnota = zadana_hodnota;
            obrazek = new System.Windows.Shapes.Ellipse();
            obrazek.Height = 2*hodnota;
            obrazek.Width = 2*hodnota;
            point = new Point(pozice_x, pozice_y);
            obrazek.Fill = System.Windows.Media.Brushes.Black;
        }
    }
}
