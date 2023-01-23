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
        self.dimension = (abs(self.coord_a[0] - self.coord_b[0]),
                         abs(self.coord_a[1] - self.coord_b[1])
                         )

    def draw(self,
             color_int: str = "",
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
            font_size = get_font_size(text, self.dimension, font)
            texte(self.dimension[0] // 2, self.dimension[1] // 2,
                  text, color_ext, "c", font,
                  font_size
                  )

    def set_picture(self, path: str):
        """
        Permet d'afficher le bouton avec une image
        """
        image(self.coord_a[0],
              self.coord_a[1],
              path,
              self.dimension[0],
              self.dimension[1],
              "nw"
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
        rectangle(coord_x - gap_x, coord_y - dim_overlay[1],
                  coord_x + gap_x, coord_y,
                  color_ext, color_int,
                  tag="overlay"
                  )
        texte(coord_x,
              coord_y - gap_y,
              text,
              color_ext,
              "c",
              taille=font_size,
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

    def is_pressed(self,
                   event
                   ):
        """
        Fonction détectant un clique effectué sur le bouton
        """
        if self.is_hover():
            if type_ev(event) == 'ClicGauche':
                return True
        return False


class ButtonRectTex:
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
        self.dimension = (abs(self.coord_a[0] - self.coord_b[0]),
                         abs(self.coord_a[1] - self.coord_b[1])
                         )

    def draw(self, path: str):
        """
        Permet d'afficher le bouton avec une image
        """
        image(self.coord_a[0],
              self.coord_a[1],
              path,
              self.dimension[0],
              self.dimension[1],
              "nw"
              )

    def overlay(self,
                color: str = "#000000",
                border: int = 1
                ):
        """
        fonction pour afficher un texte en overlay au dessus du bouton
        """
        rectangle(self.coord_a[0], self.coord_a[1],
                  self.coord_b[0], self.coord_b[1],
                  color, epaisseur=border,
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

    def is_pressed(self,
                   event
                   ):
        """
        Fonction détectant un clique effectué sur le bouton
        """
        if self.is_hover():
            if type_ev(event) == 'ClicGauche':
                return True
        return False


class ButtonCircle:
    """
    Classe permettant la création d'un
    bouton de forme circulaire
    """
    def __init__(self,
                 coord: tuple,
                 ray: int,
                 border: int
                 ):
        """
        Initialisation du bouton
        """
        self.coord = coord
        self.ray = ray
        self.border = border

    def draw(self,
             color_int: str = "",
             color_ext: str = "#000000",
             text: str = "",
             font: str = "Helvetica"
             ):
        """
        Fonction pour afficher le bouton
        """
        cercle(self.coord[0], self.coord[1],
               self.ray, color_ext, color_int,
               self.border
               )
        if text != "":
            dimension = (self.ray * 2 + 1,
                         self.ray * 2 + 1
                         )
            font_size = get_font_size(text, dimension, font)
            texte(self.coord[0], self.coord[1],
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
        rectangle(coord_x - gap_x, coord_y - dim_overlay[1],
                  coord_x + gap_x, coord_y,
                  color_ext, color_int,
                  tag="overlay"
                  )
        texte(coord_x,
              coord_y - gap_y,
              text,
              color_ext,
              "c",
              taille=font_size,
              tag="overlay"
              )

    def is_hover(self):
        """
        Fonction détectant le passage de la souris au-dessus
        """
        mouse_x = abscisse_souris()
        mouse_y = ordonnee_souris()
        distance = ((self.coord[0] - mouse_x) ** 2 +
                    (self.coord[1] - mouse_y) ** 2) ** 0.5
        if distance <= self.ray:
            return True
        return False

    def is_pressed(self,
                   event
                   ):
        """
        Fonction détectant un clique effectué sur le bouton
        """
        if self.is_hover():
            if type_ev(event) == 'ClicGauche':
                return True
        return False


class ButtonCircleTex:
    """
    Classe permettant la création d'un
    bouton de forme circulaire avec du texte
    """
    pass

class Text:
    """
    Classe permettant l'apparition d'un texte
    """
    def __init__(self,
                 coord_a: tuple,
                 coord_b: tuple,
                 text: str
                 ):
        """
        Initialisation du texte
        """
        self.coord_a = coord_a
        self.coord_b = coord_b
        self.text = text

    def draw(self,
             color: str = "#000000",
             font: str = "Helvetica",
             font_size: int = None
             ):
        """
        Fonction permettant l'affichage du texte
        """
        coord_x = (self.coord_a[0] + self.coord_b[0]) // 2
        coord_y = (self.coord_a[1] + self.coord_b[1]) // 2
        font_size = get_font_size(self.text,
                                      (abs(self.coord_a[0] - self.coord_b[0]),
                                       abs(self.coord_a[1] - self.coord_b[1])),
                                      font
                                      )
        texte(coord_x,
              coord_y,
              self.text,
              color,
              'c',
              font,
              font_size
              )


class SliderBar:
    """
    Classe permettant la création d'un
    slider.
    """
    pass
