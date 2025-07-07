
from gtts import gTTS
from IPython.display import Audio

texte = "مرحبا، هذا هو الدرس الرابع في سلسلة تحويل النص إلى كلام"
langue = "ar"

# أخذ اسم الملف من المستخدم
filename = input("ادخل اسم الملف الصوتي (مثلاً: mon_audio.mp3): ")
if not filename.endswith(".mp3"):
    filename += ".mp3"

# إنشاء الملف الصوتي وحفظه
tts = gTTS(text=texte, lang=langue)
tts.save(filename)
print(f"تم حفظ الملف الصوتي باسم {filename}")

# تشغيل الملف الصوتي داخل Jupyter أو Colab
Audio(filename)
