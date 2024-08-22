print("Scegli la figura per calcolo perimetro:")
print("1- Quadrato", "\n2- Trapezio", "\n3- Triangolo Rettangolo")

scelta = input("Inserisci un numero (1-3) per scegliere la figura: ")
while scelta not in ("1", "2", "3"):
    print("Scelta non valida. Seleziona un numero tra 1 e 3.")
    scelta = input("Inserisci il numero della figura scelta (1-3): ")

if scelta == "1":
    lato = int(input("Inserisci la lunghezza del lato del quadrato: "))
    perimetro_quadrato = lato * 4
    print(f"Il perimetro del quadrato e': {perimetro_quadrato}")

elif scelta == "2":
    base_maggiore = int(input("Inserisci base maggiore: "))
    base_minore = int(input("Inserisci base minore: "))
    lato_obliquo1 = int(input("Inserisci lato obliquo 1: "))
    lato_obliquo2 = int(input("Inserisci lato obliquo 2: "))
    perimetro_trapezio = base_maggiore + base_minore + lato_obliquo1 + lato_obliquo2
    print(f"Il perimetro del trapezio e': {perimetro_trapezio}")

elif scelta == "3":
    valore_valido = False

    while not valore_valido:
        ipotenusa = int(input("Inserisci l'ipotenusa: "))
        cateto_maggiore = int(input("Inserisci il cateto maggiore: "))
        cateto_minore = int(input("Inserisci il cateto minore: "))
        if cateto_minore < cateto_maggiore:
            valore_valido = True
        else:
            print("E no! Ti ho pure scritto che questo è il cateto minore! Riprova!")
    perimetro_triangolo_rettangolo = ipotenusa + cateto_maggiore + cateto_minore
    print(f"Il perimetro del triangolo rettangolo è: {perimetro_triangolo_rettangolo}")

