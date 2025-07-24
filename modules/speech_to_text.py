# modules/speech_to_text.py
import time
import speech_recognition as sr

def listen():
    time.sleep(1)
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale algo...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", text)
        return text.lower()
    except sr.UnknownValueError:
        return "Não entendi o que você disse."
    except sr.RequestError:
        return "Erro ao conectar com o serviço de reconhecimento."


#TEST TO VALIDATE
# listen()