# Step 1: Installer la bibliothèque gTTS
!pip install gTTS

# Step 2: Importer
from gtts import gTTS

# Step 3: Texte à lire
texte = "Bonjour, je m'appelle Almoujiz. Je vais vous apprendre le TTS en Python."
langue = "fr"  # 'ar' pour arabe, 'en' pour anglais

# Step 4: Créer l'objet TTS
tts = gTTS(text=texte, lang=langue)

# Step 5: Enregistrer le fichier
tts.save("tts_output.mp3")

# Step 6: Lecture audio dans Colab
from IPython.display import Audio
Audio("tts_output.mp3")
