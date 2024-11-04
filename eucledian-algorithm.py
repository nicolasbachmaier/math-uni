""" Euklidischer Algorithmus (mit schrittweiser Darstellung als
    Z-Linearkombination). Version: 1.0, Nicolas Bachmaier.
    Könnte ggf. Fehler enthalten, Verwendung auf eigene Verantwortung.
    Dieses Dokument darf gerne ohne Rücksprache für Bildungszwecke
    verwendet werden."""


def ggT(a: int, b: int) -> int:
    """
    Größter gemeinsamer Teiler von zwei Zahlen mittels dem
    Euklidischen Algorithmus.
    :param a: Beliebige Zahl aus der Menge der ganzen Zahlen.
    :param b: Beliebige Zahl aus der Menge der ganzen Zahlen.
    :return: Größter gemeinsamer ganzzahliger Teiler der zwei
    Zahlen a und b.
    """
    if b > a:
        a, b = b, a     # Vertausche a und b
    n = a   # Dividend n
    d = b   # Divisor d

    while d != 0:
        # n = alter d; d = Rest
        n, d = d, (n % d)
    return n

def ggT_zLK(a: int, b: int) -> int:
    """
    Größter gemeinsamer Teiler von zwei Zahlen mittels dem
    Euklidischen Algorithmus MIT schrittweiser Darstellung
    der Reste als Z-Linearkombination von a und b.
    :param a: Beliebige Zahl aus der Menge der ganzen Zahlen.
    :param b: Beliebige Zahl aus der Menge der ganzen Zahlen.
    :return: Größter gemeinsamer ganzzahliger Teiler der zwei
    Zahlen a und b + Ausgabe der schrittweisen Reste als
    Z-Linearkombination von a und b.
    """
    if b > a:
        a, b = b, a     # Vertausche a und b
    n = a   # Dividend n
    d = b   # Divisor d

    terms = {a: (1, 0), b: (0, 1)}
    while d != 0:
        rest = n%d
        q = n // d

        # Schrittweise einen Überblick über die Linearkombinationen
        # behalten und die Faktoren von a und b für die jeweiligen
        # Reste abspeichern, um in darauffolgende Zeilen wieder darauf
        # zurückgreifen zu können.
        (a_lambda, b_lambda) = (0,0)
        if n in terms:
            (a_lambda, b_lambda) = terms[n]
        if d in terms:
            (a_lambda, b_lambda) = (a_lambda + (-q) * terms[d][0],
                                    b_lambda + (-q) * terms[d][1])
        terms[rest] = (a_lambda, b_lambda)

        # siehe Algorithmus oben
        n, d = d, rest

    for rest, term in terms.items():
        print(str(rest) + " = " + "(" + str(term[0])+") * " + str(a)
              + " + " + "(" + str(term[1])+") * " + str(b))
    return n


# Beispielverwendung
print(ggT_zLK(10323, 1962))