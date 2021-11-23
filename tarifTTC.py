import math


def calculer_tarif_ttc_unitaire(tarif_HT, taxe):
    """Calculer le prix TTC unitaire d'un produit"""
    return tarif_HT / 100 * taxe + tarif_HT


def main():
    """Le programme principal."""
    # demander le nom du produit à l'utilisateur
    saisie_produit = input("Nom du produit : ")  # une chaîne de caractères
    saisie_tarifHT = input("Tarif HT : ")  # une chaîne de caractères
    saisie_taxe = input("Pourcentage de Taxe : ")  # une chaîne de caractères

    le_tarif_HT = float(saisie_tarifHT)  # convertie en un nombre réel
    la_taxe = float(saisie_taxe)  # convertie en un nombre réel

    # afficher le nom du produit et son tarif TTC
    print("Le prix TTC du produit ", saisie_produit, "est", calculer_tarif_ttc_unitaire(le_tarif_HT, la_taxe), " €")


if __name__ == "__main__":
    main()
