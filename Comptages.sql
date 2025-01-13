import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('autoroute_A7.db')
cursor = conn.cursor()

# Q1. Obtenir les données de comptage pour la station M8B
query_q1 = """
SELECT id_comptage, date, voie, q_exp, v_exp
FROM COMPTAGES
JOIN STATIONS ON COMPTAGES.id_station = STATIONS.id_station
WHERE STATIONS.nom = 'M8B';
"""
cursor.execute(query_q1)
comptages_m8b = cursor.fetchall()

# Affichage des résultats de la requête Q1
print("Données de comptage pour la station M8B:")
for row in comptages_m8b:
    print(row)

# Créer une nouvelle table COMPTAGES_M8B pour stocker les résultats de la requête Q1
cursor.execute("DROP TABLE IF EXISTS COMPTAGES_M8B;")
cursor.execute("""
CREATE TABLE COMPTAGES_M8B (
    id_comptage INTEGER,
    date INTEGER,
    voie INTEGER,
    q_exp REAL,
    v_exp REAL
);
""")
cursor.executemany("INSERT INTO COMPTAGES_M8B VALUES (?, ?, ?, ?, ?);", comptages_m8b)
conn.commit()

# Q2. Obtenir la somme des débits pour chaque date
query_q2 = """
SELECT date, SUM(q_exp) AS total_q_exp
FROM COMPTAGES_M8B
GROUP BY date;
"""
cursor.execute(query_q2)
sum_q_exp_per_date = cursor.fetchall()

# Affichage des résultats de la requête Q2
print("\nSomme des débits pour chaque date:")
for row in sum_q_exp_per_date:
    print(row)

# Fermeture de la connexion à la base de données
conn.close()