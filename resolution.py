

import numpy as np

def debit(v_max, c_max, C_ligne):
    """
    Calcule les débits aux différentes positions à un instant donné en utilisant le modèle de Greenshield.

    Arguments :
    v_max -- Vitesse maximale (en mètres par seconde)
    c_max -- Concentration maximale (en véhicules par mètre)
    C_ligne -- Tableau contenant les concentrations à un instant donné

    Retourne :
    Q -- Tableau contenant les débits (en véhicules par seconde) aux différentes positions
    """
    Q = np.zeros_like(C_ligne)
    for j in range(len(C_ligne)):
        v = v_max * (1 - C_ligne[j] / c_max)
        Q[j] = C_ligne[j] * v
    return Q

def C_depart(dx, d1, d2, c1, c2, C):
    """
    Initialise la première ligne du tableau C correspondant à t = 0.

    Arguments :
    dx -- Pas d'espace (en mètres)
    d1 -- Distance où la concentration passe de c1 à c2 (en mètres)
    d2 -- Distance où la concentration revient de c2 à c1 (en mètres)
    c1 -- Concentration initiale la plus faible (en véhicules par mètre)
    c2 -- Concentration initiale la plus forte (en véhicules par mètre)
    C -- Tableau 2D des concentrations à initialiser

    Retourne :
    C -- Tableau 2D initialisé
    """
    n1 = int(d1 / dx)
    n2 = int(d2 / dx)
    
    for j in range(C.shape[1]):
        if j <= n1 or j >= n2:
            C[0, j] = c1
        else:
            C[0, j] = c2
            
    return C

def resolution(C, dt, dx, c_max, v_max):
    """
    Résout l'équation de continuité et remplit le tableau C.

    Arguments :
    C -- Tableau 2D des concentrations à remplir
    dt -- Pas de temps (en secondes)
    dx -- Pas d'espace (en mètres)
    c_max -- Concentration maximale (en véhicules par mètre)
    v_max -- Vitesse maximale (en mètres par seconde)

    Retourne :
    C -- Tableau 2D rempli au cours de la résolution
    """
    nbr_points_temps, nbr_points_espace = C.shape
    
    for i in range(nbr_points_temps - 1):
        Q = debit(v_max, c_max, C[i, :])
        
        for j in range(nbr_points_espace):
            j_plus_1 = (j + 1) % nbr_points_espace  # Condition aux limites périodiques
            C[i + 1, j] = C[i, j] - (dt / dx) * (Q[j_plus_1] - Q[j])
    
    return C

# Exemple d'utilisation (avec des valeurs fictives)
L_a = 1000  # Longueur de l'autoroute en mètres
T_emps = 3600  # Durée de simulation en secondes
dx = 10  # Pas d'espace en mètres
dt = 1  # Pas de temps en secondes
c_max = 0.1  # Concentration maximale en véhicules par mètre
v_max = 30  # Vitesse maximale en mètres par seconde

# Initialisation du tableau C
nbr_points_espace = int(L_a / dx) + 1
nbr_points_temps = int(T_emps / dt) + 1
C = np.zeros((nbr_points_temps, nbr_points_espace))

# Initialisation de la première ligne du tableau C
C = C_depart(dx, 200, 800, 0.02, 0.08, C)

# Résolution de l'équation et remplissage du tableau C
C = resolution(C, dt, dx, c_max, v_max)

# Affichage des résultats pour vérification
print(C)
