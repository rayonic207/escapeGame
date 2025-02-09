import pyfiglet
from colorama import Fore, Back, Style, init

# Initialiser colorama pour que les couleurs fonctionnent sous Windows aussi
init()

# Fonction pour afficher l'en-tête avec couleur et texte supplémentaire
def print_header():
    # Création du texte en ASCII Art
    header = pyfiglet.figlet_format("Intrusion pirate !")

    # Affichage du texte avec couleur
    print(Fore.YELLOW + header)  # Texte en jaune

    # Texte supplémentaire en dessous
    print(Fore.CYAN + "Ohé matelot ! T'as réussi à grimper à bord du navire.")
    print(Fore.CYAN + "Maintenant, mets la main sur notre affiche et tente de percer son mystère.\n")
    print(Fore.GREEN + "Cap sur la station pirate ! ⚓")
    print(Style.RESET_ALL)  # Réinitialiser le style après utilisation des couleurs

# Appel de la fonction pour afficher l'en-tête
print_header()
