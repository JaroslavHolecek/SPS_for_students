using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Shapes;
using System.Drawing;
using System.Windows.Controls;
using System.Windows.Input;

namespace SpaceInvader
{
    class Invader
    {
        public Shape obrazek { get; private set; }
        public Point pozice_Inv { get; private set; }
        public int rychlost;
        public bool doleva;
        public int kroky;
        public int rozptyl;

        public Invader(Point p)
        {
            obrazek = new System.Windows.Shapes.Rectangle();
            obrazek.Height = 30;
            obrazek.Width = 30;
            pozice_Inv = p;
            obrazek.Fill = System.Windows.Media.Brushes.Blue;

            rychlost = 1;
            doleva = true;
            kroky = 0;
            rozptyl = 10;
        }
        public void nastavPozici(Canvas plocha, Point p)
        {
            //0  plocha.Width - obrazek.Width
            //0  plocha.Height - obrazek.Height

            pozice_Inv = p;
        }
        public void pohyb(Canvas plocha)
        {
            int zmena;
            if (doleva)
            {
                zmena = -rychlost;           
            }
            else
            {
                zmena = rychlost;
            }           
            nastavPozici(plocha, new Point(pozice_Inv.X + zmena, pozice_Inv.Y + rychlost));
            kroky += 1;
            
            if (kroky >= 10)
            {
                doleva = !doleva;
                kroky = 0;
            }
        }
    }

}
