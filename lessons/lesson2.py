"""
✅ الدرس 2: تحويل نصوص متعددة دفعة واحدة
- استخدام قائمة من الجمل
- توليد ملف صوتي لكل جملة تلقائياً
"""

from gtts import gTTS
from IPython.display import Audio

# قائمة من الجمل التي نريد تحويلها إلى صوت
texts = [
    "السلام عليكم",
    "هذا هو الدرس الثاني",
    "تحويل عدة نصوص إلى صوت تلقائياً"
]

langue = "ar"  # لغة النطق: العربية

# تحويل كل جملة في القائمة إلى ملف صوتي وحفظه
for i, txt in enumerate(texts, 1):
    tts = gTTS(text=txt, lang=langue)
    filename = f"lesson2_output_{i}.mp3"
    tts.save(filename)
    print(f"تم حفظ الملف الصوتي {filename}")

# تشغيل أول ملف صوتي كمثال (في Google Colab أو Jupyter)
Audio("lesson2_output_1.mp3")
