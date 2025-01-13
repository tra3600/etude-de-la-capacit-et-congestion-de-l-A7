import numpy as np
import matplotlib.pyplot as plt

def trace(q_exp, v_exp):
    """
    Trace le diagramme fondamental (débit vs concentration) pour les données fournies.

    Arguments:
    q_exp -- Vecteur des débits (en véhicules par heure)
    v_exp -- Vecteur des vitesses (en kilomètres par heure)
    """
    # Calcul de la concentration
    c_exp = q_exp / v_exp

    # Tracé du nuage de points
    plt.plot(c_exp, q_exp, 'o', label="Points de mesure")
    plt.xlabel("Concentration (véhicule / km)")
    plt.ylabel("Débit (véhicule / h)")
    plt.title("Diagramme fondamental (c_exp, q_exp)")
    plt.legend()
    plt.grid(True)
    plt.show()

""""
# Exemple d'utilisation avec des données fictives
# q_exp et v_exp sont des vecteurs numpy contenant les débits et vitesses mesurés
q_exp = np.array([1000, 1500, 2000, 2500, 3000, 3500, 4000])
v_exp = np.array([100, 90, 80, 70, 60, 50, 40])

trace(q_exp, v_exp)
"""


def congestion(v_exp):
    nbmesures = len(v_exp)
    for i in range(nbmesures):
        v = v_exp[i]
        j = i
        while 0 < j and v < v_exp[j-1]:
            v_exp[j] = v_exp[j-1]  # ligne à compléter
            j = j-1                # ligne à compléter
        v_exp[j] = v
    return v_exp[nbmesures // 2]


import numpy as np

# Paramètres de discrétisation
L_a = 1000  # Longueur de l'autoroute en mètres
T_emps = 3600  # Durée de simulation en secondes
dx = 10  # Pas d'espace en mètres
dt = 1  # Pas de temps en secondes

# Calcul des dimensions
nbr_points_espace = int(L_a / dx) + 1
nbr_points_temps = int(T_emps / dt) + 1

# Initialisation du tableau C
C = np.zeros((nbr_points_temps, nbr_points_espace))

# Affichage des dimensions du tableau
print("Dimensions de C :", C.shape)