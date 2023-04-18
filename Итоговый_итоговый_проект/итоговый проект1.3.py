
#библиотеки
#библиотека для распознания голоса - SpeechRecognition и еще одна библиотека это PyAudio - для работы с микрофоном
import speech_recognition as sr
import os
def record_volume():
    r = sr.Recognizer()
    #это нужно для того  чтобы программа знала откуда идет звук
    with sr.Microphone(device_index = 1) as source:
        print("Слушаю.....")
        audio = r.listen(source)
    #тут происходит распознание голоса через Google Web Speech API + язык
    query = r.recognize_google(audio, language='ru-RU')
    #после распознания здесь можно добавить функции для их открытия
    if 'открой' or 'открыть' or 'открой пожалуйста'and 'калькулятор' in query:
        os.system('C:/Windows/System32/calc')
    elif 'открой' or 'открыть' or 'открой пожалуйста' and 'блокнот' in query:
        os.system('C:/Windows/System32/notepad')
record_volume()

