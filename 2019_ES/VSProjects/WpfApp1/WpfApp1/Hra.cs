using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Threading;
using System.Drawing;

using System.Threading.Tasks;
using System.Windows.Controls;

namespace SpaceInvader
{
    class Hra
    {
        private DispatcherTimer hlavniTimer;
        private Canvas platno;
        public Hrac hrac;
        /*public List<Nepritel> vsichni_nepratele = new List<Nepritel>(); 
        public Zeton z1;
        public List<Zeton> vsechny_zetony = new List<Zeton>();
        public List<Prekazka> vsechny_prekazky = new List<Prekazka>();*/
        MainWindow mw;

        public int GRAVITACE;

        public Hra(SpaceInvader.MainWindow w)
        {
            mw = w;
            platno = mw.platno;
            platno.Background = System.Windows.Media.Brushes.LightBlue;
            hrac = new Hrac(platno);

            /*Random rnd = new Random();
            rnd.Next();
            for (int i = 1; i < 11; i++)
            {
                vsichni_nepratele.Add(new Nepritel(8, 5 * i, 15 * i));
            }

            for (int i = 1; i < 11; i++)
            {

                pridej_zeton(new Zeton(i, 10 * i, 20 * i));
            }

            for (int i = 1; i < 11; i++)
            {
                vsechny_prekazky.Add(new Prekazka(50, 100 * i, 50 * i));
            }

            GRAVITACE = 2;*/

            platno.Children.Add(hrac.obrazek);

            /*foreach (Nepritel nepritel in vsichni_nepratele)
            {
                platno.Children.Add(nepritel.obrazek);
            }


            foreach (Prekazka p in vsechny_prekazky)
            {
                platno.Children.Add(p.obrazek);
            }


            InitializeHlavniTimer();
            */
        }

        /*public bool naraz_hrace_do_nepritele(Hrac h, Nepritel n)
        {
            int polomer_hrace = (int)Math.Ceiling(h.obrazek.Width / 2);
            int polomer_nepritele = (int)Math.Ceiling(n.obrazek.Width / 2);

            Point stred_hrace = new Point(h.point.X + polomer_hrace, h.point.Y + polomer_hrace);
            Point stred_nepritele = new Point(n.point.X + polomer_nepritele, n.point.Y + polomer_nepritele);

            if ((stred_hrace.X - stred_nepritele.X) * (stred_hrace.X - stred_nepritele.X)
                + (stred_hrace.Y - stred_nepritele.Y) * (stred_hrace.Y - stred_nepritele.Y)

                < (polomer_hrace + polomer_nepritele) * (polomer_hrace + polomer_nepritele)
                )
            {
                return true;

            }
            return false;
        }


        public bool naraz_hrace_do_prekazky(Hrac h, Prekazka n)
        {
            int polomer_hrace = (int)Math.Ceiling(h.obrazek.Width / 2);
            int polomer_prekazky = (int)Math.Ceiling(n.obrazek.Width / 2);

            Point stred_hrace = new Point(h.point.X + polomer_hrace, h.point.Y + polomer_hrace);
            Point stred_prekazky = new Point(n.point.X + polomer_prekazky, n.point.Y + polomer_prekazky);

            if ((stred_hrace.X - stred_prekazky.X) * (stred_hrace.X - stred_prekazky.X)
                + (stred_hrace.Y - stred_prekazky.Y) * (stred_hrace.Y - stred_prekazky.Y)

                < (polomer_hrace + polomer_prekazky) * (polomer_hrace + polomer_prekazky)
                )
            {
                return true;
            }
            return false;
        }

        public bool naraz_hrace_do_zetonu(Hrac h, Zeton z)
        {
            int polomer_hrace = (int)Math.Ceiling(h.obrazek.Width / 2);
            int polomer_prekazky = (int)Math.Ceiling(z.obrazek.Width / 2);

            Point stred_hrace = new Point(h.point.X + polomer_hrace, h.point.Y + polomer_hrace);
            Point stred_prekazky = new Point(z.point.X + polomer_prekazky, z.point.Y + polomer_prekazky);

            if ((stred_hrace.X - stred_prekazky.X) * (stred_hrace.X - stred_prekazky.X)
                + (stred_hrace.Y - stred_prekazky.Y) * (stred_hrace.Y - stred_prekazky.Y)

                < (polomer_hrace + polomer_prekazky) * (polomer_hrace + polomer_prekazky)
                )
            {
                return true;
            }
            return false;
        }
        */
        private void InitializeHlavniTimer()
        {
            this.hlavniTimer = new DispatcherTimer(DispatcherPriority.Normal); // For lagging Fix is used priority
            this.hlavniTimer.Interval = TimeSpan.FromMilliseconds(10);
            this.hlavniTimer.Tick += hlavniAkce;

            this.hlavniTimer.Start();
        }
        /*
        public void smaz_zeton(Zeton z)
        {
            vsechny_zetony.Remove(z);
            platno.Children.Remove(z.obrazek);
        }

        public void pridej_zeton(Zeton z)
        {
            vsechny_zetony.Add(z);
            platno.Children.Add(z.obrazek);
        }
        */
        private void hlavniAkce(object sender, EventArgs e)
        {
            /* =========================== */
            /* ==== zpracování vstupu ==== */
            /* =========================== */
            hrac.pohyb(platno);

            /* ======================== */
            /* ==== výpočty ve hře ==== */
            /* ======================== */

            /* pohyb nepratel */
            /*foreach (Nepritel n in vsichni_nepratele)
            {
                n.pohyb();
            }

            */
            /* gravitace */
            /*hrac.nastavPozici(platno, new Point(hrac.point.X, hrac.point.Y + GRAVITACE));*/
            

           /* foreach (Nepritel n in vsichni_nepratele)
            {
                if (naraz_hrace_do_nepritele(hrac, n))
                {
                    hrac.body -= 1;
                    hrac.nastavPozici(platno, new Point(150, 150));
                }
            }

            foreach (Prekazka p in vsechny_prekazky)
            {
                if (naraz_hrace_do_prekazky(hrac, p))
                {
                    hrac.nastavPozici(platno, hrac.point_predchozi);
                    hrac.stojim_na_zemi = true;
                }
            }


            foreach (Zeton zeton in vsechny_zetony)
            {
                if (naraz_hrace_do_zetonu(hrac, zeton))
                {
                    hrac.body += zeton.hodnota;
                    smaz_zeton(zeton);
                    break;
                }
            }
            */
            /* ==================== */
            /* ==== Vykresleni ==== */
            /* ==================== */

            /* Hrac */
            Canvas.SetTop(hrac.obrazek, hrac.pozice_hrace.Y);
            Canvas.SetLeft(hrac.obrazek, hrac.pozice_hrace.X);
            mw.lbl_body_hrace.Content = this.hrac.body.ToString();
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
