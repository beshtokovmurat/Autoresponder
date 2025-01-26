#Объяснение кода
#    Импорт библиотек: Импортируем необходимые модули из Kivy и библиотеки gTTS.
#    Создание интерфейса: Используем BoxLayout для размещения элементов интерфейса — метки, текстового поля и кнопки.
#    Воспроизведение текста: При нажатии на кнопку play_text программа проверяет введенное число и воспроизводит соответствующий текст, используя gTTS для генерации аудиофайла и playsound для его воспроизведения.
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from gtts import gTTS
import os
import playsound

kivy.require('2.0.0')

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text='Введите номер (1-3) для воспроизведения текста:')
        self.layout.add_widget(self.label)

        self.input_text = TextInput(multiline=False)
        self.layout.add_widget(self.input_text)

        self.button = Button(text='Воспроизвести')
        self.button.bind(on_press=self.play_text)
        self.layout.add_widget(self.button)

        return self.layout

    def play_text(self, instance):
        number = self.input_text.text

        # Заготовленный текст
        texts = {
            '1': 'Привет! Как дела?',
            '2': 'Вы находитесь на эфире. Что вас интересует?',
            '3': 'Спасибо, что позвонили!'
        }

        if number in texts:
            tts = gTTS(text=texts[number], lang='ru')
            tts.save("output.mp3")
            playsound.playsound("output.mp3")
        else:
            self.label.text = 'Неверный номер. Пожалуйста, введите 1, 2 или 3.'

if __name__ == '__main__':
    MyApp().run()
