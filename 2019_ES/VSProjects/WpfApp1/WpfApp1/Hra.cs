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
        private DispatcherTimer hlavniTimer;
        private Canvas platno;
        public Hrac hrac;
        public List<Strela> strely = new List<Strela>();
        public List<Invader> seznam_invader = new List<Invader>();
    
        /*public Zeton z1;
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
            seznam_invader.Add(new Invader(new Point(25, 20)));

          
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
            /* TODO: přidat obrázky Invaderů do plátna */

            /*foreach (Nepritel nepritel in vsichni_nepratele)
            {
                platno.Children.Add(nepritel.obrazek);
            }


            foreach (Prekazka p in vsechny_prekazky)
            {
                platno.Children.Add(p.obrazek);
            }
            */

            InitializeHlavniTimer();
            
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
        public void pridejstrelu()
        {
            if (Keyboard.IsKeyDown(Key.R))
            {
            
                Point pozice = hrac.pozice_hrace;
                pozice.X += (int)Math.Ceiling (hrac.obrazek.ActualWidth / 2 - 5); /*-5 nahradit polovinou velikosti střely*/
                strely.Add(new Strela(pozice));
                platno.Children.Add(strely[strely.Count-1].obrazek);
                
            }
           
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
            foreach (Strela s in strely)
            {
                s.pohyb(platno);

            }
            
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
