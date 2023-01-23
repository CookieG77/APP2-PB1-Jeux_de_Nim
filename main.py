#All the code in this file was created by Maxime Cordonnier and Paul Amouroux for a school project.
"""
Fichier principale contenant l'execution du code permettant au lancement du jeux de Nim.
"""

import json
from fltk import (
    cree_fenetre,
    ferme_fenetre,
    donne_ev,
    type_ev,
    touche,
    image,
    rectangle,
    mise_a_jour,
    efface
)
from mad_fltk import (
    ButtonRectTex
)
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
    # ---Calcule des dimensions des objets---
    windowscale = gameconfig["GlobalConfig"]["WindowScale"]
    dim_object = jeu.dims

    # Si la largeur des objets alignés est inferieur à la hauteur des objets alignés.
    if (jeu.dims[0] * 200) < (jeu.dims[1]*600):
        new_dim_object = [[200 * (windowscale[0] - 100) / (dim_object[0] * 200), 0]]
        new_dim_object[0][1] = ((600*new_dim_object[0][0])/200)
        new_dim_object.append(
            [0,
            new_dim_object[0][1] * windowscale[1] / (dim_object[1] * new_dim_object[0][1])]
        )
        new_dim_object[1][0] = (new_dim_object[0][0] * new_dim_object[1][1]) / new_dim_object[0][1]

    # Si la hauteur des objets alignés est inférieur à la largeur des objets alignés.
    else:
        new_dim_object = [[0, 600 * windowscale[1] / (dim_object[1] * 600)]]
        new_dim_object[0][0] = ((200*new_dim_object[0][1])/600)
        new_dim_object.append(
            [new_dim_object[0][0] * (windowscale[0] - 100) / (dim_object[0] * new_dim_object[0][0]),
            0]
        )
        new_dim_object[1][1] = (new_dim_object[0][1] * new_dim_object[1][0]) / new_dim_object[0][0]

    new_dim_object = [round(new_dim_object[1][0]),
                    round(new_dim_object[1][1])]

    #---Affichage---
    rectangle(500, 0, 600, 500, remplissage = "#AAAAAA", epaisseur = 0)

    list_button = []
    for dim_y in range(jeu.dims[1]):
        list_temp = []
        for dim_x in jeu.plateau[dim_y][0]:
            object_button = ButtonRectTex(
                (new_dim_object[0] * dim_x, new_dim_object[1] * dim_y),
                (new_dim_object[0] * (dim_x + 1), new_dim_object[1] * (dim_y + 1))
                )
            object_button.draw('textures/Alumette.png')
            list_temp.append(object_button)
        list_button.append(list_temp)

    return list_button

def launch_game(gameconfig: dict) -> None:
    """
    Fonctions qui lance le jeu tout en prenant en compte si le jeu est sauvegarder.
    """
    jeu = JdNim([5, 6, 25, 5])
    dim_object = jeu.dims
    if gameconfig["GlobalConfig"]["Save"] is True:
        print("sauvegarde à charger !")
    cree_fenetre(gameconfig["GlobalConfig"]["WindowScale"][0],
                 gameconfig["GlobalConfig"]["WindowScale"][1])
    list_button = affiche_objet(jeu, gameconfig)

    continuer = True
    while continuer:
        efface("overlay")
        event = donne_ev()
        if type_ev(event) == "Quitte":
            continuer = False
        elif type_ev(event) == "Touche":
            if touche(event) == "Escape":
                continuer = False
# ---------------------------------------
        for i in range(dim_object[1]):
            for j in range(len(list_button[i])):
                if list_button[i][j].is_hover():
                    list_button[i][j].overlay()
                if list_button[i][j].is_pressed(event):
                    print("oui, " + str(i) + " : " + str(j))
# ---------------------------------------
        mise_a_jour()
    ferme_fenetre()

configjson = load_json("config.json")
launch_game(configjson)
