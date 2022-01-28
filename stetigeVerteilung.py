"""
stetigeVerteilung.py
Author: Leopold Sappler

GLEICHVERTEILUNG: auch uniforme Verteilung

    "Jeder denkbare reelle Wert der Zufallsvariable ist in einem vorgegebenen Intervall gleich wahrscheinlich"
    X ~ G(a, b)
    Parameter:
            a: min Wert
            b: max Wert
            x: gesuchter Wert
    Beispiel:
            Stetige Gleichverteilung zwischen a = 0 und b = 60
            Wie wahrscheinlich ist es, dass man weniger als 15 Minuten warten muss.
            uniform.cdf(15, 0, 60) = 0.25 = 25% Wahrscheinlichkeit

EXPONENTIALVERTEILUNG:

    "Die Exponentialverteilung ist eine Wahrscheinlichkeitsverteilung zur Bestimmung zufälliger Zeitintervalle.
    Sie wird meist für Warte- oder Ausfallzeiten verwendet, wie zum Beispiel die Länge eines Telefongesprächs,
    den radioaktiven Zerfall von Atomen oder die Lebensdauer deines Handys."
    Exp(lambda)
    Parameter:
            lambda: gegeben
            x: gesuchter Wert
    Beispiel:
            Lebensdauer lambda = 0.001
            wie wahrscheinlich ist es, dass das Gerät noch ein weiteres Jahr funktioniert. x = 365
            expon.cdf(365, scale = 1/0.001) = 0.306
            => Die Wahrscheinlichkeit, dass es noch funktioniert ist also bei fast 70 Prozent.

NORMALVERTEILUNG:

    "Der zentrale Grenzwertsatz beschreibt das Phänomen, dass reale zufällige Prozesse in
    ihrer Summe häufig glockenförmige Verteilungen aufweisen. So sind zum Beispiel Wachstumsprozesse,
    wie die Körpergröße aller Männer oder Messvorgänge, wie beispielsweise die Sprungweite von Kängurus,
    immer normalverteilt."
    N(erwartungswert, varianz)
    Parameter:
            erwartungswert: Mitte der Kurve
            varianz: Streckung / Stauchung der Kurve
    Beispiel:
            Wahrscheinlichkeit, dass eine Kerze zwischen 33 und 47 Stunden brennt.

"""

from scipy.stats import uniform, expon


def uniformfunc():
    a = int(input("a: "))
    b = int(input("b: "))
    x = int(input("x: "))

    eingabe = input("Gleichverteilung: hoechstens oder hoeherals eingeben")

    if eingabe == "hoechstens":
        print(uniform.cdf(x, a, b))
    elif eingabe == "hoeherals":
        print(uniform.sf(x, a, b))
    else:
        print("Ungültige Eingabe!")
        return

    print("Erwartungswert: ", (a + b) / 2)
    print("Varianz: ", ((b - a) ** 2) / 12)


def exponfunc():
    lam = float(input("lambda: "))
    x = int(input("x: "))

    eingabe = input("Exponentialverteilung: hoechstens oder hoeherals eingeben")

    if eingabe == "hoechstens":
        print(expon.cdf(x, scale=1 / lam))
    elif eingabe == "hoeherals":
        print(expon.sf(x, scale=1 / lam))
    else:
        print("Ungültige Eingabe!")
        return

    print("Erwartungswert: ", 1 / lam)
    print("Varianz: ", 1 / (lam ** 2))


s = input("Verteilung: gleich oder expon: ")

if s == "gleich":
    uniformfunc()
elif s == "expon":
    exponfunc()
else:
    print("Ungültige Eingabe!!!")
