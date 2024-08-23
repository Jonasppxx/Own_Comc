import os
import subprocess
from datetime import datetime

# Pfad zum Repository
repo_path = r"C:\Users\jonas\OneDrive - bwd 365\Privat\Visual Studio\Own_Comc"

def run_git_command(command):
    result = subprocess.run(
        ["git", "-C", repo_path] + command,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Fehler bei '{' '.join(command)}': {result.stderr}")
    return result

# Überprüfen, ob es Änderungen gibt
status_result = run_git_command(["status", "--porcelain"])

if status_result.stdout:
    print("Änderungen erkannt. Füge hinzu, committe und pushe...")

    # Füge alle Änderungen hinzu
    run_git_command(["add", "."])

    # Erstelle eine Commit-Nachricht mit dem aktuellen Datum und Uhrzeit
    commit_message = f"Automatischer Commit am {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    run_git_command(["commit", "-m", commit_message])

    # Pushe die Änderungen zu GitHub
    push_result = run_git_command(["push", "origin", "main"])

    if push_result.returncode == 0:
        print("Änderungen erfolgreich gepusht.")
    else:
        print("Fehler beim Pushen der Änderungen.")
else:
    print("Keine Änderungen erkannt.")