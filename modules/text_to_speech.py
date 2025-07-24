# modules/text_to_speech.py
import pyttsx3
import time

def speak(text):
    try:
        print('iniciando speaker')
        engine = pyttsx3.init()
        time.sleep(1)
        print(f'frase para falar: {text}')
        engine.say(text)
        time.sleep(4)
        engine.runAndWait()
        time.sleep(1)
    except Exception as ex_:
        print(f"validar erro speak: {ex_}")

#TEST TO VALIDATE
# test_txt = "Testando o texto escrito para fala"
# speak(test_txt)