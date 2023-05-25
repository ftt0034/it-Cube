import speech_recognition as sr
import os
def record_volume():
    r = sr.Recognizer()

    with sr.Microphone(device_index = 1)as source:
        print('Слушаю и Записываю......')
        audio = r.listen(source)

    query = r.recognize_google(audio, language= 'ru-Ru')
    print(f'Вы сказали: {query.lower()}')
    f = open('exp.txt', 'w+')
    f.write(query)
    f.close()
    if 'открой' or 'открой пожалуйста' or 'сизам открой' and  'блокнот' in query:
        os.system('C:/Windows/System32/notepad')
    elif 'открой' or 'открой пожалуйста' or 'сизам открой' and  'калькулятор' in query:
        os.system('C:/Windows/System32/calc')
    

record_volume()

