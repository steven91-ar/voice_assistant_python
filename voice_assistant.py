import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from selenium import webdriver

from module import envoyer_email

# Initialise le moteur de synthèse vocale
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Définit une voix féminine

# Fonction pour parler
def parler(texte):
    engine.say(texte)
    engine.runAndWait()

# Fonction pour écouter une commande
def ecouter_commande():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Écoute...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconnaissance en cours...")
        commande = r.recognize_google(audio, language='fr-FR')  # Utilisation de la reconnaissance vocale en français
        print(f"Vous avez dit : {commande}\n")
    except Exception as e:
        print("Veuillez répéter, s'il vous plaît...")
        return "None"
    return commande.lower()

# Fonction pour effectuer une recherche sur Internet avec Selenium
def recherche_internet(terme_recherche):
    # Configuration du WebDriver pour Microsoft Edge (ou Chrome)
    driver = webdriver.Edge(executable_path=r'C:\fichierinformatique\edgedriver\msedgedriver.exe')
    # Si tu utilises Chrome, utilise plutôt le chemin de chromedriver
    # driver = webdriver.Chrome(executable_path=r'C:\fichierinformatique\chromedriver.exe')

    # Effectuer une recherche sur Bing (ou Google)
    url_recherche = f"https://www.bing.com/search?q={terme_recherche}"  # Utilise Bing
    # url_recherche = f"https://www.google.com/search?q={terme_recherche}"  # Utilise Google si tu préfères
    driver.get(url_recherche)
    parler(f"Je recherche {terme_recherche} sur Internet.")

# Fonction pour saluer l'utilisateur
def souhaiter_bienvenue():
    heure = datetime.datetime.now().hour
    if 0 <= heure < 12:
        parler("Bonjour !")
    elif 12 <= heure < 18:
        parler("Bon après-midi !")
    else:
        parler("Bonsoir !")
    parler("Je suis votre assistant. Comment puis-je vous aider ?")

# Programme principal
if __name__ == "__main__":
    souhaiter_bienvenue()
    while True:
        commande = ecouter_commande()

        if 'wikipedia' in commande:
            parler('Recherche sur Wikipedia...')
            commande = commande.replace("wikipedia", "")
            resultats = wikipedia.summary(commande, sentences=2)
            parler(f"D'après Wikipedia : {resultats}")

        elif 'ouvrir youtube' in commande:
            webbrowser.open("https://www.youtube.com")

        elif 'ouvrir google' in commande:
            webbrowser.open("https://www.google.com")

        elif 'recherche sur internet' in commande:
            parler('Que voulez-vous rechercher sur Internet ?')
            terme_recherche = ecouter_commande().strip()  # Extrait le terme de recherche
            parler(f"Recherche de {terme_recherche} sur Internet.")
            recherche_internet(terme_recherche)

        elif 'joue de la musique' in commande:
            repertoire_musique = r'C:\Users\steve\Music'  # Assure-toi que ce chemin est correct
            chansons = os.listdir(repertoire_musique)
            if chansons:
                os.startfile(os.path.join(repertoire_musique, chansons[0]))
            else:
                parler("Aucune musique trouvée dans le répertoire.")

        elif 'quelle heure est-il' in commande:
            heure_actuelle = datetime.datetime.now().strftime("%H:%M:%S")
            parler(f"Il est {heure_actuelle}")

        elif 'email à' in commande:
            try:
                parler("Que dois-je dire ?")
                contenu = ecouter_commande()
                destinataire = "jamienay@outlook.fr"  # Adresse email du destinataire
                envoyer_email(destinataire, contenu)
                parler("L'email a été envoyé.")
            except Exception as e:
                parler("Désolé, je ne peux pas envoyer cet email.")
                print(e)

# Configuration du WebDriver pour Selenium
driver = webdriver.Edge(executable_path=r'C:\fichierinformatique\edgedriver\msedgedriver.exe')
driver.get('https://www.dominos.com')