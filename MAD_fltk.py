"""
Menu ADdon fltk
"""

import fltk

class ButtonRect:
    """
    Classe permettant la création d'un
    bouton de forme rectangulaire
    """
    def __init__(self,
                 coord_a: tuple,
                 coord_b: tuple,
                 border: int = 1,
                 text: str = ""
    ) -> None:
        """
        Initialisation du bouton.
        """
        self.coord_a = coord_a
        self.coord_b = coord_b

    def draw(self,
             color_int: str,
             color_ext: str = "#000000"
    ) -> None:
        """
        Fonction pour afficher le bouton
        """

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