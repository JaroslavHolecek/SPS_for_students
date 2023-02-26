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
    class Hrac
    {
        public Shape obrazek { get; private set; }
        public Point point { get; private set; }
        public Point point_predchozi { get; private set; }
        public int rychlost;
        public int body;
        public bool stojim_na_zemi;
        public int VYSKA_SKOKU;
        public int skok;

         
        public Hrac()
        {
            obrazek = new System.Windows.Shapes.Ellipse();
            obrazek.Height = 50;
            obrazek.Width = 50;
            point = new Point(150, 200);
            obrazek.Fill = System.Windows.Media.Brushes.Blue;

            rychlost = 10;
            body = 100;
            stojim_na_zemi = true;

            VYSKA_SKOKU = 15;
            skok = 0;
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

            if (p.Y < 0)
            {
                p.Y = 0;
            }
            else if (p.Y > plocha.Height - obrazek.Height)
            {
                p.Y = (int)(plocha.Height - obrazek.Height);
                stojim_na_zemi = true;
            }

            point = p;
        }

        public void pohyb(Canvas plocha)
        {
            point_predchozi = point;

            if (Keyboard.IsKeyDown(Key.A))
            {
                nastavPozici(plocha, new Point(point.X - rychlost, point.Y));
            }
            if (Keyboard.IsKeyDown(Key.D))
            {
                nastavPozici(plocha, new Point(point.X + rychlost, point.Y));
            }
            if (Keyboard.IsKeyDown(Key.W) && stojim_na_zemi)
            {
                stojim_na_zemi = false;
                skok = VYSKA_SKOKU;
            }
              

            /* if (Keyboard.IsKeyDown(Key.S))
             {
                 nastavPozici(plocha, new Point(point.X, point.Y + rychlost));
             }  */
        }
    }
}
