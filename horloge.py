import time

heure_actuelle = (0, 0, 0)
alarme = (0, 0, 0)
mode_affichage_24h = True
pause = False

def afficher_heure():
    global heure_actuelle
    global mode_affichage_24h

    if mode_affichage_24h:
        print(f"{heure_actuelle[0]:02d}:{heure_actuelle[1]:02d}:{heure_actuelle[2]:02d}")
    else:
        heure = heure_actuelle[0] if heure_actuelle[0] <= 12 else heure_actuelle[0] - 12
        am_pm = 'AM' if heure_actuelle[0] < 12 else 'PM'
        print(f"{heure:02d}:{heure_actuelle[1]:02d}:{heure_actuelle[2]:02d} {am_pm}")

def regler_heure(nouvelle_heure):
    global heure_actuelle
    heure_actuelle = nouvelle_heure

def regler_alarme(nouvelle_alarme):
    global alarme
    alarme = nouvelle_alarme

def mode_affichage(mode):
    global mode_affichage_24h
    mode_affichage_24h = mode

def mettre_en_pause():
    global pause
    pause = True

def relancer():
    global pause
    pause = False

while True:
    if not pause:
        afficher_heure()
        if heure_actuelle == alarme:
            print("Réveil !")
            # Ajoutez ici le code pour gérer l'alarme
            # Par exemple : jouer un son, afficher un message, etc.

        heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)
        if heure_actuelle[2] == 60:
            heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)
        if heure_actuelle[1] == 60:
            heure_actuelle = (heure_actuelle[0] + 1, 0, 0)
        if heure_actuelle[0] == 24:
            heure_actuelle = (0, 0, 0)

    time.sleep(1)  # Pause d'une seconde entre chaque actualisation de l'h