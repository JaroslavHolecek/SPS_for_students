import tkinter as tk

# funkce pro výpočty
def pocet_znaku():
    jmeno = entry.get()
    vysledek.config(text="Počet znaků: " + str(len(jmeno)))

def pocet_samohlasek():
    jmeno = entry.get().lower()
    samohlasky = "aeiouyáéíóúůě"
    pocet = sum(1 for p in jmeno if p in samohlasky)
    vysledek.config(text="Počet samohlásek: " + str(pocet))

def pocet_souhlasek():
    jmeno = entry.get().lower()
    samohlasky = "aeiouyáéíóúůě"
    pocet = sum(1 for p in jmeno if p.isalpha() and p not in samohlasky)
    vysledek.config(text="Počet souhlásek: " + str(pocet))

# vytvoření okna
okno = tk.Tk()
okno.title("Analýza jména")
okno.geometry("300x200")

# vstupní pole
label = tk.Label(okno, text="Zadej jméno:")
label.pack()

entry = tk.Entry(okno)
entry.pack()

print(pocet_znaku)
# tlačítka
btn1 = tk.Button(okno, text="Počet znaků", command=pocet_znaku)
btn1.pack(pady=20)

btn2 = tk.Button(okno, text="Počet samohlásek", command=pocet_samohlasek)
btn2.pack(pady=5)

btn3 = tk.Button(okno, text="Počet souhlásek", command=pocet_souhlasek)
btn3.pack(pady=5)

# výsledek
vysledek = tk.Label(okno, text="")
vysledek.pack(pady=10)

okno.mainloop()