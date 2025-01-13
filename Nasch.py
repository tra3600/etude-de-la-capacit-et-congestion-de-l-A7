import numpy as np

def resolution_lax_friedrichs(C, dt, dx, c_max, v_max):
    """
    Résout l'équation de continuité en utilisant le schéma de Lax-Friedriechs et remplit le tableau C.

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
        
        for j in range(1, nbr_points_espace - 1):
            C[i + 1, j] = 0.5 * (C[i, j-1] + C[i, j+1]) - (dt / (2 * dx)) * (Q[j+1] - Q[j-1])
    
    # Conditions aux limites périodiques
    C[i+1, 0] = 0.5 * (C[i, -1] + C[i, 1]) - (dt / (2 * dx)) * (Q[1] - Q[-1])
    C[i+1, -1] = 0.5 * (C[i, -2] + C[i, 0]) - (dt / (2 * dx)) * (Q[0] - Q[-2])
    
    return C


def debit_regression(a0, a1, a2, a3, C_ligne):
    """
    Calcule les débits aux différentes positions à un instant donné en utilisant la régression d'ordre 3.

    Arguments :
    a0, a1, a2, a3 -- Coefficients de la régression pour le diagramme fondamental
    C_ligne -- Tableau contenant les concentrations à un instant donné

    Retourne :
    Q -- Tableau contenant les débits (en véhicules par seconde) aux différentes positions
    """
    Q = np.zeros_like(C_ligne)
    for j in range(len(C_ligne)):
        c = C_ligne[j]
        Q[j] = a3 * c**3 + a2 * c**2 + a1 * c + a0
    return Q


def resolution_regression(C, dt, dx, a0, a1, a2, a3):
    """
    Résout l'équation de continuité en utilisant la régression d'ordre 3 pour le diagramme fondamental et remplit le tableau C.

    Arguments :
    C -- Tableau 2D des concentrations à remplir
    dt -- Pas de temps (en secondes)
    dx -- Pas d'espace (en mètres)
    a0, a1, a2, a3 -- Coefficients de la régression pour le diagramme fondamental

    Retourne :
    C -- Tableau 2D rempli au cours de la résolution
    """
    nbr_points_temps, nbr_points_espace = C.shape
    
    for i in range(nbr_points_temps - 1):
        Q = debit_regression(a0, a1, a2, a3, C[i, :])
        
        for j in range(1, nbr_points_espace - 1):
            C[i + 1, j] = 0.5 * (C[i, j-1] + C[i, j+1]) - (dt / (2 * dx)) * (Q[j+1] - Q[j-1])
    
    # Conditions aux limites périodiques
    C[i+1, 0] = 0.5 * (C[i, -1] + C[i, 1]) - (dt / (2 * dx)) * (Q[1] - Q[-1])
    C[i+1, -1] = 0.5 * (C[i, -2] + C[i, 0]) - (dt / (2 * dx)) * (Q[0] - Q[-2])
    
    return C