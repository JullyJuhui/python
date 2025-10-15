import speech_recognition as sr

with sr.Microphone() as soure:
    print('듣고 있어요...')
    audio = sr.Recognizer().listen(soure)

text = sr.Recognizer().recognize_google(audio, language='ko')
print(text)