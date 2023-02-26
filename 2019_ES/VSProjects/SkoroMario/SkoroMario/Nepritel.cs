using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Shapes;
using System.Drawing;
using System.Windows.Controls;
using System.Windows.Input;

namespace SkoroMario
{
    class Nepritel
    {
        public Shape obrazek { get; private set; }
        public Point point { get; private set; }
        public int rychlost, max_leva, max_prava;
        public bool doleva;

        public Nepritel(int rozsah, int pozice_x, int pozice_y)
        {
            obrazek = new System.Windows.Shapes.Ellipse();
            obrazek.Height = 50;
            obrazek.Width = 50;
            point = new Point(pozice_x, pozice_y);
            obrazek.Fill = System.Windows.Media.Brushes.Red;
            doleva = true;
            max_leva = pozice_x - rozsah;
            max_prava = pozice_x + rozsah;

            rychlost = 5;
        }

        public void pohyb()
        {
            if (doleva)
            {
                if (point.X > max_leva)
                {
                    point = new Point(point.X - rychlost, point.Y);
                }
                else
                {
                    doleva = false;
                }
            }
            else /* doprava */
            {
                if (point.X < max_prava)
                {
                    point = new Point(point.X + rychlost, point.Y);
                }
                else
                {
                    doleva = true;
                }
            }

        }
    }
}
