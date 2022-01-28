"""
kombinatorik.py
Author: Leopold Sappler

Permutation ohne Wiederholung:

    Anordnung von n Objekten, die alle unterscheidbar sind.    
    z.B: In einer Urne befinden sich fünf verschiedenfarbige Kugeln. Wie viele Möglichkeiten gibt es, die Kugeln in einer Reihe anzuordnen?

Variation ohne Wiederholung:

    Bei einer Variation ohne Wiederholung werden k aus n Objekten unter Beachtung der Reihenfolge ausgewählt,
    wobei jedes Objekt nur einmal ausgewählt werden kann.
    z.B: In einer Urne befinden sich fünf verschiedenfarbige Kugeln. Es sollen drei Kugeln unter Beachtung der Reihenfolge und ohne Zurücklegen gezogen werden.
         Bei einem Pferderennen nehmen 10 Pferde teil. Nur die ersten drei Plätze werden prämiert.

Variation mit Wiederholung:

    Bei einer Variation mit Wiederholung werden k aus n Objekten unter Beachtung der Reihenfolge ausgewählt,
    wobei Objekte auch mehrfach ausgewählt werden können.
    z.B: In einer Urne befinden sich fünf verschiedenfarbige Kugeln. Es sollen drei Kugeln unter Beachtung der Reihenfolge und mit Zurücklegen gezogen werden.

Kombination ohne Wiederholung:
    
    Bei einer Kombination ohne Wiederholung werden k aus n Objekten ohne Beachtung der Reihenfolge ausgewählt,
    wobei jedes Objekt nur einmal ausgewählt werden kann.
    z.B: Aus einer 30 köpfigen Schulklasse dürfen 4 Schüler die nahegelegene Universität besichtigen. Wie viele Auswahlmöglichkeiten hat der Lehrer für dieses Ausflug? (30 ueber 4)
         Beim Lotto werden 6 aus 49 Zahlen gezogen.
    
Kombination mit Wiederholung:

    Bei einer Kombination mit Wiederholung werden k aus n Objekten ohne Beachtung der Reihenfolge ausgewählt,
    wobei Objekte auch mehrfach ausgewählt werden können.
    z.B: In einer Urne befinden sich fünf verschiedenfarbige Kugeln. Es sollen drei Kugeln ohne Beachtung der Reihenfolge und mit Zurücklegen gezogen werden.
    

"""

import math
from scipy import special


print("n - Gesamtmenge der Elemente\n"
      "k - Menge der Elemente die gezogen werden\n")

n = int(input("Gesamtmenge n: "))

k = int(input("Menge k: "))

s = input("p - Permutation ohne Wiederholung\n"
          "v - Variation ohne Wiederholung\n"
          "vw - Variation mit Wiederholung\n"
          "k - Kombination ohne Wiederholung\n"
          "kw - Kombination mit Wiederholung\n")

if s == "p":
    print("Permutation ohne Wiederholung:\n")
    print(math.factorial(n))
elif s == "v":
    print("Variation ohne Wiederholung:\n")
    print(math.factorial(n) / math.factorial(n - k))
elif s == "vw":
    print("Variation mit Wiederholung:\n")
    print(math.pow(n, k))
elif s == "k":
    print("Kombination ohne Wiederholung\n")
    print(special.binom(n, k))
elif s == "kw":
    print("Kombination mit Wiederholung\n")
    print(special.binom(n+k-1, k))
else:
    print("Ungueltige Eingabe!!!")

