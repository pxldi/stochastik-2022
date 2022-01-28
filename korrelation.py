"""
korrelation.py
Author: Leopold Sappler

Berechnung und Zeichnen von Korrelationskoeffizient

    r > 0: Ist der Korrelationskoeffizient größer als null, spricht man von einer positiven Korrelation.
    In diesem Fall gilt „je mehr desto mehr“. Das heißt, je höher die Werte der einen Variablen sind,
    desto höher sind auch die Werte der anderen Variable. Ein Beispiel für einen positiven Korrelationskoeffizienten
    wäre etwa der Zusammenhang zwischen der Körpergröße und der Schuhgröße einer Person: Je größer jemand ist,
    desto größere Schuhe wird er tendenziell auch tragen.

    r < 0: Ist der Korrelationskoeffizient kleiner als null, ist der Zusammenhang negativ. Das bedeutet, wir befinden
    uns im „je mehr desto weniger Fall“. Bei einer negativen Korrelation gehen nämlich höhere Werte der einen
    Variablen mit niedrigeren Werten der anderen Variablen einher. Ein Beispiel dafür wäre die Korrelation zwischen
    den bearbeiteten Übungsaufgaben und den Fehlern in einem Test: Je mehr Übungsaufgaben jemand bearbeitet hat,
    desto weniger Fehler wird er voraussichtlich machen.

    r ~ 0: Liegt der Korrelationskoeffizient nahe 0, gibt es keinen linearen Zusammenhang zwischen den Variablen.
    Folglich kann man mit dem Korrelationskoeffizienten keine Aussage darüber machen, wie sich die Werte der einen
    Variablen verändern, wenn die Werte der anderen Variable steigen. Beachte allerdings, dass der
    Korrelationskoeffizient nur lineare Zusammenhänge abbildet. Es kann also sein, dass die Variablen vielleicht
    trotzdem zusammenhängen, nur eben quadratisch oder exponentiell.

    Beispiel: Wie korreliert die Anzahl der durchschnittlichen Sonnenstunden pro Tag (a)
              mit den Besuchszahlen eines Freizeitparks (b).
              ANZAHL SONNENSTUNDEN a = (1.6, 2.6, 3.7, 5.3, 6.9, 7.1, 7.2, 6.7, 5.1, 3.6, 2.1, 1.4)
              BESUCHERZAHL b = (28300, 28000, 41000, 40000, 48000, 47500, 43000, 50700, 50000, 48000, 25000, 24000)
              r von a,b =  0.83419769 (stark positive Korrelation)

"""

import numpy as np
from matplotlib import pyplot as plt

a = (1.6, 2.6, 3.7, 5.3, 6.9, 7.1, 7.2, 6.7, 5.1, 3.6, 2.1, 1.4)
b = (28300, 28000, 41000, 40000, 48000, 47500, 43000, 50700, 50000, 48000, 25000, 24000)

print(np.corrcoef(a, b))

plt.scatter(a, b)
plt.show()
