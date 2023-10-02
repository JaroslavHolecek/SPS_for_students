using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Threading;
using System.Drawing;
using System.Threading.Tasks;
using System.Windows.Controls;
using System.Windows.Input;

namespace SpaceInvader
{
    class Hra
    {
        private int Max_pocet_strel;
        private DispatcherTimer hlavniTimer;
        private Canvas platno;
        public Hrac hrac;
        public List<Strela> strely = new List<Strela>();
        public List<Invader> seznam_invader = new List<Invader>();
        MainWindow mw;

        public int GRAVITACE;

        public Hra(SpaceInvader.MainWindow w)
        {
            mw = w;
            platno = mw.platno;
            platno.Background = System.Windows.Media.Brushes.LightBlue;
            hrac = new Hrac(platno);

            Max_pocet_strel = 10;

            /*Random rnd = new Random();
            rnd.Next();
            */

            platno.Children.Add(hrac.obrazek);
            pridejinvadery(5);

            InitializeHlavniTimer();

        }

        public bool kolize_strely_invader(Invader invader, Strela strela) {
            double invader_x = invader.pozice_Inv.X;
            double invader_konec_x = invader.pozice_Inv.X + invader.obrazek.Width;

            double invader_y = invader.pozice_Inv.Y;
            double invader_konec_y = invader.pozice_Inv.Y + invader.obrazek.Height;

            double strela_x = strela.pozice_Strely.X;
            double strela_konec_x = strela.pozice_Strely.X + strela.obrazek.Width;

            double strela_y = strela.pozice_Strely.Y;
            double strela_konec_y = strela.pozice_Strely.Y + strela.obrazek.Height;

            if (((strela_x > invader_x && strela_x < invader_konec_x) || (strela_konec_x > invader_x && strela_konec_x < invader_konec_x))
                && ((strela_y > invader_y && strela_y < invader_konec_y) || (strela_konec_y > invader_y && strela_konec_y < invader_konec_y)))
            {
                return true;
            }
            return false;
        }

        public void pridejinvadery(int pocet)
        {
            for (int i = 0; i < pocet; i++)
            {
                pridejinvadera(new Point(60*i ,30 ));
            } 
        }


        private void InitializeHlavniTimer()
        {
            this.hlavniTimer = new DispatcherTimer(DispatcherPriority.Normal); // For lagging Fix is used priority
            this.hlavniTimer.Interval = TimeSpan.FromMilliseconds(10);
            this.hlavniTimer.Tick += hlavniAkce;

            this.hlavniTimer.Start();
        }

        public void smaz_invadera(Invader i)
        {
            seznam_invader.Remove(i);
            platno.Children.Remove(i.obrazek);
        }

        public void smaz_strelu(Strela j)
        {
            strely.Remove(j);
            platno.Children.Remove(j.obrazek);
        }
        public void pridejstrelu()
        {
            if (Keyboard.IsKeyDown(Key.R))
            {
                if (strely.Count < Max_pocet_strel)
                {
                    Point pozice = hrac.pozice_hrace;
                    pozice.X += (int)Math.Ceiling(hrac.obrazek.ActualWidth / 2 - 5); /*-5 nahradit polovinou velikosti střely*/
                    strely.Add(new Strela(pozice));
                    platno.Children.Add(strely[strely.Count - 1].obrazek);
                }
            }
        }

        public void pridejinvadera(Point p)
        {
            seznam_invader.Add(new Invader(p)); /* TODO: invadery přidávat na náhodné pozice  */
            platno.Children.Add(seznam_invader[seznam_invader.Count - 1].obrazek);
        }

        private void hlavniAkce(object sender, EventArgs e)
        {
            /* =========================== */
            /* ==== zpracování vstupu ==== */
            /* =========================== */
            hrac.pohyb(platno);
            pridejstrelu();

            /* ======================== */
            /* ==== výpočty ve hře ==== */
            /* ======================== */
            foreach (Invader i in seznam_invader)
            {
                i.pohyb(platno);
            }
                bool break_strely = false;
            foreach (Strela s in strely)
            {
                s.pohyb(platno);
                if (s.pozice_Strely.Y < 0)
                {
                    smaz_strelu(s);
                    break;
                }

                break_strely = false;
                foreach (Invader i in seznam_invader)
                {
                    if (kolize_strely_invader(i,s))
                    {
                        smaz_strelu(s);
                        smaz_invadera(i);
                        break_strely = true;
                        break;
                    }
                }
                if (break_strely)
                {
                    break;
                }
            }

           
            /* ==================== */
            /* ==== Vykresleni ==== */
            /* ==================== */

            /* Hrac */
            Canvas.SetTop(hrac.obrazek, hrac.pozice_hrace.Y);
            Canvas.SetLeft(hrac.obrazek, hrac.pozice_hrace.X);
            mw.lbl_body_hrace.Content = this.hrac.body.ToString();

            foreach (Strela strela in strely)
            {
                Canvas.SetTop(strela.obrazek, strela.pozice_Strely.Y);
                Canvas.SetLeft(strela.obrazek, strela.pozice_Strely.X);
            }

            foreach (Invader invader in seznam_invader)
            {
                Canvas.SetTop(invader.obrazek, invader.pozice_Inv.Y);
                Canvas.SetLeft(invader.obrazek, invader.pozice_Inv.X);
            }

            /* Nepritel */
            /*foreach (Nepritel nepritel in vsichni_nepratele)
            {
                Canvas.SetTop(nepritel.obrazek, nepritel.point.Y);
                Canvas.SetLeft(nepritel.obrazek, nepritel.point.X);
            }*/


            /* Zetony */
            /*foreach (Zeton zeton in vsechny_zetony)
            {
                Canvas.SetTop(zeton.obrazek, zeton.point.Y);
                Canvas.SetLeft(zeton.obrazek, zeton.point.X);
            }*/

            /* Prekazky */
            /*foreach (Prekazka p in vsechny_prekazky)
            {
                Canvas.SetTop(p.obrazek, p.point.Y);
                Canvas.SetLeft(p.obrazek, p.point.X);
            }*/
        }
    }
}
