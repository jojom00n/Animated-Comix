import requests
import shutil
import re
import kivy
import eel
import os
import threading
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Установка пути к папке с шаблонами для Eel
eel.init('')

# Создание простого HTML-шаблона для вывода сообщения
html_template = """
<!doctype html>
<html>
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>My comics</title>
</head>

<body>
    <div class="container">
        <div class="parallax">
            <div class="parallax-layer layer1 land">
                <img src="imgs/%D1%84%D0%BE%D0%BD%20%D0%BD%D0%B5%D0%B1%D0%B0.png"/>
            </div>
            <div class="parallax-layer layer1 water">
                <img src="imgs/%D1%84%D0%BE%D0%BD%20%D0%B2%D0%BE%D0%B4%D1%8B.png"/>>
            </div>
            <div class="parallax-layer layer2 meteor">
                <img src="imgs/%D0%BC%D0%B5%D1%82%D0%B5%D0%BE%D1%80%D0%B8%D1%82.png"/>
            </div>
            <div class="parallax-layer layerdino dino">
                <img src="imgs/%D0%B4%D0%B8%D0%BD%D0%BE%D0%B7%D0%B0%D0%B2%D1%80%D1%8B.png"/>
            </div>
            <div class="parallax-layer layerham hamster">
                <img src="imgs/%D1%85%D0%BE%D0%BC%D1%8F%D0%BA.png"/>
            </div>
            <div class="parallax-layer layer2 wale">
                <img src="imgs/%D0%BA%D0%B8%D1%82.png"/>
            </div>
            <div class="parallax-layer layer3 grass2">
                <img src="imgs/%D1%82%D1%80%D0%B0%D0%B2%D0%B0.png"/>
            </div>
            <div class="parallax-layer layer3 grass1">
                <img src="imgs/%D1%82%D1%80%D0%B0%D0%B2%D0%B0.png"/>
            </div>
        </div>
    </div>
    <script src="js/script.js"></script>
</body></html>

"""

# Простой CSS-файл для стилизации HTML
css_template = """
::-webkit-scrollbar {
  width: 0;
}

*,
*::before,
*::after {
    padding: 0;
    margin: 0;
    border: 0;
    box-sizing: border-box;
}

a {
    text-decoration: none;
}

ul,
ol,
li {
    list-style: none;
}

img {
    vertical-align: top;
}

h1,
h2,
h3,
h4,
h5,
h6 {
    font-weight: inherit;
    font-size: inherit;
}

html,
body {
    height: 100%;
    line-height: 0;
    font-size: 16px;
    background-color: black;
}

.wrapper {
    min-height: 100%;
}

.container {
    max-width: 500px;
    margin: auto auto;
    padding: auto 200px;
    background-color: black
}

.parallax {
    height: 100vh;
    background-color: black;
    overflow-x: hidden;
    perspective: 1px;
}

.parallax-layer {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
}

.layer1 {
    transform: translateZ(-1px);
}

.layer2 {
    transform: translateZ(-1.35px);
}

.layer3 {
    transform: translateZ(-1.1px);
}

.layerham {
    transform: translateZ(-1.2px);
}

.layerdino {
    transform: translateZ(-1.35px);
}

/* specific to this implementation */
div {
    font-size: 50px;
    text-align: center;
}

.land {
    top: -400px;
    width: 100px;
    left: -300px;
}

.water {
    top: 3770px;
    width: 1000px;
    left: -300px;
}

.meteor {
    top: 30px;
    width: 00px;
    left: 20px;
    transform: scale(0.5);
}

.dino {
    top: 1150px;
    width: 1100px;
    left: -340px;
}

.hamster {
    top: 3000px;
    width: 1100px;
    left: -309px;
}

.wale {
    top: 4700px;
    left: 400px;
    transform: rotate(130deg) scale(0.3);

}

.grass1 {
    top: 2350px;
    width: 1100px;
    left: -309px;
}

.grass2 {
    top: 3400px;
    width: 1100px;
    left: -309px;
}

"""

# Функция для создания HTML файла
def create_html_file():
    with open('index.html', 'w') as f:
        f.write(html_template)

# Функция для создания CSS файла
def create_css_file():
    with open('styles.css', 'w') as f:
        f.write(css_template)

# Функция для создания папки imgs
def create_imgs_folder():
    if not os.path.exists('imgs'):
        os.makedirs('imgs')

# Функция для изменения заголовка в HTML файле
def change_title():
    with open('index.html', 'r') as f:
        html_content = f.read()
    
    # Создаем объект Beautiful Soup для парсинга HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Изменяем заголовок
    title_tag = soup.title
    title_tag.string = 'Thats all'
    
    # Сохраняем изменения в HTML файл
    with open('index.html', 'w') as f:
        f.write(str(soup))

# Функция для загрузки изображения и сохранения его в папке imgs
def download_image():
    url = 'https://ico.cppng.com/download/2117/rat_mouse_PNG23542.png'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # Открываем файл для бинарной записи
        with open('imgs/хомяк.png', 'wb') as f:
            response.raw.decode_content = True
            # Копируем данные из запроса в файл
            shutil.copyfileobj(response.raw, f)

# Функция для загрузки изображения с пк и сохранения его в папке imgs
def load_image_and_save():
    root = tk.Tk()
    root.withdraw()  # Скрыть основное окно

    # Показать диалоговое окно выбора файла и получить путь к выбранному файлу
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg; *.png; *.jpeg")])

    if file_path:
        # Определить расширение исходного файла
        file_extension = os.path.splitext(file_path)[1]

        # Путь для сохранения файла с новым именем "хомяк" и тем же расширением
        destination_path = os.path.join("imgs", "хомяк" + file_extension)

        # Копировать выбранный файл в папку imgs
        shutil.copyfile(file_path, destination_path)

        # Вернуть путь к сохраненному файлу
        return destination_path
    else:
        return None

# Функция для загрузки изображения и сохранения его в папке imgs
def download_image():
    # Загрузить изображение и сохранить его
    image_path = load_image_and_save()

    if image_path:
        print("Изображение успешно загружено и сохранено:", image_path)
    else:
        print("Изображение не выбрано или не сохранено.")


# Определение функции, которая будет вызываться при нажатии на кнопку в Kivy
def on_button_click():
    create_html_file()
    create_css_file()
    create_imgs_folder()

# Определение функции, которая будет вызываться при нажатии на кнопку "Открыть HTML"
def open_html():
    eel.start('index.html', size=(300, 200))

# Создание интерфейса с помощью Kivy
class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Создание кнопки для создания HTML и CSS файлов
        create_files_button = Button(text='Создать HTML и CSS файлы')
        create_files_button.bind(on_press=lambda x: on_button_click())
        
        # Создание кнопки для открытия HTML файла
        open_html_button = Button(text='Открыть HTML')
        open_html_button.bind(on_press=lambda x: threading.Thread(target=open_html).start())
        
        # Создание кнопки для изменения заголовка в HTML файле
        change_title_button = Button(text='Изменить заголовок в HTML')
        change_title_button.bind(on_press=lambda x: change_title())

        # Создание кнопки для загрузки изображения
        download_image_button = Button(text='Скачать изображение')
        download_image_button.bind(on_press=lambda x: download_image())


        # Добавление кнопок на экран
        layout.add_widget(create_files_button)
        layout.add_widget(open_html_button)
        layout.add_widget(change_title_button)
        layout.add_widget(download_image_button)

        return layout

# Запуск приложения
if __name__ == '__main__':
    # Запуск приложения Kivy
    MyApp().run()
