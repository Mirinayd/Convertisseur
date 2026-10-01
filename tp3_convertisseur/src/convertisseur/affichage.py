import datetime as dt


def entete():
    return f"Convertisseur - {dt.date.today().isoformat()}"


def formater(valeur, unite):
    return f"{valeur:.2f} {unite}"