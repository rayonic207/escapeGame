import pyfiglet
from colorama import Fore, Back, Style, init

# Initialiser colorama pour que les couleurs fonctionnent sous Windows aussi
init()

# Fonction pour afficher l'en-tête avec couleur et texte supplémentaire
def print_header():
    # Création du texte en ASCII Art
    header = pyfiglet.figlet_format("Pirates des Outre-mers")

    # Affichage du texte avec couleur
    print(Fore.YELLOW + header)  # Texte en jaune

    # Texte supplémentaire en dessous
    print(Fore.CYAN + "Arrr matelot! Bienvenue dans l'aventure pirate!")
    print(Fore.CYAN + "Essaie de trouver le trésor.Mais seul des vrai pirates seront de mettre le main dessus.\n")
    print(Fore.GREEN + "Cap vers l'aventure et le tresor! ⚓")
    print(Style.RESET_ALL)  # Réinitialiser le style après utilisation des couleurs

# Appel de la fonction pour afficher l'en-tête
print_header()
