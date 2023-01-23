"""
fichier secondaire contenant les classes nécessaire au fonctionnement du jeu
"""

class JdNim:
    """
    Classe permettant d'organiser les données du jeu de Nim.
    """
    def __init__(self,
                 orga: list
    ) -> None:
        """
        Initialisation de la classe.
        """
        self.plateau = []
        for i in orga:
            temp = []
            for j in range(i):
                temp.append(j)
            self.plateau.append([temp, i])
        self.dims = [0, len(self.plateau)]
        for coo_y in range(self.dims[1]):
            if self.plateau[coo_y][1] > self.dims[0]:
                self.dims[0] = self.plateau[coo_y][1]

    def load_save(self,
                  save: list[str, list]
    ) -> None:
        """
        Fonction permettant de charger une sauvegarde du jeu.
        """
        print(1)

    def del_elements(self,
                     selection: list
    ) -> None:
        """
        Fonction permettant de supprimer une selection d'objet (une liste).
        Chaques objet est représenté par un couple (x,y)
        """
        plateau_temp = self.plateau[:]
        for i in selection:
            ligne = plateau_temp[i[0]]
            ligne[0].remove(i[1])
            plateau_temp[i[0]] = ligne
