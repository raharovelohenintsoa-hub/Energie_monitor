# ENERGIE MONITOR - Calcul de consommation

def calculer_energie(puissance, duree):
    """Calcule l'énergie consommée en Wh."""
    return puissance * duree

# Données des appareils électriques
appareils = {
    "Refrigerateur": {
        "puissance": 150,
        "duree": 8
    },
    "Television": {
        "puissance": 100,
        "duree": 4
    },
    "Ordinateur": {
        "puissance": 200,
        "duree": 6
    }
}

# Calcul de la consommation totale
energie_totale = 0

print("=== BILAN DE CONSOMMATION ELECTRIQUE ===\n")

for nom, donnees in appareils.items():
    puissance = donnees["puissance"]
    duree = donnees["duree"]

    energie = calculer_energie(puissance, duree)
    energie_totale += energie

    print(f"{nom} : {energie} Wh")

print("\n----------------------------------------"
print(f"Consommation totale : {energie_totale} Wh")
print(f"Consommation totale : {energie_totale / 1000} kWh")
