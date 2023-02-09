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
    class Hrac
    {
        public Shape obrazek { get; private set; }
        public Point pozice_hrace { get; private set; }
        public Point point_predchozi { get; private set; }
        public int rychlost;
        public int body;

        public Hrac()
        {
            obrazek = new System.Windows.Shapes.Rectangle();
            obrazek.Height = 50;
            obrazek.Width = 100;
            pozice_hrace = new Point(150, 200);
            obrazek.Fill = System.Windows.Media.Brushes.Green;

            rychlost = 10;
            body = 100;
            
        }

        public void nastavPozici(Canvas plocha, Point p)
        {
            //0  plocha.Width - obrazek.Width
            //0  plocha.Height - obrazek.Height
            if (p.X < 0)
            {
                p.X = 0;
            }
            else if (p.X > plocha.Width - obrazek.Width)
            {
                p.X = (int)(plocha.Width - obrazek.Width);
            }
            p.Y = (int)(plocha.Height - obrazek.Height);

            pozice_hrace = p;
        }

        public void pohyb(Canvas plocha)
        {
            point_predchozi = pozice_hrace;

            if (Keyboard.IsKeyDown(Key.A))
            {
                nastavPozici(plocha, new Point(pozice_hrace.X - rychlost, pozice_hrace.Y));
            }
            if (Keyboard.IsKeyDown(Key.D))
            {
                nastavPozici(plocha, new Point(pozice_hrace.X + rychlost, pozice_hrace.Y));
            }
            


            /* if (Keyboard.IsKeyDown(Key.S))
             {
                 nastavPozici(plocha, new Point(point.X, point.Y + rychlost));
             }  */
        }
    }
}
