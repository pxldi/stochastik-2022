"""
diskreteVerteilung.py
Author: Leopold Sappler

BERNOULLI-VERTEILUNG:

    "Mit Welcher Wahrscheinlichkeit tritt ein Erfolg bei einem Versuch ein?"
    X ~ Ber(p)
    Parameter: p - Wahrscheinlichkeit fuer Erfolg

GEOMETRISCHE VERTEILUNG:

    "Wie viele Versuche, bis Erfolg eintritt."
    X ~ geom(p)
    Parameter: n - Anzahl der Versuche
               p - Wahrscheinlichkeit fuer Erfolg

BINOMIAL-VERTEILUNG:

    "Mit welcher Wahrscheinlichkeit treten k Erfolge in n Versuchen ein?"
    X ~ Bin(n,p)
    Parameter: n - Anzahl der Versuche
               k - Anzahl der Erfolge
               p - Wahrscheinlichkeit fuer Erfolg

POISSON-VERTEILUNG:

    "Anzahl der Vorkommnisse in einem Intervall"
     X ~ Po(lambda)
     Parameter: lambda - Auftrittsrate
                k: Anzahl der Vorkommnisse

"""

from scipy.stats import geom, binom, poisson

def geomfunc():
    n = int(input("n:"))
    p = float(input("p:"))

    eingabe = input("Geometrisch: bitte gleich, höchstens oder mindestens eingeben: ")

    if eingabe == "gleich":
        print(geom.pmf(n, p))
    elif eingabe == "höchstens":
        print(geom.cdf(n, p))
    elif eingabe == "mindestens":
        print(1 - geom.cdf(n - 1, p))
    else:
        print("Ungültige Eingabe!")
        return

    print("Median: ", geom.median(p))
    print("Mean: ", geom.mean(p))
    print("Variance: ", geom.var(p))
    print("Standard Deviation: ", geom.std(p))


def binomfunc():
    n = int(input("n:"))
    p = float(input("p:"))
    k = int(input("k:"))

    eingabe = input("Binomial: Für k bitte gleich, höchstens oder mindestens eingeben: ")

    if eingabe == "gleich":
        print(binom.pmf(k, n, p))
    elif eingabe == "höchstens":
        print(binom.cdf(k, n, p))
    elif eingabe == "mindestens":
        k = k - 1
        print(1 - binom.cdf(k, n, p))
    else:
        print("Ungültige Eingabe!")
        return

    print("Median: ", binom.median(n, p))
    print("Mean: ", binom.mean(n, p))
    print("Variance: ", binom.var(n, p))
    print("Standard Deviation: ", binom.std(n, p))


def poissonfunc():
    k = int(input("k:"))
    lam = float(input("lam:"))

    eingabe = input("Poisson: Für k bitte gleich, höchstens oder mindestens eingeben: ")

    if eingabe == "gleich":
        print(poisson.pmf(k, lam))
    elif eingabe == "höchstens":
        print(poisson.cdf(k, lam))
    elif eingabe == "mindestens":
        print(1 - poisson.cdf(k - 1, lam))
    else:
        print("Ungültige Eingabe!")
        return

    print("Median: ", poisson.median(lam))
    print("Mean: ", poisson.mean(lam))
    print("Variance: ", poisson.var(lam))
    print("Standard Deviation: ", poisson.std(lam))


s = input("Verteilung: binom, geom oder poisson: ")

if s == "geom":
    geomfunc()
elif s == "binom":
    binomfunc()
elif s == "poisson":
    geomfunc()
else:
    print("Ungültige Eingabe!")
