# Jeu_de_Role
## Petit jeu de rôle en lignes de commande
### REGLES DU JEU
Le but de ce projet est de créer un jeu de rôle textuel dans le terminal.

_ Le jeu comporte deux joueurs : vous et un ennemi.

_ Vous commencez tous les deux avec 50 points de vie.

_ Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie.

_ L'ennemi ne dispose d'aucune potion.

_ Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.

_ Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.

_ L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.

_ Lorsque vous utilisez une potion, vous passez le prochain tour.

### DEROULE DE LA PARTIE
Lorsque vous lancez le script, on vous demande si vous souhaitez attaquer ou utiliser une potion :

"Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "

Cette phrase sera demandée au joueur au début de chaque tour.

_ Si le joueur choisi la première option (1), son personnage inflige des points de dégât à l'ennemi.
Ces points seront compris entre 5 et 10 et déterminés aléatoirement par le programme.

_ Si le joueur choisi la deuxième option (2), son personnage prend une potion.
Les points de vie que la potion donne sont compris entre 15 et 50 et générés aléatoirement par le programme.

Quand le joueur prend une potion, il passe le prochain tour.

Une fois l'action du joueur exécutée, et si l'ennemi est encore vivant, il attaque.
Si l'ennemi est mort, le jeu est terminé.

L'attaque de l'ennemi inflige des dégâts au joueur compris entre 5 et 15,
là encore déterminés aléatoirement par le script.

Si le joueur n'a plus de points de vie, le jeu se termine et la partie est perdue.

Toutes ces opérations se répètent tant que le joueur et l'ennemi sont en vie.

À chaque tour, le joueur attaque en premier. Il ne peut donc pas y avoir de match nul.
Si lorsque le joueur attaque, son attaque fait descendre les points de vie de l'ennemi en dessous (ou égal à) 0,
le joueur gagne la partie sans que l'ennemi n'ait le temps de l'attaquer en retour.
