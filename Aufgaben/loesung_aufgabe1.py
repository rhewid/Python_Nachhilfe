
## Lösungen zu Aufgabe 1: Grundlagen

# Aufgabe 1: Hallo Welt
# Schritt 1: Verwende die print-Funktion, um Text auszugeben.
print("Hallo Welt")

# Erweiterung: Eingabe des Namens
# Schritt 1: Verwende input(), um den Namen einzulesen.
# Schritt 2: Speichere in einer Variablen.
# Schritt 3: Gib eine Begrüßung aus.
name = input("Wie heißt du? ")
print("Hallo, " + name + "!")

# Aufgabe 2: Variablen
# Schritt 1: Definiere Variablen.
alter = 25
name = "Max"
stadt = "Berlin"
# Schritt 2: Gib sie in einem Satz aus.
print("Ich heiße " + name + ", bin " + str(alter) + " Jahre alt und wohne in " + stadt + ".")

# Aufgabe 3: Einfache Berechnung
# Schritt 1: Lies Alter ein.
alter = int(input("Gib dein Alter ein: "))
# Schritt 2: Berechne Tage (vereinfacht).
tage = alter * 365
# Schritt 3: Gib aus.
print("Du bist ungefähr " + str(tage) + " Tage alt.")