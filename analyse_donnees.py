import pandas as pd

donnees = {
    "appareil": [
        "Refrigerateur",
        "Television",
        "Ordinateur",
        "Climatiseur",
        "Lampe"
    ],
    "puissance_W": [150, 100, 200, 1200, 20],
    "duree_h": [8, 4, 6, 3, 5]
}

df = pd.DataFrame(donnees)

print(df)
