import smtplib
import requests
import os
import datetime
from voice_assistant import talk

# Fonction pour envoyer un email
def envoyer_email(destinataire, contenu):
    try:
        email_utilisateur = os.getenv('EMAIL_USER')  # Récupérer l'email depuis les variables d'environnement
        email_mdp = os.getenv('EMAIL_PASS')
        serveur = smtplib.SMTP('smtp.gmail.com', 587)
        serveur.ehlo()
        serveur.starttls()
        serveur.login(email_utilisateur, email_mdp)
        serveur.sendmail(email_utilisateur, destinataire, contenu)
        serveur.close()
        print("L'email a été envoyé avec succès.")
        talk("L'email a été envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")
        talk("Désolé, je n'ai pas pu envoyer l'email.")

# Fonction pour récupérer la météo
def obtenir_meteo(ville):
    api_key = os.getenv('WEATHER_API_KEY')  # Récupérer la clé API depuis les variables d'environnement
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&lang=fr"
    donnees_meteo = requests.get(base_url).json()

    if donnees_meteo['cod'] != '404':
        main = donnees_meteo['main']
        description_meteo = donnees_meteo['weather'][0]['description']
        temperature = main['temp'] - 273.15
        humidite = main['humidity']
        return f"Température: {temperature:.2f}°C\nHumidité: {humidite}%\nDescription: {description_meteo}"
    else:
        return "Ville non trouvée"

# Fonction pour saluer l'utilisateur
def souhaiter_bienvenue():
    heure = int(datetime.datetime.now().hour)
    if 0 <= heure < 12:
        talk("Bonjour !")
    elif 12 <= heure < 18:
        talk("Bon après-midi !")
    else:
        talk("Bonsoir !")
    talk("Je suis votre assistant. Comment puis-je vous aider ?")

if __name__ == "__main__":
    souhaiter_bienvenue()
    ville = "Paris"  # Exemple, tu peux demander à l'utilisateur la ville
    meteo = obtenir_meteo(ville)
    print(meteo)
    talk(meteo)