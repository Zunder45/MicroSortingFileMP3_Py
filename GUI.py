import PySimpleGUI as sg
import Logg,AudoiFiles

def run():
    layout = [[sg.Text('Выберите путь к каталогу:'), sg.InputText(key="pathDir"),sg.FolderBrowse()],
              [sg.Button('Начать'), sg.Button('Выход')] ]


    window = sg.Window('microMP3 gui', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Выход': 
            break
        if event == 'Начать':
            if values["pathDir"] != "":
                AudoiFiles.sort(values["pathDir"],"g")
                
                

    window.close()