# Lösungen zu Prüfung Kapitel 1: Grundlagen

# Frage 1: Was wird ausgegeben?
# name = "Anna"
# print("Hallo, " + name)
# Antwort: Hallo, Anna

# Schritt: Die Variable name wird auf "Anna" gesetzt, dann mit print ausgegeben.

# Frage 2: Schreibe Code, um deinen Namen einzulesen und "Willkommen, [Name]!" auszugeben.
# Schritt 1: Verwende input() um den Namen einzulesen.
# Schritt 2: Speichere in Variable.
# Schritt 3: Gib mit print aus.
name = input("Gib deinen Namen ein: ")
print("Willkommen, " + name + "!")

# Frage 3: Definiere eine Variable für dein Lieblingsessen und gib einen Satz damit aus.
# Schritt 1: Definiere Variable.
essen = "Pizza"
# Schritt 2: Gib Satz aus.
print("Mein Lieblingsessen ist " + essen + ".")

# Frage 4: Berechne das Quadrat einer eingelesenen Zahl.
# Schritt 1: Lies Zahl ein.
zahl = int(input("Gib eine Zahl ein: "))
# Schritt 2: Berechne Quadrat.
quadrat = zahl * zahl
# Schritt 3: Gib aus.
print("Das Quadrat ist:", quadrat)