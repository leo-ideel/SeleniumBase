# mon_fichier.py
import sys

# Récupère le message envoyé depuis GitHub Actions
if len(sys.argv) < 2:
    print("Pas de message reçu !")
    sys.exit(1)

message = sys.argv[1]

# Ici tu peux faire ce que tu veux avec le message
print(f"Beaugosse vive le aaah, tu as envoyé : {message}")
