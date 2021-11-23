import math


def tarif_ttc(tarif_HT, taxe):
    """Calculer la prix d'un produit TTC à partir de son nom, tarif HT et son pourcentage de taxe.
    """
    return tarif_HT / 100 * math.ceil(taxe) + tarif_HT


def tarif_remise(tarif_HT, taxe):
    return tarif_ttc(tarif_HT, taxe) / 100 * 12


def main():
    """Le programme principal."""
    # demander le nom du produit à l'utilisateur
    saisie_produit = input("Nom du produit : ")  # une chaîne de caractères
    saisie_qty = input("Quantité en stock : ")  # une chaîne de caractères
    saisie_tarifHT = input("Tarif HT : ")  # une chaîne de caractères
    saisie_taxe = input("Pourcentage de Taxe : ")  # une chaîne de caractères

    le_tarif_HT = float(saisie_tarifHT)  # convertie en un nombre réel
    la_taxe = float(saisie_taxe)  # convertie en un nombre réel
    le_stock = float(saisie_qty)  # convertie en un nombre réel

    # afficher le nom du produit et son tarif TTC
    print("Le prix TTC du produit ", saisie_produit, "est", tarif_ttc(le_tarif_HT, la_taxe), " €")
    print("La taxe est de ", math.ceil(la_taxe), " %")

    if (le_stock * tarif_ttc(le_tarif_HT, la_taxe)) > 1000:
        print("Le total TTc du stock remisé est de ",
              (le_stock * tarif_ttc(le_tarif_HT, la_taxe) - tarif_remise(le_tarif_HT, la_taxe) * le_stock), " €")
        print("La remise est de ", tarif_remise(le_tarif_HT, la_taxe) * le_stock, " €")
    else:
        print("Le total TTc du stock est de ", (le_stock * tarif_ttc(le_tarif_HT, la_taxe))), " €"


if __name__ == "__main__":
    main()
