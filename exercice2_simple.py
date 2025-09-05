"""
EXERCICE 2 - TRÈS SIMPLE POUR DÉBUTANTS
======================================

Objectif: Compter combien de chaque type de produit on a
"""

# On importe les données
from data_partie3 import products

print("=== EXERCICE 2: COMPTER LES PRODUITS ===")
print()

# 1. Compter manuellement chaque type de produit
print("1. Compter chaque type de produit:")

# On crée un dictionnaire pour compter
compteur = {}

# On parcourt tous les produits
for produit in products:
    if produit in compteur:
        compteur[produit] = compteur[produit] + 1
    else:
        compteur[produit] = 1

# On affiche le résultat
for produit, nombre in compteur.items():
    print(f"   {produit}: {nombre} fois")

print()

# 2. Trouver le produit le plus fréquent
print("2. Produit le plus fréquent:")
produit_max = max(compteur, key=compteur.get)
print(f"   {produit_max}: {compteur[produit_max]} fois")
print()

# 3. Trouver le produit le moins fréquent
print("3. Produit le moins fréquent:")
produit_min = min(compteur, key=compteur.get)
print(f"   {produit_min}: {compteur[produit_min]} fois")
print()

# 4. Nombre total de produits différents
print("4. Nombre de types de produits différents:")
nombre_types = len(compteur)
print(f"   {nombre_types} types de produits différents")
print()

print("=== EXERCICE 2 TERMINÉ ===")
