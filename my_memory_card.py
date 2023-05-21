#создай приложение для запоминания информации
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QRadioButton, 
    QGroupBox, QVBoxLayout, QHBoxLayout, QButtonGroup
)

from random import shuffle

app =QApplication([])
window = QWidget()

lbl_question = QLabel('Сколько месяцев в году имеют 28 дней?')
rbtn_1 = QRadioButton('Ни один')
rbtn_2 = QRadioButton('Два')
rbtn_3 = QRadioButton('Все')
rbtn_4 = QRadioButton('Один')

btn = QPushButton('Ответить')
answer = QGroupBox('Ответы')
result = QGroupBox('Результат')
lbl_result = QLabel('Вы ответили правильно')
lbl_right_answer = QLabel('Все')

btn_group = QButtonGroup()
btn_group.addButton(rbtn_1)
btn_group.addButton(rbtn_2)
btn_group.addButton(rbtn_3)
btn_group.addButton(rbtn_4)

v_result = QVBoxLayout()
v_result.addWidget(lbl_result)
v_result.addWidget(lbl_right_answer)

result.setLayout(v_result)
result.hide()

v_nain = QVBoxLayout()
h_nain_1 = QHBoxLayout()
h_nain_2 = QHBoxLayout()
h_nain_3 = QHBoxLayout()

h_grpbox = QHBoxLayout()
v_grpbox_1 = QVBoxLayout()
v_grpbox_2 = QVBoxLayout()

h_nain_1.addWidget(lbl_question)
h_nain_2.addWidget(answer)
h_nain_2.addWidget(result)
h_nain_3.addWidget(btn)

v_nain.addLayout(h_nain_1)
v_nain.addLayout(h_nain_2)
v_nain.addLayout(h_nain_3)

v_grpbox_1.addWidget(rbtn_1)
v_grpbox_1.addWidget(rbtn_2)
v_grpbox_2.addWidget(rbtn_3)
v_grpbox_2.addWidget(rbtn_4)

h_grpbox.addLayout(v_grpbox_1)
h_grpbox.addLayout(v_grpbox_2)

answer.setLayout(h_grpbox)

buttons = [rbtn_1,rbtn_2, rbtn_3, rbtn_4]

class question:
    def __init__(self, question, right, wront_1, wront_2, wront_3):
        self.question = question
        self.right = right
        self.wront_1 = wront_1
        self.wront_2 = wront_2
        self.wront_3 = wront_3

cur_question = 0
questions = [
    question('Сколько ннн?', '10', '100', '300', '5'),
    question('Сколько rrr?', '10', '100', '300', '5'),
    question('Сколько ppp?', '10', '100', '300', '5'),
    question('Сколько yyy?', '10', '100', '300', '5')
]

def ask(_q):
    shuffle(buttons)
    buttons[0].setText(_q.right)
    buttons[1].setText(_q.wront_1)
    buttons[2].setText(_q.wront_2)
    buttons[3].setText(_q.wront_3)
    lbl_question.setText(_q.question)
    lbl_right_answer.setText(_q.right)
    show_shototam()

def show_result():
    answer.hide()
    result.show()
    btn.setText('Следующий вопрос')

def next_question():
    global cur_question
    cur_question += 1
    if cur_question >= len(questions):
        cur_question =0
    ask(questions[cur_question])

def show_shototam():
    answer.show()
    result.hide()
    btn.setText('Ответить')
    btn_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    btn_group.setExclusive(True)

def click_shototam():
    if btn.text() == 'Ответить':
        show_result()
    else:
        next_question()
btn.clicked.connect(click_shototam)

window.setLayout(v_nain)
window.show()
app.exec()