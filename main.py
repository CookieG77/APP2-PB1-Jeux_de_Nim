#All the code in this file was created by Maxime Cordonnier and Paul Amouroux for a school project.
"""
Fichier principale contenant l'execution du code permettant au lancement du jeux de Nim.
"""

import json
from fltk import cree_fenetre, ferme_fenetre, donne_ev, type_ev, touche, image, rectangle, attend_ev, mise_a_jour, hauteur_fenetre, largeur_fenetre
from classes import JdNim

def load_json(filename: str, directory: str = "") -> dict:
    """
    Permet de charger le dico stocker en format json
    """
    with open(directory + filename, encoding="utf-8") as file:
        content = json.load(file)
    file.close()
    return content


def save_json(directory: str, filename: str, content: any):
    """
    Permet de sauvegarder le dico en format json
    """
    with open(directory + filename, "w", encoding="utf-8") as file:
        json.dump(content, file)
    file.close()

def affiche_objet(jeu: JdNim):
    """
    Fonction qui permet l'affichage des objets du jeu.
    """
    windowscale = (largeur_fenetre(),hauteur_fenetre())
    dim_object = [0, len(jeu.plateau)]
    print(jeu.plateau)
    for coo_y in range(dim_object[1]):
            if jeu.plateau[coo_y][1] > dim_object[0]:
                dim_object[0] = jeu.plateau[coo_y][1]
    ratio = round(dim_object[0]*200/windowscale[0], 1), round(dim_object[1]*600/windowscale[1], 1)
    print(ratio)
    for coo_y in range(dim_object[1]):
        for coo_x in jeu.plateau[coo_y][0]:
            image(coo_x*200, coo_y*600,
                  "textures/Alumette.png",
                  ancrage = "nw", tag = "obj")


def launch_game(gameconfig: dict) -> None:
    """
    Fonctions qui lance le jeu tout en prenant en compte si le jeu est sauvegarder.
    """
    jeu = JdNim([7,5,3,1])
    if gameconfig["GlobalConfig"]["Save"] is True:
        print("sauvegarde à charger !")
    cree_fenetre(500, 500)
    affiche_objet(jeu)
    CONTINUER = True
    while CONTINUER:
        event = donne_ev()
        if type_ev(event) == "Quitte":
            CONTINUER = False
        elif type_ev(event) == "Touche":
            if touche(event) == "Escape":
                CONTINUER = False
        mise_a_jour()
    ferme_fenetre()

configjson = load_json("config.json")
launch_game(configjson)
