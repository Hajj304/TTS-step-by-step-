# تثبيت المكتبة (في حال العمل على Google Colab)
# !pip install gTTS

from gtts import gTTS
from IPython.display import Audio

texte = "السلام عليكم، هذا هو الدرس الأول في تعلم تحويل النص إلى صوت باستخدام Python."
langue = "ar"  # 'ar' للعربية, 'fr' للفرنسية, 'en' للإنجليزية

tts = gTTS(text=texte, lang=langue)
tts.save("lesson1_output.mp3")

print("تم إنشاء الملف الصوتي lesson1_output.mp3")
Audio("lesson1_output.mp3")
