import speech_recognition as sr

def record_volume():
    r = sr.recognizers()

    with sr.Microphone(device_index = 1) as source:
        print("Слушаю.....")
        audio = r.listen(source)
    query = r.recognize_google(audio, language='ru-RU')
    f = open('exzamole.txt' , 'w')
    f.write(query.lower())
    f.close()


record_volume()

