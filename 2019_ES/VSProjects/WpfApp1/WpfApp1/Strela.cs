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
    class Strela
    {
        public Shape obrazek { get; private set; }
        public Point pozice_Strely { get; private set; }
        public int rychlost;

        public Strela(Point p)
        {
            obrazek = new System.Windows.Shapes.Rectangle();
            obrazek.Height = 10;
            obrazek.Width = 10;
            pozice_Strely = p;
            obrazek.Fill = System.Windows.Media.Brushes.Red;

            rychlost = 1;

        }
        public void nastavPozici(Canvas plocha, Point p)
        {
            //0  plocha.Width - obrazek.Width
            //0  plocha.Height - obrazek.Height
            
            pozice_Strely = p;
        }
        public void pohyb(Canvas plocha)
        {
            nastavPozici(plocha, new Point(pozice_Strely.X, pozice_Strely.Y -rychlost));       
        }
    }
    
}
