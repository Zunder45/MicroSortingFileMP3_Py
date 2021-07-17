import PySimpleGUI as sg
import tkinter
import webbrowser
import AudoiFiles
import Logg


def run(pathDirInput = ""):
    layout = [[sg.Text('Выберите путь к каталогу:',background_color="#1E1E1E")], 
            [sg.InputText(pathDirInput,key="pathDir",background_color="#3C3C3C",text_color="#D2D2D2",justification='center'),sg.FolderBrowse("Выбрать",button_color="#252526")],
              [sg.Button('Начать',button_color="#C7C507",mouseover_colors="#1E1E1E",border_width=0)],
              [sg.Text('github.com/Zunder45/microMP3_Py',key="link",enable_events=True,background_color="#1E1E1E",text_color="#D2D2D2")] ]


    window = sg.Window('microMP3 gui', layout, size=(500,150), element_justification='c',background_color="#1E1E1E")

    

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: 
            break
        if event == 'Начать':
            if values["pathDir"] != "":
                AudoiFiles.sort(values["pathDir"],"g")
        if event == "link":
            webbrowser.open('https://github.com/Zunder45/microMP3_Py')         
                

    window.close()
