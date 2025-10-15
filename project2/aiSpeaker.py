import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from scrapping import weather, exchange, stock

#문자를 소리로 출력(gtts)
def speak(text):
    print('[AI] ' + text)
    tts = gTTS(text=text, lang='ko')
    file_name = 'data/voice.mp3'
    tts.save(file_name)
    playsound(file_name)

    if os.path.exists(file_name):  #말하고 없애기
        os.remove(file_name)

#음성을 듣고 문자로 출력(sr)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        # if '종료' in text:
        #     print('종료합니다.')
        #     stop(wait_for_stop=False)  #마이크 종료
        #     os._exit(0)
        print('[서주희] ' + text)
        answer(text)

    except sr.UnknownValueError:
        print('인식 실패')
    except sr.RequestError:
        print('요청 실패')

#문자를 입력받아 인공지능이 대답
def answer(text):
    answer_text = ''
    if '종료' in text:
        answer_text = '다음에 또 만나요.'
        speak(answer_text)

        stop(wait_for_stop=False)  #마이크 종료
        os._exit(0)  #프로그램 종료

    elif '안녕' in text:
        answer_text = '안녕하세요! 반갑습니다.'

    elif '날씨' in text:
        index = text.find('날씨')
        query = text[:index]
        temp = weather(query)
        answer_text = f'{query}의 {temp}'

    elif '환율' in text:
        rate = exchange()
        answer_text = f'1달러 환율은 {rate}원 입니다.'

    elif '주식' in text:
        index = text.find('주식')
        query = text[:index + 2]
        price = stock(query)
        answer_text = f'{query}의 가격은 {price}원 입니다.'

    else:
        answer_text = '다시 한번 말씀해 주시겠어요?'

    speak(answer_text)

speak('무엇을 도와드릴까요?')

mic = sr.Microphone()
stop = sr.Recognizer().listen_in_background(mic, listen)

while True:
    pass