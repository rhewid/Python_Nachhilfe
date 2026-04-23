# Lösungen zu Prüfung Kapitel 1: Grundlagen - Neu

# Frage 1: Was gibt dieser Code aus?
# alter = 15
# print("Ich bin " + str(alter) + " Jahre alt.")
# Antwort: Ich bin 15 Jahre alt.

# Schritt: Variable alter wird gesetzt, str() wandelt in String um, print gibt aus.

# Frage 2: Schreibe Code, um eine Farbe einzulesen und "Deine Lieblingsfarbe ist [Farbe]." auszugeben.
# Schritt 1: input() für Farbe.
farbe = input("Gib deine Lieblingsfarbe ein: ")
# Schritt 2: print mit Variable.
print("Deine Lieblingsfarbe ist " + farbe + ".")

# Frage 3: Berechne das Doppelte einer eingelesenen Zahl.
# Schritt 1: input() und int().
zahl = int(input("Gib eine Zahl ein: "))
# Schritt 2: Berechne doppelt.
doppelt = zahl * 2
# Schritt 3: print.
print("Das Doppelte ist:", doppelt)

# Frage 4: Gib deinen Namen und dein Alter in einem Satz aus, ohne input.
# Schritt 1: Variablen definieren.
name = "Max"
alter = 20
# Schritt 2: print mit str().
print("Ich heiße " + name + " und bin " + str(alter) + " Jahre alt.")