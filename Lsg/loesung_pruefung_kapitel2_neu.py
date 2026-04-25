# Lösungen zu Prüfung Kapitel 2: Schleifen - Neu

# Frage 1: Gib mit einer for-Schleife die Zahlen von 1 bis 5 aus.
# Schritt 1: range(1,6) für 1 bis 5.
for i in range(1, 6):
    print(i)

# Frage 2: Verwende eine while-Schleife, um von 3 bis 1 zu zählen und "Countdown" auszugeben.
# Schritt 1: i = 3.
i = 3
# Schritt 2: while i > 0, print und i -=1.
while i > 0:
    print("Countdown:", i)
    i -= 1

# Frage 3: Berechne die Summe der Zahlen von 1 bis 10 mit einer Schleife.
# Schritt 1: summe = 0.
summe = 0
# Schritt 2: for i in range(1,11), summe += i.
for i in range(1, 11):
    summe += i
print("Summe:", summe)

# Frage 4: Gib mit einer for-Schleife nur die geraden Zahlen von 2 bis 10 aus.
# Schritt 1: for i in range(2,11,2), da step=2 für gerade.
for i in range(2, 11, 2):
    print(i)


# Frage 5: Gib mit einer for-Schleife nur die geraden Zahlen von 2 bis 10 aus.
# Schritt 1:
for i in 'NAME':
    print(i)
    
# Frage 6: Gebe nur den vierten und fünften Buchstaben des Strings Rinderkennzeichnungsfleischetikettierungsüberwachungsaufgabenübertragungsgesetz mit einer for-Schleife aus.

print("----")
for i in 'Rinderkennzeichnungsfleischetikettierungsüberwachungsaufgabenübertragungsgesetz'[3:5:1]:
    print(i)

# Frage 7: Laufe mit einer for-Schleife iterativ einen String RÜCKWÄRTS durch der deinen Namen RÜCKWÄRTS ausgibt.

for i in "NAME"[::-1]:
    print(i)
