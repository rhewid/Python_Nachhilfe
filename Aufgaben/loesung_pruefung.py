## Lösungen zur Prüfung

# Frage 1: Was gibt das folgende Programm aus?
# print("Hallo Welt")
# Antwort: Hallo Welt

# Frage 2: Schreibe Code, um zwei Zahlen einzulesen und ihre Summe auszugeben.
a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))
print("Summe:", a + b)

# Frage 3: Erkläre den Unterschied zwischen for und while Schleife.
# Antwort: For-Schleife wird für eine bekannte Anzahl von Iterationen verwendet (z.B. über eine Liste oder range).
# While-Schleife läuft solange eine Bedingung wahr ist.

# Frage 4: Schreibe eine if-else Anweisung, die prüft, ob eine Zahl positiv ist.
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 0:
    print("Positiv")
else:
    print("Nicht positiv")

# Frage 5: Berechne die Fakultät einer Zahl mit einer Schleife.
n = int(input("Gib n ein: "))
fak = 1
for i in range(1, n+1):
    fak *= i
print("Fakultät:", fak)