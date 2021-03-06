import PySimpleGUI as sg
import webbrowser, os
import audoiFiles
import logg as Log


def popup_selectFolder(message):
    return sg.popup_get_folder(message)


def run(pathFromDir,pathDirInput = ""):


    layout = [[sg.Text('Выберите путь, где лежат файлы:',background_color="#1E1E1E")], 
            [sg.InputText(pathFromDir,key="fromDir",background_color="#3C3C3C",text_color="#D2D2D2",justification='center'),sg.FolderBrowse("Выбрать",button_color="#252526")],
            [sg.Text('Выберите путь к каталогу, где будет сортировака:',background_color="#1E1E1E")], 
            [sg.InputText(pathDirInput,key="pathDir",background_color="#3C3C3C",text_color="#D2D2D2",justification='center'),sg.FolderBrowse("Выбрать",button_color="#252526")],
            [sg.Checkbox("Неизвестные исполнители",background_color="#1E1E1E",key="checkAutor")],
            [sg.Button('Начать',size=(10,1),button_color="#006B04",mouseover_colors="#1E1E1E",border_width=0)],
            [sg.Button('Закрыть',size=(10,1),button_color="#920000",mouseover_colors="#1E1E1E",border_width=0),sg.Text('github.com/Zunder45/MicroSortingFileMP3_Py',key="link",enable_events=True,background_color="#1E1E1E",text_color="#D2D2D2")]]


    window = sg.Window('MicroSortingFileMP3 gui', layout, size=(450,220),background_color="#1E1E1E")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Закрыть': 
            break
        if event == 'Начать':
            if values["pathDir"] != "":
                

                if audoiFiles.scan(values["fromDir"], values["checkAutor"]):
            
                    if sg.popup_yes_no('Продолжить?') == "Yes":
                    
                        audoiFiles.sort(values["pathDir"])
                        
                        Log.pop("OK  " + values["pathDir"],"o")
                    
                    else:
                        audoiFiles.clear()
        
        if event == "link":
            webbrowser.open('https://github.com/Zunder45/MicroSortingFileMP3_Py.git')
                

    window.close() 


if __name__ == "__main__":
    path = os.getcwd()
    run(path,path)
