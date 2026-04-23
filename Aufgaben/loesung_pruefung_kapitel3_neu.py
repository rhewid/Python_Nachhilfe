# Lösungen zu Prüfung Kapitel 3: Verzweigungen - Neu

# Frage 1: Frage nach dem Alter und gib aus, ob die Person ein Kind (<12), Teenager (12-17) oder Erwachsener ist.
# Schritt 1: input() für alter.
alter = int(input("Gib dein Alter ein: "))
# Schritt 2: if-elif-else.
if alter < 12:
    print("Du bist ein Kind.")
elif 12 <= alter <= 17:
    print("Du bist ein Teenager.")
else:
    print("Du bist ein Erwachsener.")

# Frage 2: Prüfe, ob eine Zahl größer als 100 ist.
# Schritt 1: input().
zahl = int(input("Gib eine Zahl ein: "))
# Schritt 2: if.
if zahl > 100:
    print("Die Zahl ist größer als 100.")
else:
    print("Die Zahl ist nicht größer als 100.")

# Frage 3: Gib basierend auf einer Punktzahl (0-10) aus: <5=Schlecht, 5-7=Okay, >7=Gut.
# Schritt 1: input().
punkte = int(input("Gib deine Punktzahl ein (0-10): "))
# Schritt 2: if-elif-else.
if punkte < 5:
    print("Schlecht")
elif 5 <= punkte <= 7:
    print("Okay")
else:
    print("Gut")

# Frage 4: Frage nach Ja/Nein und gib entsprechend "Ja" oder "Nein" aus.
# Schritt 1: input().
antwort = input("Ja oder Nein? ")
# Schritt 2: if.
if antwort.lower() == "ja":
    print("Ja")
elif antwort.lower() == "nein":
    print("Nein")
else:
    print("Ungültige Antwort")