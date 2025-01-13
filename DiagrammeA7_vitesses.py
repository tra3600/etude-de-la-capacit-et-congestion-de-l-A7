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

# Exemple d'utilisation avec des données fictives
# q_exp et v_exp sont des vecteurs numpy contenant les débits et vitesses mesurés
q_exp = np.array([1000, 1500, 2000, 2500, 3000, 3500, 4000])
v_exp = np.array([100, 90, 80, 70, 60, 50, 40])

trace(q_exp, v_exp)