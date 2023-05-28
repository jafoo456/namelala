from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton,  QPushButton, QLabel)

class Question():
    def __init__(self, question, r_a, false1, false2, false3):
        self.question = question
        self.r_a = r_a
        self.false1 = false1
        self.false2 = false2
        self.false3 = false3
        
s_v = []
quest1 =  Question('999+1', '1000', '9991', '998', '1001')
s_v.append(quest1)
quest2 =  Question('ты кто', 'я', 'никто', 'не знаю', 'владимир')
s_v.append(quest2)
quest3 =  Question('вопрос', 'ответ', 'не ответ', '.', 'не знаю')
s_v.append(quest3)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.move(0,0)
window.resize(400, 300)

q_1 = QLabel('Cамый сложный вопрос в мире')
RadioGroupBox = QGroupBox('Bарианты ответа:')
qrbutton1 = QRadioButton('Вариант 1')
qrbutton2 = QRadioButton('Вариант 2')
qrbutton3 = QRadioButton('Вариант 3')
qrbutton4 = QRadioButton('Вариант 4')

layout_ans1 = QVBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans1.addWidget(qrbutton1)
layout_ans1.addWidget(qrbutton2)
layout_ans2.addWidget(qrbutton3)
layout_ans2.addWidget(qrbutton4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

ansGroupBox = QGroupBox('Результаты теста:')
lb_result = QLabel('прав ты или нет?')
lb_correct = QLabel('ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_correct)

ansGroupBox.setLayout(layout_res)

button_ok = QPushButton('Ответить')
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_card = QVBoxLayout()

layout_line1.addWidget(q_1)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(ansGroupBox)
ansGroupBox.hide()
layout_line3.addWidget(button_ok)
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
window.setLayout(layout_card)

def show_result():
    RadioGroupBox.hide()
    ansGroupBox.show()
    button_ok.setText('Следующий вопрос')
def show_question():
    ansGroupBox.hide()
    RadioGroupBox.show()
    button_ok.setText('Ответить')
    button_group = QButtonGroup()
    button_group.addButton(qrbutton1)
    button_group.addButton(qrbutton2)
    button_group.addButton(qrbutton3)
    button_group.addButton(qrbutton4)

    button_group.setExclusive(False)
    qrbutton1.setChecked(False)
    qrbutton2.setChecked(False)
    qrbutton3.setChecked(False)
    qrbutton4.setChecked(False)
    button_group.setExclusive(True)
    







answers = [qrbutton1, qrbutton2, qrbutton3, qrbutton4]
shuffle(s_v)
def ask():
    global asked_questions
    asked_questions += 1
    if asked_questions == len(s_v):
        asked_questions -= 1
        print('Процент правильных ответов', score/asked_questions*100)

    ask_questions =  s_v[asked_questions]
    
    shuffle(answers)
    answers[0].setText(ask_questions.r_a)
    answers[1].setText(ask_questions.false1)
    answers[2].setText(ask_questions.false2)
    answers[3].setText(ask_questions.false3)

    q_1.setText(ask_questions.question)
    lb_correct.setText(ask_questions.r_a)

    show_question()

def check_answer():
    if answers[0].isChecked():
        global score
        score+=1
        lb_result.setText('Верно')
        show_result()
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        lb_result.setText('Неверно')
        show_result()

def click_ok():
    if button_ok.text() == 'Ответить':
        check_answer()
    else:
        ask()


score = 0
asked_questions = -1
ask()
button_ok.clicked.connect(click_ok)
window.show()
app.exec_()



