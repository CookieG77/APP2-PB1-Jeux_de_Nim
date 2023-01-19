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

def affiche_objet(jeu: JdNim, gameconfig: dict):
    """
    Fonction qui permet l'affichage des objets du jeu.
    """
    windowscale = (600, 500)
    dim_object = jeu.dims

    if (jeu.dims[0] * 200) < (jeu.dims[1]*600): # Si la largeur des objets alignés est inférieur à la hauteur des objets alignés
        new_dim_object = [[200 * (windowscale[0]-100) / (dim_object[0] * 200), 0]]
        new_dim_object[0][1] = ((600*new_dim_object[0][0])/200)
        new_dim_object.append([0, new_dim_object[0][1] * windowscale[1] / (dim_object[1] * new_dim_object[0][1])])
        new_dim_object[1][0] = (new_dim_object[0][0] * new_dim_object[1][1]) / new_dim_object[0][1]

    else: # Si la hauteur des objets alignés est inférieur à la largeur des objets alignés
        new_dim_object = [[0, 600 * windowscale[1] / (dim_object[1] * 600)]]
        new_dim_object[0][0] = ((200*new_dim_object[0][1])/600)
        new_dim_object.append([new_dim_object[0][0] * (windowscale[0] - 100) / (dim_object[0] * new_dim_object[0][0]), 0])
        new_dim_object[1][1] = (new_dim_object[0][1] * new_dim_object[1][0]) / new_dim_object[0][0]
    
    new_dim_object = [round(new_dim_object[1][0]),
                    round(new_dim_object[1][1])]

    print(new_dim_object)
    rectangle(500, 0, 600, 500, remplissage = "#AAAAAA", epaisseur = 0)
    for dim_y in range(jeu.dims[1]):
        for dim_x in jeu.plateau[dim_y][0]:
            image(new_dim_object[0] * dim_x,
                  new_dim_object[1] * dim_y,
                  fichier = "textures/Alumette.png",
                  largeur = new_dim_object[0],
                  hauteur = new_dim_object[1],
                  tag = "object",
                  ancrage = "nw")
    


def launch_game(gameconfig: dict) -> None:
    """
    Fonctions qui lance le jeu tout en prenant en compte si le jeu est sauvegarder.
    """
    jeu = JdNim([7,5])
    if gameconfig["GlobalConfig"]["Save"] is True:
        print("sauvegarde à charger !")
    cree_fenetre(600, 500)
    affiche_objet(jeu, gameconfig)
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
