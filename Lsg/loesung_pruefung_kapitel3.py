# Lösungen zu Prüfung Kapitel 3: Verzweigungen

# Frage 1: Frage nach einer Temperatur und gib aus, ob es warm (>20) oder kalt ist.
# Schritt 1: Lies Temperatur ein.
temp = int(input("Gib die Temperatur ein: "))
# Schritt 2: Prüfe mit if.
if temp > 20:
    print("Es ist warm.")
else:
    print("Es ist kalt.")

# Frage 2: Prüfe, ob eine Zahl zwischen 10 und 20 liegt.
# Schritt 1: Lies Zahl ein.
zahl = int(input("Gib eine Zahl ein: "))
# Schritt 2: Prüfe Bereich.
if 10 <= zahl <= 20:
    print("Die Zahl liegt zwischen 10 und 20.")
else:
    print("Die Zahl liegt nicht zwischen 10 und 20.")

# Frage 3: Gib basierend auf einer Note (A, B, C) das Feedback aus.
# Schritt 1: Lies Note ein.
note = input("Gib deine Note ein (A, B, C): ")
# Schritt 2: Verwende if-elif.
if note == "A":
    print("Gut")
elif note == "B":
    print("Okay")
elif note == "C":
    print("Schlecht")
else:
    print("Ungültige Note")

# Frage 4: Frage nach dem Wochentag und gib aus, ob es Wochenende ist.
# Schritt 1: Lies Wochentag ein.
tag = input("Gib den Wochentag ein: ")
# Schritt 2: Prüfe auf Wochenende.
if tag.lower() in ["samstag", "sonntag"]:
    print("Es ist Wochenende.")
else:
    print("Es ist kein Wochenende.")