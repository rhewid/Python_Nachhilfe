# Lösungen zu Aufgabe 2: Schleifen

# Aufgabe 1: For-Schleife
# Schritt 1: Verwende range(1,11) für 1 bis 10.
# Schritt 2: Schleife über die Zahlen und gib sie aus.
for i in range(1, 11):
    print(i)

# Aufgabe 2: While-Schleife
# Schritt 1: Setze Startwert 10.
# Schritt 2: Schleife solange >0, gib aus und dekrementiere.
i = 10
while i > 0:
    print(i)
    i -= 1

# Aufgabe 3: Summe berechnen
# Schritt 1: Initialisiere summe = 0.
# Schritt 2: Schleife von 1 bis 100, addiere.
summe = 0
for i in range(1, 101):
    summe += i
print("Summe:", summe)