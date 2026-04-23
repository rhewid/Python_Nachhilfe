# Lösungen zu Prüfung Kapitel 2: Schleifen

# Frage 1: Gib mit einer for-Schleife die Buchstaben eines Wortes aus.
# Schritt 1: Definiere Wort.
wort = "Python"
# Schritt 2: Schleife über jedes Zeichen.
for buchstabe in wort:
    print(buchstabe)

# Frage 2: Verwende eine while-Schleife, um von 5 bis 1 zu zählen.
# Schritt 1: Setze Startwert.
i = 5
# Schritt 2: Schleife solange i > 0.
while i > 0:
    print(i)
    i -= 1

# Frage 3: Berechne das Produkt der Zahlen von 1 bis 5 mit einer Schleife.
# Schritt 1: Initialisiere produkt = 1.
produkt = 1
# Schritt 2: Schleife von 1 bis 5, multipliziere.
for i in range(1, 6):
    produkt *= i
print("Produkt:", produkt)

# Frage 4: Gib alle Elemente einer Liste aus, außer dem letzten.
# Schritt 1: Definiere Liste.
liste = [1, 2, 3, 4, 5]
# Schritt 2: Schleife über alle außer dem letzten (len-1).
for i in range(len(liste) - 1):
    print(liste[i])