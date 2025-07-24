# 🤖 Assistente Virtual com Python (Bootcamp DIO)

Projeto desenvolvido como desafio prático do bootcamp da DIO, com foco em **Processamento de Linguagem Natural (PLN)** utilizando Python. O objetivo foi criar um sistema de assistência virtual capaz de:

- Reconhecer fala (speech to text)
- Responder em voz (text to speech)
- Executar comandos por voz (como abrir YouTube, consultar Wikipedia e buscar farmácias próximas)

---

## 📌 Funcionalidades

✅ Reconhecimento de fala em português  
✅ Resposta em voz utilizando síntese de texto  
✅ Execução de comandos automatizados:
- Consultar informações na Wikipedia
- Abrir o YouTube no navegador
- Buscar farmácias próximas no Google Maps

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- Python 3.10+
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [Wikipedia](https://pypi.org/project/wikipedia/)
- webbrowser (biblioteca padrão do Python)

---

## 🧱 Estrutura do Projeto

```
virtual-assistant/
├── main.py                         # Script principal
├── modules/
│   ├── speech_to_text.py          # Reconhecimento de fala
│   ├── text_to_speech.py          # Fala sintetizada
│   └── commands.py                # Processamento e execução de comandos
├── requirements.txt               # Dependências do projeto
└── README.md                      # Este arquivo
```

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/romanozamoth/virtual-assistant-dio.git
cd virtual-assistant-dio
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o assistente

```bash
python main.py
```

---

## 📋 Requisitos Importantes

- Certifique-se de que seu microfone está funcionando.
- No Windows, `pyttsx3` costuma funcionar sem dependências extras.
- No Linux, pode ser necessário instalar o `espeak`:
  ```bash
  sudo apt install espeak
  ```

---

## 📚 Créditos e Referências

- [SpeechRecognition Docs](https://pypi.org/project/SpeechRecognition/)
- [Pyttsx3 Docs](https://pyttsx3.readthedocs.io/)
- [Wikipedia Python API](https://pypi.org/project/wikipedia/)
- Curso e desafio disponibilizados pela [Digital Innovation One](https://www.dio.me/)

---

## ✍️ Autor

**Thomaz Romano**  
Desenvolvido como parte do desafio do módulo **Processamento de Linguagem Natural com Python**.
