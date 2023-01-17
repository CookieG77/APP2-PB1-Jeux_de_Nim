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
            ligne[0].pop(i[1])
            plateau_temp[i[0]] = ligne
            


test = JdNim([7,5,3,1])
test.del_elements([(0,0),(1,0),(0,3)])
print(test.plateau)