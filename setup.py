import os

# Installe toutes les dépendances nécessaires
def install_dependencies():
    os.system('pip install pyttsx3 speechrecognition wikipedia gtts playsound pyaudio requests wolframalpha selenium')

if __name__ == "__main__":
    install_dependencies()
    print("Toutes les dépendances sont installées.")
