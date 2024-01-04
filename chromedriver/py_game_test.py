from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from pygame import mixer
import multiprocessing

driver_path = "C:\\Users\\User\\Desktop\\audio_vks_bot\\chromedriver\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
service = Service(driver_path)

def simulate_user(surname_input, name_input, patronymic_input, url):
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(url=url)
        driver.implicitly_wait(5)

        #поиск и заполнение поля "Фамилия"
        surname = driver.find_element(By.XPATH, "//input[@placeholder='Фамилия']")
        surname.clear()
        surname.send_keys(surname_input)
        driver.implicitly_wait(5)

        # поиск и заполнение поля "Имя"
        name = driver.find_element(By.XPATH, "//input[@placeholder='Имя']")
        name.clear()
        name.send_keys(name_input)
        driver.implicitly_wait(5)

        # поиск и заполнение поля "Отчество"
        patronymic = driver.find_element(By.XPATH, "//input[@placeholder='Отчество']")
        patronymic.clear()
        patronymic.send_keys(patronymic_input)
        driver.implicitly_wait(5)

        # нажатие кнопки входа
        login_button = driver.find_element(By.XPATH, "//span[contains(text(),'Войти')]")
        login_button.click()
        time.sleep(3)

        #поиск и нажатие кнопки камеры
        camera_button = driver.find_element(By.CLASS_NAME, "vks-cam")
        camera_button.click()
        driver.implicitly_wait(5)

        # поиск и нажатие кнопки микрофона
        # mic_button = driver.find_element(By.CLASS_NAME, "vks-mic")
        # mic_button.click()
        # time.sleep(20)

        # Заменеите 'deti-online.com_-_kniga-1-glava-1.wav' на ваш аудиофайл
        mixer.init(devicename = 'CABLE Input (VB-Audio Virtual Cable)') # Инициализация с корректным инпутом
        mixer.music.load("YOUR_AUDIO.wav") # Загрузка аудиофайла
        time.sleep(5)
        mixer.music.play()

        while mixer.music.get_busy():
            time.sleep(1)

    except Exception as ex:
        print(ex)
    finally:
        try:
            driver.close()
            driver.quit()
        except NameError:
            pass