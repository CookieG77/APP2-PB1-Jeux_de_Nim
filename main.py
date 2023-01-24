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
    rectangle,
    mise_a_jour,
    efface,
    efface_tout
)
from mad_fltk import (
    ButtonRectTex,
    ButtonCircle,
    Text
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
    rectangle(500, 0, 600, 500, remplissage = "#BABABA", epaisseur = 0)

    list_button = []
    for dim_y in range(jeu.dims[1]):
        list_temp = []
        for dim_x in jeu.plateau[dim_y][0]:
            object_button = ButtonRectTex(
                (new_dim_object[0] * dim_x, new_dim_object[1] * dim_y),
                (new_dim_object[0] * (dim_x + 1), new_dim_object[1] * (dim_y + 1))
                )
            object_button.draw('textures/Alumette.png')
            list_temp.append((object_button, dim_x))
        list_button.append(list_temp)

    return list_button

def launch_game(gameconfig: dict) -> None:
    """
    Fonctions qui lance le jeu tout en prenant en compte si le jeu est sauvegarder.
    """
    jeu = JdNim([7, 5, 3])
    dim_object = jeu.dims
    lst_choice = [[], "X"]

    if gameconfig["GlobalConfig"]["Save"] is True:
        print("sauvegarde à charger !")
    cree_fenetre(gameconfig["GlobalConfig"]["WindowScale"][0],
                 gameconfig["GlobalConfig"]["WindowScale"][1])
    list_button = affiche_objet(jeu, gameconfig)
    end_turn_button = ButtonCircle(
        (gameconfig["GlobalConfig"]["WindowScale"][0] - 50,
         gameconfig["GlobalConfig"]["WindowScale"][1] - 50),
        40, 5)
    end_turn_button_reset = False
    end_turn_button.draw("#AAAAAA", "#888888")
    joueurs = Text(
        (gameconfig["GlobalConfig"]["WindowScale"][0] - 10, 10),
        (gameconfig["GlobalConfig"]["WindowScale"][0] - 90, 90),
        "J.1"
    )
    joueurs.draw()

    continuer = True
    while continuer:
        efface("overlay")
        event = donne_ev()
        if type_ev(event) == "Quitte":
            continuer = False
        elif type_ev(event) == "Touche":
            if touche(event) == "Escape":
                continuer = False
        elif end_turn_button.is_pressed(event) and lst_choice[0]:
            end_turn_button_reset = True
            jeu.del_elements(lst_choice[0])
            efface_tout()
            if gameconfig["GlobalConfig"]["Misery-Mode"]:
                if jeu.check_victory(misery = True):
                    break
            else:
                if jeu.check_victory():
                    break
            else:
                list_button = affiche_objet(jeu, gameconfig)
            if lst_choice[1] == "X":
                lst_choice = [[], "O"]
                joueurs = Text(
                    (gameconfig["GlobalConfig"]["WindowScale"][0] - 10, 10),
                    (gameconfig["GlobalConfig"]["WindowScale"][0] - 90, 90),
                    "J.2"
                )
            else:
                lst_choice = [[], "X"]
                joueurs = Text(
                    (gameconfig["GlobalConfig"]["WindowScale"][0] - 10, 10),
                    (gameconfig["GlobalConfig"]["WindowScale"][0] - 90, 90),
                    "J.1"
                )
            joueurs.draw()
            print(jeu.check_victory(misery=True))
            
            
            

        #Changement Statut bouton de fin de tour.
        if end_turn_button_reset:
            end_turn_button_reset = False
            #Si aucun objet choisit pour le moment.
            if not lst_choice[0]:
                end_turn_button.draw(color_ext = "#AAAAAA",
                                     color_int = "#888888")
            #Si un ou plusieurs objets choisits.
            else:
                end_turn_button.draw(color_ext = "#AAFFAA",
                                     color_int = "#88FF88")

        #Detection Click sur objet & objet avec overlay
        for i in range(dim_object[1]):
            for j in range(len(list_button[i])):
                if list_button[i][j][0].is_hover():
                    list_button[i][j][0].overlay()
                if list_button[i][j][0].is_pressed(event):
                    if not lst_choice[0]:
                        end_turn_button_reset = True
                        lst_choice[0].append((i, list_button[i][j][1]))
                        list_button[i][j][0].overlay(
                            color = "#EE9999",
                            tag = str(hex(i))+str(hex(list_button[i][j][1]))
                            )
                    elif i == lst_choice[0][0][0]:
                        if (i, list_button[i][j][1]) not in lst_choice[0]:
                            lst_choice[0].append((i, list_button[i][j][1]))
                            list_button[i][j][0].overlay(
                                color = "#EE4949",
                                tag = str(hex(i))+str(hex(list_button[i][j][1]))
                                )
                        else:
                            lst_choice[0].remove((i, list_button[i][j][1]))
                            efface(str(hex(i))+str(hex(list_button[i][j][1])))
                            if not lst_choice[0]:
                                end_turn_button_reset = True

        mise_a_jour()
    ferme_fenetre()
    if lst_choice[1] == "X" and not gameconfig["GlobalConfig"]["Misery-Mode"]:
        print("victoire de l'équipe 1.")
    else:
        print("victoire de l'équipe 2.")

configjson = load_json("config.json")
launch_game(configjson)
