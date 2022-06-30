# Author: Lim Hong Yong
# UI config
import os.path
import sys

import pandas as pd
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from urllib.request import urlopen
import json
import pandas
import random

with urlopen("https://opentdb.com/api.php?amount=50&category=9&difficulty=medium&type=multiple") as webpage:
    data = json.loads(webpage.read().decode())
    # convert to dataframe
    df = pd.DataFrame(data["results"])
    print(df.columns)


def preload_data(index):
    #category = df["category"][index]
    difficulty = df["difficulty"][0]
    question = df["question"][index]
    correct = df["correct_answer"][index]
    incorrect = df["incorrect_answers"][index]

    # Check in terminal
    print(question)
    print("Difficulty: " + difficulty)
    print("Answer:" + correct)

    # list of tuples for correction of bad question formatting
    text_to_format = [
        ("&#039;", "'"),
        ("&'", "'"),
        ("&quot;", '"'),
        ("&lt;", "<"),
        ("&gt;", ">"),
        ("&ldquo;", '"'),
        ("&rdquo;", '"')
    ]

    # reformat bad characters from string data and saves into vars to be appended into parameters dictionary
    for tuple in text_to_format:
        question = question.replace(tuple[0], tuple[1])
        correct = correct.replace(tuple[0], tuple[1])

    for tuple in text_to_format:
        incorrect = [char.replace(tuple[0], tuple[1]) for char in incorrect]

    # adds correctly formatted data into parameters
    parameters["question"].append(question)
    parameters["correct"].append(correct)
    parameters["difficulty"].append(difficulty)

    # incorrect var contains 'list' data type, hence correct must be converted into a list also
    all_ans = incorrect + [correct]
    random.shuffle(all_ans)
    print(all_ans)  # print all_ans for unit testing

    # to implement for loop for number of questions imported from JSON API
    # appends shuffled choices into dictionary
    parameters["answer1"].append(all_ans[0])
    parameters["answer2"].append(all_ans[1])
    parameters["answer3"].append(all_ans[2])
    parameters["answer4"].append(all_ans[3])


parameters = {
    "question": [],
    "difficulty": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "correct": [],
    "score": [],
    "index": []
}

# Dictionary for storing widgets as key and value pairs
widgets = {
    "empty_space": [],
    "logos": [],
    "buttons": [],
    "score": [],
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "message": [],
    "message2": [],
    "leaderboard_button": [],
    "settings_button": [],
    "achievements_button": [],
    "instructions_button": []
}

# initialise GUI app
app = QApplication(sys.argv)
# initialise grid layout
grid = QGridLayout()

# windows settings
window = QWidget()
window.setWindowTitle("Gami-ccount: Gamified System for Accounting Learning")
window.setWindowIcon(QtGui.QIcon("gami-ccount_icon.png"))
window.setFixedWidth(1000)
window.setFixedHeight(900)
window.move(20, 20)
window.setStyleSheet("background:'Black';")


# Function for image resize to x and y px ratio
def resize_image(src, x, y):
    pixmap = QtGui.QPixmap(src)
    # Automatically resizes to max size available
    pixmap_scaled = pixmap.scaled(x, y, QtCore.Qt.KeepAspectRatio)
    return pixmap_scaled


# function for creating button widgets
def create_buttons(answer, l_margin, r_margin):
    btn = QPushButton(answer)
    btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    btn.setFixedWidth(470)
    btn.setStyleSheet(
        "*{margin-left:" + str(l_margin) + "px;" +
        " margin-right:" + str(r_margin) + "px;" +
        '''
        border: 4px solid'#7FFF00';
        border-radius: 12px;
        font-family: 'Arial';     
        font-size: 16px;
        color: 'white';
        padding: 5px 0;
        margin-top: 5px;}
        *:hover{
            background:'#32CD32';
            font-weight: bold;
            color: 'yellow';
        }
        '''
    )
    btn.clicked.connect(lambda x: is_correct(btn))
    return btn

def create_start_buttons(placeholder_text):
    btn = QPushButton(placeholder_text)
    btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    # btn.setFixedWidth(300)
    btn.setStyleSheet(
        '''
        *{  
            font: 'Georgia';
            border: 1px solid 'GREEN';
            border-radius: 12px;
            font-size: 30px;
            color: 'white';
            padding: 5px ;
            margin: 0px 300px;
            }
        *:hover{
                background:'green';
                color:'black';
                font-weight:1200;
                font-size: 35px;  
            }
        '''
    )

    if placeholder_text == "Leaderboard":
        btn.clicked.connect(leaderboard)
    elif placeholder_text == "Settings":
        btn.clicked.connect(settings)
    elif placeholder_text == "Achievements":
        btn.clicked.connect(achievements)
    elif placeholder_text == "Instructions":
        btn.clicked.connect(instructions)
    else:
        pass  # do nothing
    return btn


def settings():
    print("Settings Frame")


def leaderboard():
    print("Leaderboard Frame")


def achievements():
    print("Achievement Frame")


def instructions():
    print("Instructions Frame")

def is_correct(btn):
    if btn.text() == parameters["correct"][-1]:
        print(btn.text() + " is correct!")

        temp_score = parameters["score"][-1]
        parameters["score"].pop()
        parameters["score"].append(temp_score + 10)  # adds 10 score everytime answered correctly
        # generates subsequent random question
        parameters["index"].pop()
        parameters["index"].append(random.randint(0, 49))
        preload_data(parameters["index"][-1])
        widgets["score"][-1].setText("Score: " + str(parameters["score"][-1]))
        widgets["question"][0].setText(parameters["question"][-1])
        widgets["answer1"][0].setText(parameters["answer1"][-1])
        widgets["answer2"][0].setText(parameters["answer2"][-1])
        widgets["answer3"][0].setText(parameters["answer3"][-1])
        widgets["answer4"][0].setText(parameters["answer4"][-1])

        # wins the round if score is 100
        if parameters["score"][-1] == 100:
            clear_widgets()
            win_game()

    else:  # wrong answer chosen.
        clear_widgets()
        defeat_screen()


# Function to clear widgets from global dictionary, vital to avoid UI truncates and abnormalities!
def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:  # if not an empty list, remove current widget
            widgets[widget][-1].hide()

        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


def clear_parameters():
    for param in parameters:
        if parameters[param] != []:
            for i in range(0, len(parameters[param])):
                parameters[param].pop()
    # after cleaing parameters, re-populate the 2 vital parameters
    parameters["index"].append(random.randint(0, 49))
    parameters["score"].append(0)


def start_game():
    clear_widgets()
    clear_parameters()
    # Test
    # parameters["score"].append(90)
    preload_data(parameters["index"][-1])
    frame2()


def menu():
    # display Gamiccount menu logo
    logo = QLabel()
    logo.setPixmap(resize_image("main-logo.png", 500, 300))
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet('''
            margin-top: 50px;
            margin-bottom: 5px;
    ''')
    widgets["logos"].append(logo)

    # button Widgets
    btn_start = QPushButton("Start Gami-ccount")
    btn_start.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    btn_start.setStyleSheet(
        '''        
        *{  
            font: 'Georgia';
            border: 1px solid 'GREEN';
            border-radius: 12px;
            font-size: 30px;
            color: 'white';
            padding: 5px ;
            margin: 0px 300px;
            }
        *:hover{
                background:'green';
                color:'yellow';
                font-weight:1200;
                font-size: 35px;   
            }
        '''
    )
    btn_start.clicked.connect(start_game)
    widgets["buttons"].append(btn_start)

    btn_leaderboard = create_start_buttons("Leaderboard")
    widgets["leaderboard_button"].append(btn_leaderboard)

    btn_settings = create_start_buttons("Settings")
    widgets["settings_button"].append(btn_settings)

    btn_achievements = create_start_buttons("Achievements")
    widgets["achievements_button"].append(btn_achievements)

    btn_instructions = create_start_buttons("Instructions")
    widgets["instructions_button"].append(btn_instructions)

    # empty/placeholder space in bottom
    empty_space = QPushButton("")
    empty_space.setStyleSheet(
        '''
            background: 'green';
            margin-top: 100px;
        ''')
    empty_space.setMinimumHeight(200)
    widgets["empty_space"].append(empty_space)


    # place inside Global Variable Dictionary of Widgets
    grid.addWidget(widgets["logos"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["buttons"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["leaderboard_button"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["settings_button"][-1], 3, 0, 1, 2)
    grid.addWidget(widgets["achievements_button"][-1], 4, 0, 1, 2)
    grid.addWidget(widgets["instructions_button"][-1], 5, 0, 1, 2)
    grid.addWidget(widgets["empty_space"][-1], 6, 0, 1, 2)

def return_to_menu():
    clear_widgets()
    clear_parameters()
    menu()


def frame2():
    # ************Score placement***************
    score = QLabel("Score: " + str(parameters["score"][-1]))
    score.setAlignment(QtCore.Qt.AlignRight)
    score.setStyleSheet(
        '''
        font-family: 'Georgia';
        font-size: 25px;
        color: '#32CD32';
        padding: 1px;
        margin: 5px;
        '''
    )
    widgets["score"].append(score)

    # ************Question placement***************
    question = QLabel(parameters["question"][-1])  # Prints Question randomly from dictionary
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        '''
        font-family: 'Georgia';
        background: 'white';
        border: 1px solid 'White';
        font-size:  25px;
        color: 'black';
        margin-top: 10px;
        margin-bottom: 10px;
        margin-left: 30px;
        margin-right: 30px;
        padding: 25px;
        '''
    )
    widgets["question"].append(question)

    # **************Logo Placement***************
    logo_bottom = QLabel()
    logo_bottom.setPixmap(resize_image("logo_bottom_formatted.png", 300, 300))
    logo_bottom.setAlignment(QtCore.Qt.AlignCenter)
    logo_bottom.setStyleSheet("margin-top: 75px; margin-bottom: 100px;")
    widgets["logos"].append(logo_bottom)

    # ***************Button Creation**************
    btn1 = create_buttons(parameters["answer1"][-1], 0, 0)
    btn2 = create_buttons(parameters["answer2"][-1], 0, 0)
    btn3 = create_buttons(parameters["answer3"][-1], 0, 0)
    btn4 = create_buttons(parameters["answer4"][-1], 0, 0)

    widgets["answer1"].append(btn1)
    widgets["answer2"].append(btn2)
    widgets["answer3"].append(btn3)
    widgets["answer4"].append(btn4)

    # place buttons on the grid
    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 3, 0)
    grid.addWidget(widgets["answer3"][-1], 2, 1)
    grid.addWidget(widgets["answer4"][-1], 3, 1)
    grid.addWidget(widgets["logos"][-1], 4, 0, 1, 2)


def win_game():
    # congratulations widget
    message = QLabel("You did good!\nYou are a natural accountant!\nYour Score Is:")
    message.setAlignment(QtCore.Qt.AlignCenter)
    message.setStyleSheet(
        '''
        font-family: 'Georgia';
        font-size: 25px;
        color: 'white';
        margin: 50px 0px;
        '''
    )
    widgets["message"].append(message)

    # score widget placement
    score = QLabel(str(parameters["score"][-1]))
    score.setStyleSheet(
        '''
        font-family: 'Georgia';
        font-size: 150px;
        color: 'White';
        margin-top:0px;
        margin-bottom: 25px; 
        '''
    )
    widgets["score"].append(score)

    # bid goodbye widget placement
    bye_message = QLabel("You are a cut above average!")
    bye_message.setAlignment(QtCore.Qt.AlignCenter)
    bye_message.setStyleSheet(
        "font-family: 'Georgia'; font-size: 20px; color: 'white'; margin: 5pxpx 100px;"
    )
    bye_message.setWordWrap(True)
    widgets["message2"].append(bye_message)

    # Retry button widget
    retry_btn = QPushButton('TRY AGAIN?')
    retry_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    retry_btn.clicked.connect(return_to_menu)
    retry_btn.setStyleSheet(
        '''*{
            text-family: Garamond;
            padding: 25px 0px;
            background: '#BC006C';
            color: 'white';
            font-family: 'Georgia';
            font-size: 35px;
            border-radius: 30px;
            margin: 0px 325px;
        }
        *:hover{
                background: QLinearGradient(x1:0, y1:0,
                                            x2:1, y2:0,
                                            stop: 0 #ea9714,
                                            stop: 1 #9ed228);
                font-size: 45px;
                color: 'white';
        }'''
    )
    widgets["buttons"].append(retry_btn)

    # Bottom Logo widget
    logo_bottom = QLabel()
    logo_bottom.setPixmap(resize_image("logo_bottom_formatted.png", 300, 300))
    logo_bottom.setAlignment(QtCore.Qt.AlignCenter)
    logo_bottom.setStyleSheet("margin-top: 30px; margin-bottom: 30px;")
    widgets["logos"].append(logo_bottom)

    # place widgets on the grid
    grid.addWidget(widgets["message"][-1], 2, 0)
    grid.addWidget(widgets["score"][-1], 2, 1)
    grid.addWidget(widgets["message2"][-1], 3, 0, 1, 2)
    grid.addWidget(widgets["buttons"][-1], 4, 0, 1, 2)
    grid.addWidget(widgets["logos"][-1], 5, 0, 1, 2)


def defeat_screen():
    # consolation message
    message = QLabel("Yikes, that was awful.\nFinal score is:")
    message.setWordWrap(True)
    message.setAlignment(QtCore.Qt.AlignRight)
    message.setStyleSheet(
        "font-family: 'Georgia'; font-size: 35px; color: 'white'; margin: 130px 0px; padding:0px;"
    )
    widgets["message"].append(message)

    # score widget placement
    score = QLabel(str(parameters["score"][-1]))
    score.setAlignment(QtCore.Qt.AlignLeft)
    score.setStyleSheet("font-size: 250px; color: white; margin: 0px 0px;")
    widgets["score"].append(score)

    # Retry button widget
    retry_btn = QPushButton("STUDY MORE\n" + "and" + "\nTRY AGAIN!")
    retry_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    retry_btn.clicked.connect(return_to_menu)
    retry_btn.setStyleSheet(
        '''*{
            text-family: Garamond;
            padding: 25px 0px;
            background: '#BC006C';
            color: 'white';
            font-family: 'Georgia';
            font-size: 35px;
            border-radius: 30px;
            margin: 0px 250px;
        }
        *:hover{
                background: QLinearGradient(x1:0, y1:0,
                                            x2:1, y2:0,
                                            stop: 0 #ea9714,
                                            stop: 1 #9ed228);
                font-size: 25px;
                color: 'black';
        }'''
    )

    # solid colour when you hover above Retry button
    #   *:hover{
    #             background: '#ff1b9e';
    #     }'''
    #     )

    widgets["buttons"].append(retry_btn)

    # Bottom Logo widget
    logo_bottom = QLabel()
    logo_bottom.setPixmap(resize_image("logo_bottom_formatted.png", 300, 300))
    logo_bottom.setAlignment(QtCore.Qt.AlignCenter)
    logo_bottom.setStyleSheet("margin-top: 30px; margin-bottom: 30px;")
    widgets["logos"].append(logo_bottom)

    # place widgets on the grid
    grid.addWidget(widgets["message"][-1], 1, 0)
    grid.addWidget(widgets["score"][-1], 1, 1)
    grid.addWidget(widgets["buttons"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["logos"][-1], 3, 0, 1, 2)


# *********Unit Tests***********
menu()
# start_game()
# ***********************

window.setLayout(grid)

window.show()
sys.exit(app.exec())  # terminate app
