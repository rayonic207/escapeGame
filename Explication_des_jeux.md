# 1. Mystère 5 Stack
L’objectif de premier jeu était de proposer une expérience ludique et éducative où les participants, guidés par des M5 Stacks, doivent résoudre une série de 2 quiz interactifs mêlant technologie, réflexion et d'exploration pour aboutir à un message de victoire.

#### Quiz 1 : "Le 1er ordinateur electronique, ENIAC, a ete cree en 1945. Mais combien de temps lui fallait-il pour demarrer ?"
- A: Quelques minutes
- B: Quelques jours
- C: Quelques heures

La réponse correcte est la **C: Quelques heures**.


#### Quiz 2 : "Trouver la correspondance binaire de cette sequence : 5 - 8 - 3 - 7"
- A: 0101 - 0111 - 1001 - 0101
- B: 0101 - 1000 - 0011 - 0111
- C: 1110 - 0010 - 1101 - 0110
     
La réponse correcte est la **B: 0101 - 1000 - 0011 - 0111**.

Ils ont à leurs dispositions des indices sur des M5Stack pour les aider qui sont discimuler un peu partout dans la pièce et ils possèdent des "parchemins pirates" contenant une énigme pour les permettrent de retrouver ces indices.

À la fin de ce jeu, un message s’affiche sur le M5Stack principal. Ce message est une énigme à décoder, orientant les participants vers le deuxième jeu intitulé “Intrusion des pirates”.

- Message : "Leve l'ancre matelot ! Cap sur le navire 192.168.1.120 a la porte 147 et demande pour le cap'tain Blackbeard et donne le mot passe pour entrer.

# 2. Intrusion Des Pirates

![Screenshot from 2025-02-08 22-20-22](https://github.com/user-attachments/assets/fc66b1bb-85ab-4551-81ac-1c584b5e1312)

L’objectif de ce second challenge permet aux participants réaliser une attaque par dictionnaire sur une machine à distance pour tenter de cracker le mot de passe en utilisant la commande **hydra** et le dictionnaire de mot de passe **rockyou.txt**.
- commande :  hydra -l blackbeard -P rockyou.txt ssh://192.168.1.120:147 -V

Et les participants doivent obtenir comme mot de passe : **secret**. Ensuite, ils se connectent à l'utilisateur blackbeard à distance en utilisant la commande : ssh -p 147 blackbeard@192.168.1.120. Puis trouver une image nommée **pirate_des_outre-mers.jpg** sur cette machine qui contient un message caché. Pour les aider, un fichier **indice.txt** contient la commande steghide pour récupérer le message caché dans l'image.

Après avoir lancer la commande, les participants obtiennent un fichier **flag.txt** contenant les instructions pour accéder au jeu intitulé “Station Radio Pirate”.

**À savoir que : Pour la machine à distance, nous avons utilisé un raspberry pi 3.**

# 3. Station Radio Pirate

![Screenshot from 2025-02-08 22-20-53](https://github.com/user-attachments/assets/0dad7bbc-2162-4941-b809-f8f28134e94e)

L’objectif de ce troisième challenge est que les participants utilisent les indices à leur disposition pour déchiffrer un message encodé en morse transmis par une radio . Ce message correspond au nom d’un dossier qu’ils doivent chercher sur la machine à leur disposition. Ce dossier contient un fichier contenant un code final pour passer .

Une fois que les participants se sont connecté sur la radio 

**À savoir que : Pour réaliser la radio, nous avons utilisé un raspberry pi.**
