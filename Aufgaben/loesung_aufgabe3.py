# Lösungen zu Aufgabe 3: Verzweigungen

# Aufgabe 1: Einfache Verzweigung
# Schritt 1: Lies Alter ein.
alter = int(input("Gib dein Alter ein: "))
# Schritt 2: Prüfe mit if.
if alter >= 18:
    print("Du bist volljährig.")
else:
    print("Du bist nicht volljährig.")

# Aufgabe 2: Mehrere Bedingungen
# Schritt 1: Lies Note ein.
note = int(input("Gib deine Note ein (1-6): "))
# Schritt 2: Verwende if-elif-else.
if note == 1:
    print("Sehr gut")
elif note == 2:
    print("Gut")
elif note == 3:
    print("Befriedigend")
elif note == 4:
    print("Ausreichend")
elif note == 5:
    print("Mangelhaft")
else:
    print("Ungenügend")

# Aufgabe 3: Gerade oder Ungerade
# Schritt 1: Lies Zahl ein.
zahl = int(input("Gib eine Zahl ein: "))
# Schritt 2: Prüfe mit Modulo.
if zahl % 2 == 0:
    print("Gerade")
else:
    print("Ungerade")