# modules/commands.py
import webbrowser
import wikipedia
from modules.speech_to_text import listen
from modules.text_to_speech import speak

wikipedia.set_lang("pt")

def process_command(command):
    if "wikipédia" in command:
        speak("O que você quer pesquisar na Wikipedia?")
        topic = listen()
        print(f'pegou {topic}')
        if topic:
            speak(f"Você escolheu: {topic}")
        else:
            topic = input("Digite o termo: ")
        summary = wikipedia.summary(topic, sentences=2)
        speak(summary)
    elif "youtube" in command:
        speak("Abrindo o YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "farmácia" in command:
        speak("Buscando farmácias próximas...")
        webbrowser.open("https://www.google.com/maps/search/farmácia+próxima")
    else:
        speak("Desculpe, não entendi o comando.")
