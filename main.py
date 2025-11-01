import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import ttk
from tkinter import StringVar

def calculate():
    try:
        cyl = float(cyl_var.get().replace(',', '.'))
        prix = float(prix_var.get().replace(',', '.'))
    except ValueError:
        result_var.set("Entrées invalides")
        return
    if cyl < 1.8:
        douane = prix * 0.15
    else:
        douane = prix * 0.3

    tic = prix * 0.3
    tva = (prix + douane + tic) * 0.19

    tva *= 130
    tic *= 130
    douane *= 130
    dedouanement = (tva + tic + douane) * 0.5
    prix_yri = prix * 230
    total = prix_yri + dedouanement

    result_var.set(f"Total à payer avec dédouanement: {total:,.2f} DA")
    prix_Dedouanement.set(f"Montant dédouanement : {dedouanement:,.2f} DA")

root = tb.Window(themename="flatly", title="Calculateur Avec Dedouanement", size=(460,200))

main = ttk.Frame(root, padding=12)
main.pack(fill='both', expand=True)

ttk.Label(main, text="Cylindre (L) :").grid(row=0, column=0, sticky='w', pady=6, padx=(0,8))
cyl_var = StringVar(value="1.6")
ttk.Entry(main, textvariable=cyl_var, width=20).grid(row=0, column=1, pady=6)

ttk.Label(main, text="Prix voiture (transport inclus) :").grid(row=1, column=0, sticky='w', pady=6, padx=(0,8))
prix_var = StringVar(value="1000")
ttk.Entry(main, textvariable=prix_var, width=20).grid(row=1, column=1, pady=6)

tb.Button(main, text="Calculer", bootstyle="primary", command=calculate).grid(row=2, column=0, columnspan=2, sticky='ew', pady=10)

result_var = StringVar()
prix_Dedouanement = StringVar()  
ttk.Label(main, textvariable=result_var, font=('Segoe UI', 11, 'bold')).grid(row=3, column=0, columnspan=2)
ttk.Label(main, textvariable=prix_Dedouanement, font=('Segoe UI', 11, 'bold')).grid(row=4, column=0, columnspan=2)

root.bind("<Return>", lambda e: calculate())
root.mainloop()
