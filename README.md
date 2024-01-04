# audio_vks_bot
# Назначение этой программы - тестирование веб-приложения для видеоконференций VKS.

Программа имеет 3 файла: main, py_audio_test.py и py_game_test.py. Они находятся в папке chromedriver.

Перед запуском поменяйте путь driver_path в файлах py_game_test.py и py_audio_test.py.
Если захотите запустить другой аудиофайл на воспроизведение, то он должен иметь расширение .wav 
(ну или скачайте mp3 файл и найдите какой-нибудь конвертер в браузере), затем добавьте его в директорию chromedriver
и измените название воспроизводимого файла в py_audio_test.py и py_game_test.py

Чтобы начать работу запустите файл main. В нем же находится url тестовой комнаты vks (при необходимости можете изменить url прямо в main).

Данные реализации работают с браузером Chrome.
Сначала вам нужно установить соответствующие драйверы для своей версии Chrome и разместить их в директории chromedriver
(ссылка на драйвер:https://chromedriver.storage.googleapis.com/index.html).

Основное отличие py_audio_test.py и py_game_test.py заключается в разных методах воспроизведения звука.  
Воспроизводимый файл должен находиться в директории chromedriver вместе с main.py, py_audio_test.py и py_game_test.py


py_audio_test.py для воспроизведения звука использует библиотеку pyaudio. Сама реализация:

	# Открываем mp3 файл для чтения
        with wave.open('YOUR_AUDIO.wav', 'rb') as audio_file: //замените на свой аудио файл

            # Инициализируем PyAudio
            p = pyaudio.PyAudio()

            # Открываем поток для проигрывания аудио
            stream = p.open(format=p.get_format_from_width(audio_file.getsampwidth()),
                            channels=audio_file.getnchannels(),
                            rate=audio_file.getframerate(),
                            output=True)

            # Читаем данные из mp3 файла и проигрываем их через поток
            data = audio_file.readframes(1024)
            while data:
                stream.write(data)
                data = audio_file.readframes(1024)

            # Останавливаем поток и закрываем PyAudio
            stream.stop_stream()
            stream.close()
            p.terminate()

py_game_test.py в свою очередь использует библиотеку pygame и заранее скаченный виртуальный аудио кабель
(ссылка на виртуальный аудио кабель: https://vb-audio.com/Cable/)
После установки виртуального аудиокабеля вам нужно будет открыть настройки звука на вашем компьютере и выставить
Cable INPUT и Cable OUTPUT устройствами воспроизведения и записи по-умолчанию. 
Данные настройки никак не повлияют на работу py_audio_test.py.
Сама реализация воспроизведения звука:
 	
	mixer.init(devicename = 'CABLE Input (VB-Audio Virtual Cable)') # Инициализация с корректным инпутом
        mixer.music.load("YOUR_AUDIO.wav") # Загрузка аудиофайла (замените на свой аудиофайл)
        time.sleep(5)
        mixer.music.play()