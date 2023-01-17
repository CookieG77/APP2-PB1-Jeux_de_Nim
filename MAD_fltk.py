"""
Menu ADdon fltk
"""

from fltk import*

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

def get_font_size(text: str, dimension: tuple, police: str = "Helvetica"):
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
    ) -> None:
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
             police: str = "Helvetica"

    ) -> None:
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
            font_size = get_font_size(text, dimension, police)
            texte(dimension[0] // 2, dimension[1] // 2,
                  text, color_ext, "c", police,
                  font_size
                  )

    def is_hover(self):
        """
        Fonction du passage de la souris au-dessus
        """
    pass


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