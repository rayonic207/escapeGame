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

Ils ont à leurs dispositions des indices sur des M5Stack pour les aider qui sont discimuler un peu partout dans la pièce et ils possèdent des "parchemins pirates" contenant une énigme pour les permettrent de retrouver ces indices. Pour le quiz 2, les participants ont un parchemin conportant les correspondances binaires de chaque chiffres mais tout en gardant le thème pirate tels qu'un drapeau correspont à 0 et un palmier correspont à un 1.  

À la fin de ce jeu, un message s’affiche sur le M5Stack principal. Ce message est une énigme à décoder, orientant les participants vers le deuxième jeu intitulé “Intrusion des pirates”.

- Message : "Leve l'ancre matelot ! Cap sur le navire 192.168.1.120 a la porte 147 et demande pour le cap'tain Blackbeard et donne le mot passe pour entrer. Attention, seuls les vrais pirates des réseaux peuvent atteindre cette destination."

# 2. Intrusion Des Pirates

![Screenshot from 2025-02-08 22-20-22](https://github.com/user-attachments/assets/fc66b1bb-85ab-4551-81ac-1c584b5e1312)

L’objectif de ce second challenge permet aux participants réaliser une attaque par dictionnaire sur une machine à distance pour tenter de cracker le mot de passe en utilisant la commande **hydra** et le dictionnaire de mot de passe **rockyou.txt**.
- commande :  hydra -l blackbeard -P rockyou.txt ssh://192.168.1.120:147 -V

Et les participants doivent obtenir comme mot de passe : **secret**. Ensuite, ils se connectent à l'utilisateur blackbeard à distance en utilisant la commande : ssh -p 147 blackbeard@192.168.1.120. Puis trouver une image nommée **pirate_des_outre-mers.jpg** sur cette machine qui contient un message caché. Pour les aider, un fichier **indice.txt** contient la commande **steghide extract -sf image.jpg** pour récupérer le message caché dans l'image.
- Message : "Ohé matelot ! T'as réussi à percer le mystère de l'affiche. Mets les voiles vers le navire 192.168.1.122. Là-bas, l'capitaine répond au nom d'Etudiant. Mais veille bien à retenir ça : 107.1 MHz. À la bordage ! Cap sur la station pirate !"

Après avoir lancer la commande, les participants obtiennent un fichier **flag.txt** contenant le message pour accéder au jeu intitulé “Station Radio Pirate”.

**À savoir que : Pour la machine à distance, nous avons utilisé un raspberry pi 3.**

# 3. Station Radio Pirate

![Screenshot from 2025-02-08 22-20-53](https://github.com/user-attachments/assets/0dad7bbc-2162-4941-b809-f8f28134e94e)

L’objectif de ce troisième challenge est que les participants utilisent les indices à leur disposition pour déchiffrer un message encodé en morse transmis par une radio sur un raspberry pi. Ce message correspond au nom d’un dossier qu’ils doivent chercher sur la machine à leur disposition. Ce dossier contient un fichier contenant un code final pour passer.

Une fois que les participants se sont connecté sur la machine à distance que la radio se lance automatiquement. Cela aura pour effet de rendre plus fluide le challenge, le joueur n’aura pas à lancer manuellement la radio. Par ailleurs, cela garantit aussi que le joueur respecte les étapes du jeu. 

Pour réaliser cette fluidité, nous avons ajouté dans le fichier **.bashrc** du raspberry la commande : sudo PiFmRds/src/pi_fm_rds -freq 107.1 -audio PiFmRds/src/santa_morse.wav -ps PiRate_des_Autres_Mers -rt "Transmission Morse".

Alors le message diffusé sur la radio commence par une voie d’introduction qui fera comprendre au joueur que c’est le début du message puisque celui-ci tourne en boucle. Cette voix déclare de manière énigmatique : “**Hello Moussaillons, un morse a codé ce message, aide-moi à le décoder.**” Immédiatement après, le signal en code morse est transmis.

Après leurs efforts de décryptage, le message révélé est : **santa**. Ce message correspond au nom d’un fichier qu’ils doivent trouver sur l’ordinateur mis à leur disposition depuis le début du jeu. 

# 4. Crocs du requin

L'objectif de ce challenge de fin est de réaliser une analyse d'un fichier .pcapng nommé **les_crocs_du_requins.pcapng** qui se trouve dans le dossier santa. Et dans l'un des trames du fichier se trouve un message pour terminer l'Escape Game dont le messsage est **code : hacker**.

Pour réaliser le fichier pcap, nous avons utilisé un esp8266 pour envoyer un ping vers une machine du réseau pirate-dom tout les 5 secondes qui contient le message.
