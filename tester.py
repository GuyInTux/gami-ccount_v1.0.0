# pop() function
# someshits = {"apple":5,
#              "king":10,
#              "queens":12}
#
# print(someshits)
# print("To pop:", someshits.pop("king"))
# print("What's left:", someshits)
#
# #reading key pair from a dictionary
# value = int(input("Key in a value pair:\n"))
#
# def get_key(value):
#     key_value = [k for k,v in someshits.items() if v== value]
#     print("The key of the value is:", key_value)
#     #returns all items within a dictionary (key and value pairs)
#
# get_key(value)

# *************************************************************
# Author: Lim Hong Yong
# tester file
import os.path
import sys

import pandas as pd
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QFileDialog, \
    QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from urllib.request import urlopen
import json
import pandas
import random
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# with urlopen("https://opentdb.com/api.php?amount=50&category=9&difficulty=medium&type=multiple") as webpage:
#     data = json.loads(webpage.read().decode())
#     # convert to dataframe
#     df = pd.DataFrame(data["results"])
#     print(df.columns)
# # =========
# parameters = {
#     "question": [],
#     "difficulty": [],
#     "answer1": [],
#     "answer2": [],
#     "answer3": [],
#     "answer4": [],
#     "correct": [],
#     "score": [],
#     "index": []
# }
#
# # Dictionary for storing widgets as key and value pairs
# widgets = {
#     "empty_space": [],
#     "logos": [],
#     "buttons": [],
#     "score": [],
#     "question": [],
#     "answer1": [],
#     "answer2": [],
#     "answer3": [],
#     "answer4": [],
#     "message": [],
#     "message2": [],
#     "leaderboard_button": [],
#     "settings_button": [],
#     "achievements_button": [],
#     "instructions_button": []
# }
# # =====
# # initialise GUI app
# app = QApplication(sys.argv)
# # initialise grid layout
# grid = QGridLayout()
#
# # windows settings
# window = QWidget()
# window.setWindowTitle("Gami-ccount: Gamified System for Accounting Learning")
# window.setWindowIcon(QtGui.QIcon("gami-ccount_icon.png"))
# window.setFixedWidth(1000)
# window.setFixedHeight(900)
# window.move(20, 20)
# window.setStyleSheet("background:'Black';")
#
#
# # =========EXECUTABLES
#
# def create_buttons(answer, l_margin, r_margin):
#     btn = QPushButton(answer)
#     btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
#     btn.setFixedWidth(485)
#     btn.setStyleSheet(
#         "*{margin-left:" + str(l_margin) + "px;" +
#         " margin-right:" + str(r_margin) + "px;" +
#         '''
#         border: 4px solid'#7FFF00';
#         border-radius: 12px;
#         font-family: 'shanti';
#         font-size: 16px;
#         color: 'white';
#         padding: 5px 0;
#         margin-top: 5px;}
#         *:hover{
#             background:'#32CD32'
#         }
#         '''
#     )
#     btn.clicked.connect(lambda x: is_correct(btn))
#     return btn
#
#
# def resize_image(src, x, y):
#     pixmap = QtGui.QPixmap(src)
#     # Automatically resizes to max size available
#     pixmap_scaled = pixmap.scaled(x, y, QtCore.Qt.KeepAspectRatio)
#     return pixmap_scaled
#
#
# def create_start_buttons(placeholder_text):
#     btn = QPushButton(placeholder_text)
#     btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
#     # btn.setFixedWidth(300)
#     btn.setStyleSheet(
#         '''
#         *{
#             font: 'Georgia';
#             border: 1px solid 'GREEN';
#             border-radius: 12px;
#             font-size: 30px;
#             color: 'white';
#             padding: 5px ;
#             margin: 0px 300px;
#             }
#         *:hover{
#                 background:'green';
#                 color:'black';
#                 font-weight:1200;
#                 font-size: 35px;
#             }
#         '''
#     )
#
#     if placeholder_text == "Leaderboard":
#         btn.clicked.connect(leaderboard)
#     elif placeholder_text == "Settings":
#         btn.clicked.connect(settings)
#     elif placeholder_text == "Achievements":
#         btn.clicked.connect(achievements)
#     elif placeholder_text == "Instructions":
#         btn.clicked.connect(instructions)
#     else:
#         pass  # do nothing
#     return btn
#
#
# def settings():
#     print("Settings Frame")
#
#
# def leaderboard():
#     print("Leaderboard Frame")
#
#
# def achievements():
#     print("Achievement Frame")
#
#
# def instructions():
#     print("Instructions Frame")
#
#
# def menu():
#     # display Gamiccount menu logo
#     logo = QLabel()
#     logo.setPixmap(resize_image("main-logo.png", 500, 300))
#     logo.setAlignment(QtCore.Qt.AlignCenter)
#     logo.setStyleSheet('''
#             margin-top: 50px;
#             margin-bottom: 5px;
#     ''')
#     widgets["logos"].append(logo)
#
#     # button Widgets (Method 1)
#     btn_start = QPushButton("Start Gami-ccount")
#     btn_start.setCursor(QCursor(QtCore.Qt.PointingHandCursor))  # shows Pointing Hand cursor when hovering on button
#     btn_start.setStyleSheet(
#         '''
#         *{
#             font: 'Georgia';
#             border: 1px solid 'GREEN';
#             border-radius: 12px;
#             font-size: 30px;
#             color: 'white';
#             padding: 5px ;
#             margin: 0px 300px;
#             }
#         *:hover{
#                 background:'green';
#                 color:'yellow';
#                 font-weight:1200;
#                 font-size: 35px;
#             }
#         '''
#     )
#     # btn_start.clicked.connect(start_game)
#     widgets["buttons"].append(btn_start)
#
#     # ++++++++++++++++Test (Method 2)
#     btn_leaderboard = create_start_buttons("Leaderboard")
#     widgets["leaderboard_button"].append(btn_leaderboard)
#
#     btn_settings = create_start_buttons("Settings")
#     widgets["settings_button"].append(btn_settings)
#
#     btn_achievements = create_start_buttons("Achievements")
#     widgets["achievements_button"].append(btn_achievements)
#
#     btn_instructions = create_start_buttons("Instructions")
#     widgets["instructions_button"].append(btn_instructions)
#
#     # empty space in bottom
#     empty_space = QPushButton("")
#     empty_space.setStyleSheet(
#         '''
#             background: 'green';
#             margin-top: 100px;
#         ''')
#     empty_space.setMinimumHeight(200)
#     widgets["empty_space"].append(empty_space)
#
#     # place inside Global Variable Dictionary of Widgets
#     grid.addWidget(widgets["logos"][-1], 0, 0, 1, 2)
#     grid.addWidget(widgets["buttons"][-1], 1, 0, 1, 2)
#     grid.addWidget(widgets["leaderboard_button"][-1], 2, 0, 1, 2)
#     grid.addWidget(widgets["settings_button"][-1], 3, 0, 1, 2)
#     grid.addWidget(widgets["achievements_button"][-1], 4, 0, 1, 2)
#     grid.addWidget(widgets["instructions_button"][-1], 5, 0, 1, 2)
#     grid.addWidget(widgets["empty_space"][-1], 6, 0, 1, 2)
#
#
# # Run Unit
# menu()
#
# window.setLayout(grid)
#
# window.show()
# sys.exit(app.exec())  # terminate app

#===================================================
#Create DB for Python and SQL (SQLite Backend)
# import sqlite3
# import pandas as pd
#
# try:
#     # to connect to DB
#     connection = sqlite3.connect(("gta.db"))
# except Exception as e:
#     print(e)
#
# #creates cursor object
# cursor = connection.cursor()
#
# cursor.execute(
#     '''
#     CREATE TABLE GTA(
#     RELEASE_YEAR INTEGER,
#     RELEASE_GAME TEXT,
#     CITY TEXT
#     )
#         ''')
#
# release_list = [
#     (1997, "Grand Theft Auto", "state of New Guernsey"),
#     (1999, "Grand Theft Auto 2", "Anywhere, USA"),
#     (2001, "Grand Theft Auto III", "Liberty City"),
#     (2002, "Grand Theft Auto: Vice City", "Vice City"),
#     (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
#     (2008, "Grand Theft Auto IV", "Liberty City"),
#     (2013, "Grand Theft Auto V", "Los Santos")
# ]
#
# #(?,?,?) is a template for a tuple
# cursor.executemany('''INSERT INTO GTA VALUES (?,?,?)''',release_list)
#
# for row in cursor.execute("SELECT * FROM GTA WHERE RELEASE_YEAR = 2002"):
#     print(row)
#
# cursor.execute("select * from gta where city =:c",{"c":"Liberty City"})
# gta_search = cursor.fetchall()
# print(gta_search)
#
# cursor.execute(
#     '''
#     CREATE TABLE cities(
#     gta_city text,
#     real_city text
#     )
#     '''
# )
#
# cursor.execute("INSERT INTO CITIES VALUES (?,?)",("Liberty City","New York"))
# cursor.execute("select * from cities where gta_city =:c",{"c":"Liberty City"})
#
# cities_search = cursor.fetchall()
# print(cities_search)
#
# print("===========================================")
# for i in gta_search:
#     ["New York" if value == "Liberty City" else value for value in i]
#
# #to disable connection
# connection.close()

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
    # df = pd.DataFrame(data["results"])
    df = pd.DataFrame(data)
    print(df.columns)
