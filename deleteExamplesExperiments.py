# ---- USE IN CASE WEB DELETE EXPERIMENT FUNCTION DOESN'T WORK ---- 

import sqlite3

DB_PATH = "db/WebLab.db"

# Change ID's for the ones you wanna remove
EXPERIMENT_IDS_TO_DELETE = [1, 2]  # ID 'dummy' and 'external-robot-movement'

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Delete experiment parameters
for exp_id in EXPERIMENT_IDS_TO_DELETE:
    cursor.execute("DELETE FROM ExperimentClientParameter WHERE experiment_id=?", (exp_id,))
    cursor.execute("DELETE FROM ExperimentInstance WHERE experiment_id=?", (exp_id,))
    cursor.execute("DELETE FROM UserUsedExperiment WHERE experiment_id=?", (exp_id,))

# Delete experiment
for exp_id in EXPERIMENT_IDS_TO_DELETE:
    cursor.execute("DELETE FROM Experiment WHERE id=?", (exp_id,))

conn.commit()
conn.close()

print(" Succesfully removed")
