import subprocess
import os

# Pfad zum Verzeichnis mit den Skripten
directory = r"C:\Users\jonas\OneDrive\Desktop\Own_comc\today"

# Liste der Skripte, die ausgeführt werden sollen
scripts = [
    "1scrape.py",
    "2(a)analyze.py",
    "remove.py",
    "3url_generator.py",
    "4fertigen.py",
    "5compare_values.py"
]

# Gehe in das Verzeichnis mit den Skripten
os.chdir(directory)

# Führt jedes Skript nacheinander aus
for script in scripts:
    if os.path.exists(os.path.join(directory, script)):
        try:
            print(f"Starte {script}...")
            subprocess.run(["python", script], check=True)
            print(f"{script} beendet.\n")
        except subprocess.CalledProcessError as e:
            print(f"Fehler beim Ausführen von {script}: {e}")
            break
    else:
        print(f"Das Skript {script} wurde nicht gefunden. Bitte überprüfen.")
        break

print("Skript-Ausführung beendet.")
