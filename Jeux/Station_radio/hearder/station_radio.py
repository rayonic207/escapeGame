import pyfiglet
from colorama import Fore, Back, Style, init

# Initialiser colorama pour que les couleurs fonctionnent sous Windows aussi
init()

# Fonction pour afficher l'en-tête avec couleur et texte supplémentaire
def print_header():
    # Création du texte en ASCII Art
    header = pyfiglet.figlet_format("Station PiRate !")

    # Affichage du texte avec couleur
    print(Fore.YELLOW + header)  # Texte en jaune

    # Texte supplémentaire en dessous
    print(Fore.CYAN + "Arrr! Par le triden de Neptune !\n")
    print(Fore.CYAN + "Je m'attendais à ce que t'abandonne le navire.")
    print(Fore.CYAN + "Maintenant que t'es à bord de la station. Arme-toi de ta radio et calibre")
    print(Fore.CYAN + "ton compas sur la bonne fréquence\n")
    print(Fore.CYAN + "Tends bien l'oreille à ce message et retourne à bord de ton navire initial.")
    print(Fore.CYAN + "Tu sauras alors quoi chercher.\n")
    print(Fore.GREEN + "Si t'as du sable dans les oreilles, utilise GQRX,")
    print(Fore.GREEN + "ton fidèle perroquet numérique qui est à bord de ton vaisseau ! ⚓")
    print(Style.RESET_ALL)  # Réinitialiser le style après utilisation des couleurs

# Appel de la fonction pour afficher l'en-tête
print_header()
