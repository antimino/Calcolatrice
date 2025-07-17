import customtkinter as ctk

ctk.set_appearance_mode("Light")  # o "Dark"
ctk.set_default_color_theme("blue")

# Finestra principale
app = ctk.CTk()
app.title("Calcolatrice")
app.geometry("320x400")
app.resizable(False, False)

# Display
display = ctk.CTkEntry(
    app,
    width=280,
    height=50,
    font=("Arial", 20),
    justify="right"
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=(10, 5),
    sticky="ew"  # si espande verso est e ovest (orizzontale)
)

# Funzioni
def clicca(tasto):
    display.insert(ctk.END, tasto)

def calcola():
    try:
        risultato = eval(display.get())
        display.delete(0, ctk.END)
        display.insert(0, str(risultato))
    except:
        display.delete(0, ctk.END)
        display.insert(0, "Errore")

def cancella():
    display.delete(0, ctk.END)

def backspace():
    current = display.get()
    display.delete(0, ctk.END)
    display.insert(0, current[:-1])

# Funzione per gestire la tastiera
def gestisci_tasti(event):
    tasto = event.keysym
    if tasto in "0123456789":
        clicca(tasto)
    elif tasto in ["plus", "KP_Add"]:
        clicca("+")
    elif tasto in ["minus", "KP_Subtract"]:
        clicca("-")
    elif tasto in ["asterisk", "KP_Multiply"]:
        clicca("*")
    elif tasto in ["slash", "KP_Divide"]:
        clicca("/")
    elif tasto == "Return":
        calcola()
    elif tasto == "Escape":
        cancella()
    elif tasto == "BackSpace":
        backspace()
    elif tasto == "period" or tasto == "comma":
        clicca(".")

# Associazione eventi tastiera
app.bind("<Key>", gestisci_tasti)

# Pulsanti
pulsanti = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for testo, riga, colonna in pulsanti:
    width = 67 if testo != 'C' else 281
    btn = ctk.CTkButton(
        master=app,
        text=testo,
        width=width,
        height=50,
        corner_radius=20,
        font=("Arial", 16),
        fg_color="#FFA500" if testo in ['+', '-', '*', '/', '='] else None,
        hover_color="#FFB84D" if testo in ['+', '-', '*', '/', '='] else None,
        command=calcola if testo == '=' else (cancella if testo == 'C' else lambda t=testo: clicca(t))
    )
    if testo == 'C':
        btn.grid(row=riga, column=colonna, columnspan=4, padx=5, pady=5)
    else:
        btn.grid(row=riga, column=colonna, padx=5, pady=5)

app.mainloop()
