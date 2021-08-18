# PyGUI > SimpleGUI.py

import PySimpleGUI as sg

layout = [[sg.Text("Hello from @lyushher \n Say Hello; ")], [sg.Button("Hello!")]]

window = sg.Window("Hello World", layout)

while True:
    event, values = window.read()
    if event == "Hello!" or event == sg.WIN_CLOSED:
        break

window.close()
