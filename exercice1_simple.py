"""
EXERCICE 1 - TRÈS SIMPLE POUR DÉBUTANTS
======================================

Objectif: Faire des calculs simples avec des listes de nombres
"""

# On importe les données du fichier data_partie3.py
from data_partie3 import quantities, prices

print("=== EXERCICE 1: CALCULS SIMPLES ===")
print()

# 1. Calculer la somme des quantités
print("1. Somme des quantités:")
somme_quantites = sum(quantities)
print(f"   Total des quantités: {somme_quantites}")
print()

# 2. Calculer la moyenne des prix
print("2. Moyenne des prix:")
moyenne_prix = sum(prices) / len(prices)
print(f"   Prix moyen: {moyenne_prix:.2f} euros")
print()

# 3. Trouver le prix le plus élevé
print("3. Prix le plus élevé:")
prix_max = max(prices)
print(f"   Prix maximum: {prix_max:.2f} euros")
print()

# 4. Trouver le prix le plus bas
print("4. Prix le plus bas:")
prix_min = min(prices)
print(f"   Prix minimum: {prix_min:.2f} euros")
print()

# 5. Compter combien d'éléments on a
print("5. Nombre d'éléments:")
nombre_elements = len(prices)
print(f"   Nombre de produits: {nombre_elements}")
print()

print("=== EXERCICE 1 TERMINÉ ===")
