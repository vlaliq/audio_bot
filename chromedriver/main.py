import multiprocessing
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from py_audio_test import simulate_user as simulate_pyaudio
from py_game_test import simulate_user as simulate_pygame

url = "https://vks-dev.o-code.ru/active_conference/?roomId=TESTROOM"

if __name__ == '__main__':
    print('Выберите дальнейшее действие:')
    choice = input("Введите 1, чтобы запустить pyaudio-бота\n"
                   "Введите 2, чтобы запустить pygame-бота\n"
                   "Введите 3, чтобы запустить одновременно pyaudio-бота и pygame-бота:\n")
    if choice == '1':
        kol = int(input("Введите количество ботов pyaudio: "))
        processes = []
        for i in range(kol):
            surname = "audio"
            name = "volo"
            patronymic = str(i)
            user = {'surname': surname, 'name': name, 'patronymic': patronymic}
            process = multiprocessing.Process(target=simulate_pyaudio,
                                              args=(user['surname'], user['name'], user['patronymic'], url))
            processes.append(process)
            process.start()
        for process in processes:
            process.join()

    elif choice == '2':
        kol = int(input("Введите количество ботов pygame: "))
        processes = []
        for i in range(kol):
            surname = "game"
            name = "volo"
            patronymic = str(i)
            user = {'surname': surname, 'name': name, 'patronymic': patronymic}
            process = multiprocessing.Process(target=simulate_pygame,
                                              args=(user['surname'], user['name'], user['patronymic'], url))
            processes.append(process)
            process.start()
        for process in processes:
            process.join()

    elif choice == '3':
        kol = int(input("Введите количество ботов: "))
        processes = []
        for i in range(kol):
            surname1 = "audio"
            surname2 = "game"
            name = "volo"
            patronymic = str(i)
            user1 = {'surname1': surname1, 'name': name, 'patronymic': patronymic}
            user2 = {'surname2': surname2, 'name': name, 'patronymic': patronymic}
            if i % 2 == 0:
                process = multiprocessing.Process(target=simulate_pyaudio,
                                                  args=(user1['surname1'], user1['name'], user1['patronymic'], url))
            else:
                process = multiprocessing.Process(target=simulate_pygame,
                                                  args=(user2['surname2'], user2['name'], user2['patronymic'], url))
            processes.append(process)
        for process in processes:
            process.start()
        for process in processes:
            process.join()
    else:
        print("Некорректный ввод")
        exit()