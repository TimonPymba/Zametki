#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import json

#Интерфейс

app = QApplication([])

window = QWidget()

text = QTextEdit()

widget = QListWidget()
widget1 = QListWidget()

Nad = QLabel("Список заметок")
Nad1 = QLabel("Список тегов")

line1 = QLineEdit("Введите тег...")

button = QPushButton("Искать заметки по тегу")
button1 = QPushButton("Открепить от заметки")
button2 = QPushButton("Добавить к заметке")
button3 = QPushButton("Сохранить заметку")
button4 = QPushButton("Удалить заметку")
button5 = QPushButton("Создать заметку")

layout = QVBoxLayout()
layout1 = QVBoxLayout()

layout2 = QHBoxLayout()

layout1.addWidget(Nad)
layout1.addWidget(widget1)
layout1.addWidget(button5)
layout1.addWidget(button4)
layout1.addWidget(button3)
layout1.addWidget(Nad1)
layout1.addWidget(widget)
layout1.addWidget(line1)
layout1.addWidget(button2)
layout1.addWidget(button1)
layout1.addWidget(button)
layout.addWidget(text)

layout2.addLayout(layout)
layout2.addLayout(layout1)

window.setLayout(layout2)

#Открытие файла

with open("data.json", "r", encoding = "UTF-8") as file:
    data = json.load(file)
widget1.addItems(data)

#Открытие заметок

def show_notes():
    key = widget1.selectedItems()[0].text()
    text.setText(data[key]["текст"])
    widget.clear()
    widget.addItems(data[key]["теги"])

#Сохранение заметок

def save_notes():
    if widget1.selectedItems():
        key = widget1.selectedItems()[0].text()
        data[key]["текст"] = text.toPlainText()
        with open("data.json", "w", encoding = "UTF-8") as file:
            json.dump(data,file,ensure_ascii=False)
    else:
        print("Заметка не выбрана")

#Удаление заметок

def del_notes():
    if widget1.selectedItems():
        key = widget1.selectedItems()[0].text()
        del data[key]
        widget.clear()
        widget1.clear()
        text.clear()
        widget1.addItems(data)
        with open("data.json", "w", encoding = "UTF-8") as file:
            json.dump(data,file,ensure_ascii=False)
    else:
        print("Заметка не выбрана")

#Создание заметок

def cre_notes():






widget1.itemClicked.connect(show_notes)
button3.clicked.connect(save_notes)
button4.clicked.connect(del_notes)

window.show()
app.exec()