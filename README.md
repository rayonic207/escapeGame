# Pirate des Outre-Mers (Escape Game edition JPO 2024)
![logo_pirate_des_dom](https://github.com/user-attachments/assets/01934350-f3e3-4c68-81c6-88f061f609ec)
## Présentation
Ce projet est un Escape Game réalisé par les étudiants de 2ème à l'IUT de Kourou en BUT Réseaux & Télécommunications. Il a été mise en place pour présenter aux participants, notre filière Réseaux & Télécommunication dans le domaine de la cybersécurité tout en s'amusant lors d'un évènement tels que la JPO (Journée Porte Ouvert de l'IUT). Il est composé de 4 jeux : Mystère 5 Stack, Intrusion Des Pirates, Station Radio Pirate et Les Crocs du Requin. Pour sa réalisation, les étudiants ont utilisés :
- 3 M5 Stack
- 3 Raspberry Pi (avec 1 cartes SD chacun)
- 1 ordinateur (avec un compte spécial pour les participants)

Avec le premier Raspberry Pi, nous avons réalisé notre propre réseau Wi-Fi **pirate-dom**, pour cela nous avons téléchargé et installé RaspAP dessus.

**À savoir que: Pour les tutos et programmes sources, vous les trouverez dans le dossier annexe. Chaque programme est commenté pour faciliter la compréhension et la réutilisation.**

## Jeux

### Mystère 5 Stack
L’objectif de premier jeu était de proposer une expérience ludique et éducative où les participants, guidés par des M5 Stacks, doivent résoudre une série de 2 quiz interactifs mêlant technologie, réflexion et d'exploration pour aboutir à un message de victoire. 

- Quiz 1 :
   - "Le 1er ordinateur electronique, ENIAC, a ete cree en 1945. Mais combien de temps lui fallait-il pour demarrer ?"
     - A: Quelques minutes
     - B: Quelques jours
     - C: Quelques heures

- Quiz 2 :
   - "Trouver la correspondance binaire de cette sequence : 5 - 8 - 3 - 7"
     -  A: 0101 - 0111 - 1001 - 0101
     -  B: 0101 - 1000 - 0011 - 0111
     -  C: 1110 - 0010 - 1101 - 0110

Ils ont à leurs dispositions des indices sur des M5Stack pour les aider qui sont discimuler un peu partout dans la pièce et ils possèdent des "parchemins pirates" contenant une énigme pour les permettrent de retrouver ces indices.

À la fin de ce jeu, un message s’affiche sur le M5Stack principal. Ce message est une énigme à décoder, orientant les participants vers le deuxième jeu intitulé “Intrusion des pirates”.

- Message : "Leve l'ancre matelot ! Cap sur le navire 192.168.1.120 a la porte 147 et demande pour le cap'tain Blackbeard et donne le mot passe pour entrer.
Attention seul les vrais pirates des reseaux peuvent atteindre cette destination."

**À savoir que : Les boutons physiques (A, B, C) du M5Stack permettaient de soumettre une réponse. Une réponse correcte affichait un message de validation. Une réponse incorrecte redémarre le quiz**

### Intrusion Des Pirates

L’objectif de ce second challenge permet aux participants réaliser une attaque par dictionnaire sur une machine à distance pour tenter de cracker le mot de passe en utilisant la commande **hydra** et le dictionnaire de mot de passe **rockyou.txt**. 
- commande :  hydra -l blackbeard -P rockyou.txt ssh://192.168.1.120:147

Puis trouver une image sur cette machine qui contient un message caché. Pour la machine à distance, nous avons utilisé un raspberry pi 3.
