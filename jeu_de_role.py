from random import randint

VIE_JOUEUR = VIE_ENNEMI = 50
POTIONS = 3
OPTIONS = ["1", "2"] #Liste de choix que peut faire le joueur

# MAIN
print("*** JEU DE RÔLE ***")
while True:
    choix_joueur = input("Souhaitez-vous attaquer (1) \U00002694 ou utiliser une potion (2) \U0001F9EA ? ")
    if choix_joueur not in OPTIONS:
        continue
    # Attaque
    if choix_joueur == "1":
        ATTAQUE_JOUEUR = randint(5, 10)
        VIE_ENNEMI = VIE_ENNEMI - ATTAQUE_JOUEUR
        print(f"Vous avez infligé {ATTAQUE_JOUEUR} points de dégats à l'ennemi \U00002694.")
        if VIE_ENNEMI <= 0:
            break # Si l'ennemi meurt on sort du jeu
        else:
            ATTAQUE_ENNEMI = randint(5, 15)
            VIE_JOUEUR = VIE_JOUEUR - ATTAQUE_ENNEMI
            print(f"L'ennemi vous a infligé {ATTAQUE_ENNEMI} points de dégats \U00002694.")
            if VIE_JOUEUR <= 0:
                break # Si le joueur meurt on sort du jeu
    # Prise de potion
    elif choix_joueur == "2":
        if POTIONS > 0:
            point_de_vie = randint(15, 50)
            VIE_JOUEUR = VIE_JOUEUR + point_de_vie
            POTIONS -= 1
            print(f"Vous avez récupéré {point_de_vie} points de vie \U00002764 ({POTIONS} \U0001F9EA restantes).")
            ATTAQUE_ENNEMI = randint(5, 15)
            VIE_JOUEUR = VIE_JOUEUR - ATTAQUE_ENNEMI
            print(f"L'ennemi vous a infligé {ATTAQUE_ENNEMI} points de dégats \U00002694.")
            if VIE_JOUEUR <= 0:
                break # Si le joueur meurt on sort du jeu
        else:
            print("Vous n'avez plus de potions...")
            continue # Si plus de potion on recommence le tour de jeu
        print(f"""Il vous reste {VIE_JOUEUR} points de vie \U00002764.
Il reste {VIE_ENNEMI} points de vie à l'ennemi \U00002764.
{"-" * 70}""")
        print("Vous passez votre tour...") # On passe son tour et l'ennemi attaque une nouvelle fois
        ATTAQUE_ENNEMI = randint(5, 15)
        VIE_JOUEUR = VIE_JOUEUR - ATTAQUE_ENNEMI
        print(f"L'ennemi vous a infligé {ATTAQUE_ENNEMI} points de dégats \U00002694.")
    print(f"""Il vous reste {VIE_JOUEUR} points de vie \U00002764.
Il reste {VIE_ENNEMI} points de vie à l'ennemi \U00002764.
{"-" * 70}""")
if VIE_ENNEMI <= 0:
    print("Vous avez gagné \U0001F4AA\U0001F973")
else: print("Vous avez perdu \U00002620")

print("Fin du jeu")