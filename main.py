import speech_recognition as sr
import sys
import webbrowser

def talk(words):
    print(words)

talk('Привет, спроси меня что-нибудь')

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Говорите')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio).lower()
        print(f"Вы сказали: {zadanie}")
    except sr.UnknownValueError:
        talk('Я вас не поняла')
        zadanie = command()

    return zadanie

def makeTask(zadanie):
    if 'open website' in zadanie or 'open yandex' in zadanie:
        talk('Открываю Яндекс')
        url = 'https://yandex.ru'
        webbrowser.open(url)
    elif 'stop' in zadanie:
        talk('Заканчиваю работу')
        sys.exit()
    elif 'open vk' in zadanie:
        talk('Открываю сайт Вконатке')
        url = 'https://vk.com'
        webbrowser.open(url)

if 'start' in input():
    makeTask(command())