from gtts import gTTS
from IPython.display import Audio

# نصوص باللغتين العربية والفرنسية
texts = {
    "ar": "مرحباً بكم في درس دعم اللغة العربية والفرنسية",
    "fr": "Bienvenue dans la leçon sur la prise en charge des langues arabe et française"
}

# تحويل النصوص إلى ملفات صوتية وحفظها
for lang, txt in texts.items():
    tts = gTTS(text=txt, lang=lang)
    filename = f"lesson3_output_{lang}.mp3"
    tts.save(filename)
    print(f"تم حفظ الملف الصوتي {filename}")

# تشغيل ملف الصوت العربي كمثال
Audio("lesson3_output_ar.mp3")
