import os
from playsound import playsound
import random
import speech_recognition

sr = speech_recognition.Recognizer()

commands_dict = {
    'commands':{
            'greeting': ['привет', 'добрый день', 'здравствуйте'],
            'play_music' : ['включи музыку', 'включи песню', 'включи трек'],
            'create_task' : ['добавь задание', 'добавь задачу'],
        }
}

def greeting():
    return "Здравствуйте. Я ваш голосовой помощник."


def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            return query
    except speech_recognition.UnknownValueError:
        return 'Речь не распознана'


def play_music():
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    print(f'Включаю {random_file.split("/")[-1]}')
    playsound(random_file)
    return 0

def find_out_the_weather():
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    print(f'Включаю {random_file.split("/")[-1]}')
    playsound(random_file)
    return 0

def create_task():
    print("Скажите, что мне добавить в список дел.")

    query = listen_command()

    with open('todo-list.txt', 'a') as file:
        file.write(f'{query}\n')

    return f'Задача {query} добавлена в todo-list!'


def main():
    query = listen_command()
    print(query)
    for a, b in commands_dict['commands'].items():
        if query in b:
            print(globals()[a]())



if __name__ == '__main__':
    main()