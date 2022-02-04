from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

app = QApplication(sys.argv)
wind = QWidget()

names = {}
lsprite_base = {}

class oilwin():
    def __init__(self, res_x, res_y, title, resiz, icon) -> None:
        self.res_x = res_x
        self.res_y = res_y
        self.title = title
        self.resize = resiz
        self.icon = icon

    def draw_win(self):
        global app, wind
        if self.icon != None:
            wind.setWindowIcon(QIcon(self.icon))

        if self.title != '':
            wind.setWindowTitle(self.title)
        elif self.title == '':
            wind.setWindowTitle('oilukla window')

        if self.resize == True:
            wind.setFixedSize(self.res_x, self.res_y)

        wind.resize(self.res_x, self.res_y)

    def resize_win(self, nres_x, nres_y):
        global wind
        if self.resize == False:
            wind.resize(nres_x, nres_y)
        elif self.resize == True:
            wind.setFixedSize(nres_x, nres_y)

    def rename_win(self, ntitle):
        global wind
        wind.setWindowTitle(ntitle)

    def ena_window(self):
        sys.exit(app.exec())

    def draw_obj(self):
        wind.show()


class oilentity(): #, img_way, res_x, res_y, phys, add_script
    def __init__(self, name, sprite, res_x, res_y) -> None:
        self.name = name
        self.sprite = sprite
        self.res_x = res_x
        self.res_y = res_y

        globals()['lsprite'] = self.sprite
        globals()['res_x'] = self.res_x
        globals()['res_y'] = self.res_y

    def add_object(self):
        main_dict = {}
        main_dict = dict({'sprite':lsprite, 'res_x':res_x, 'res_y':res_y})

        with open(self.name + '.data', 'wb') as d_file:
            d_file.write(str(main_dict).encode('utf-8'))

        globals()['llabel'] = QLabel()

        tsprite = QPixmap(lsprite)

        llabel.setPixmap(tsprite)
        llabel.resize(16, 16)

        print(llabel)
        

    
        
        
        
