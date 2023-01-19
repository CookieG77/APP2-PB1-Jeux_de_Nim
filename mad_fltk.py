"""
Menu ADdon fltk
"""

from fltk import *

__all__ = [
    # Classe
    "ButtonRect",
    "ButtonRectTex",
    "ButtonCircle",
    "ButtonCircleTex",
    "Text",
    "SliderBar",
    # Fonction
    "get_font_size"
]

def get_font_size(text: str,
                  dimension: tuple,
                  police: str = "Helvetica"
                  ):
    """
    Renvoie la taille nécessaire de la police pour rentrer dans une zone définie
    """
    font_size = 24
    while font_size != 1:
        dim_text = taille_texte(text, police, str(font_size))
        if dimension[0] > dim_text[0] and dimension[1] > dim_text[1]:
            return font_size
        font_size -= 1
    return 1


class ButtonRect:
    """
    Classe permettant la création d'un
    bouton de forme rectangulaire
    """
    def __init__(self,
                 coord_a: tuple,
                 coord_b: tuple,
                 border: int = 1
                 ):
        """
        Initialisation du bouton.
        """
        self.coord_a = coord_a
        self.coord_b = coord_b
        self.border = border

    def draw(self,
             color_int: str,
             color_ext: str = "#000000",
             text: str = "",
             font: str = "Helvetica"
             ):
        """
        Fonction pour afficher le bouton
        """
        rectangle(self.coord_a[0], self.coord_a[1],
                  self.coord_b[0], self.coord_b[1],
                  color_ext, color_int, self.border
                  )
        if text != "":
            dimension = (abs(self.coord_a[0] - self.coord_b[0]),
                         abs(self.coord_a[1] - self.coord_b[1])
                         )
            font_size = get_font_size(text, dimension, font)
            texte(dimension[0] // 2, dimension[1] // 2,
                  text, color_ext, "c", font,
                  font_size
                  )

    def overlay(self,
                text: str,
                color_int: str = "",
                color_ext: str = "#000000",
                font_size: int = 24
                ):
        """
        fonction pour afficher un texte en overlay au dessus du bouton
        """
        dim_overlay = taille_texte(text, "Helvetica", font_size)
        gap_x = dim_overlay[0] // 2
        gap_y = dim_overlay[1] // 2
        coord_x, coord_y = abscisse_souris(), ordonnee_souris()
        rectangle((coord_x - gap_x, coord_y - dim_overlay),
                  (coord_x + gap_x, coord_y),
                  color_ext,
                  color_int,
                  tag="overlay"
                  )
        texte(coord_x,
              coord_y - gap_y,
              text,
              "c",
              taille_texte=font_size,
              tag="overlay"
              )


    def is_hover(self):
        """
        Fonction détectant le passage de la souris au-dessus
        """
        if self.coord_a[0] <= self.coord_b[0]:
            test_x = self.coord_a[0] <= abscisse_souris() <= self.coord_b[0]
        else:
            test_x = self.coord_b[0] <= abscisse_souris() <= self.coord_a[0]
        if self.coord_a[1] <= self.coord_b[1]:
            test_y = self.coord_a[1] <= ordonnee_souris() <= self.coord_b[1]
        else:
            test_y = self.coord_b[1] <= ordonnee_souris() <= self.coord_a[1]
        if test_x and test_y:
            return True
        return False

    def is_pressed(self, event):
        """
        Fonction détectant un clique effectué sur le bouton
        """
        if self.is_hover():
            if type_ev(event) == 'ClicGauche':
                return True
        return False


class ButtonRectTex:
    pass

class ButtonCircle:
    pass

class ButtonCircleTex:
    pass

class Text:
    pass

class SliderBar:
    pass