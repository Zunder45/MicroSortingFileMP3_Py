import os
from gui import Gui



if __name__ == "__main__":
    gui = Gui()
    path = os.getcwd()
    gui.run(path,path)