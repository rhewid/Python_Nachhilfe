## Lösungen zu Aufgabe 4: Gemischt

# Aufgabe 1: Kombination
# Schritt 1: Definiere Liste.
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Schritt 2: Schleife über Liste.
for zahl in zahlen:
    # Schritt 3: Prüfe Bedingungen.
    if zahl > 5 and zahl % 2 == 0:
        print(zahl)

# Aufgabe 2: Schleife mit Bedingung
# Schritt 1: Lies Wort ein.
wort = input("Gib ein Wort ein: ")
# Schritt 2: Initialisiere Zähler.
vokale = 0
# Schritt 3: Schleife über Buchstaben.
for buchstabe in wort.lower():
    if buchstabe in "aeiou":
        vokale += 1
# Schritt 4: Gib aus.
print("Anzahl Vokale:", vokale)