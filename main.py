import time
from modules.speech_to_text import listen
from modules.text_to_speech import speak
from modules.commands import process_command

if __name__ == "__main__":
    mode = "COMMAND"
    
    speak(f"Módulo selecionado: {mode}")
    
    if mode == "COMMAND":
        while True:
            time.sleep(0.5)
            comando = listen()
            time.sleep(0.5)
            if comando:
                process_command(comando)
    elif mode == "SPEECH":
        user_to_txt=""
        init_txt="Olá, fale algo para testar se eu compreendo"
        speak(init_txt)
        time.sleep(0.5)
        user_to_txt = listen()
        time.sleep(0.5)
        print(f'pegou {user_to_txt}')
        if user_to_txt:
            speak(f"Você disse a seguinte frase: {user_to_txt}")
        else:
            speak("Desculpe, não compreendi.")
        
    else:
        text_error="Módulo ainda não implementado"
        speak(text_error)
