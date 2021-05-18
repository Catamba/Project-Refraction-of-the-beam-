import sys


from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
import math


SCREEN_SIZE = [1200, 700]
SCREEN_SIZE2 = [500, 500]



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 120, *SCREEN_SIZE)
        self.setWindowTitle('Шестая программа')
        # # рисование 1000, 600
        # fon1_color = 'green'
        # width = 500
        # height = 500
        # draw = ImageDraw.Draw(im)
        # draw.polygon(((0, 0), (500, 0), (500, 250), (0, 250),), fon1_color)
        #
        # draw.line((0, 250, 500, 250), fill=('white'), width=3)
        # draw.line((250, 0, 250, 500), fill=('white'), width=3)
        ###################################################################################
        new_image = Image.new("RGB", (500, 500), ('green'))  # размер холста
        self.orig_image = new_image
        self.curr_image = new_image
        self.degree = 0

        draw = ImageDraw.Draw(self.curr_image)

        self.dd = 0
        if self.dd:
            draw.line((0, 0, 250, 250), fill=('red'), width=3)



        draw.line((0, 250, 500, 250), fill=('white'), width=3)
        draw.line((250, 0, 250, 500), fill=('white'), width=3)


        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)

        self.image = QLabel(self)
        self.image.move(15, 15)
        self.image.resize(500, 500)   # ограничение отображаемого размера
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)


        ###################################################################################

        # текс кнопки начать
        self.label_vivod = QLabel(self)
        self.label_vivod.setText("Нажмите кнопку (                            ) что бы программа отрисовала отражение луча")
        self.label_vivod.move(600, 180)

        self.label_a = QLabel(self)
        self.label_a.setText("a")
        self.label_a.move(245, 210)

        self.label_b = QLabel(self)
        self.label_b.setText("b")
        self.label_b.move(260, 269)


        # sreda1
        self.label_sreda1 = QLabel(self)
        self.label_sreda1.setText("Оптическая плотность первой среды ->")
        self.label_sreda1.move(600, 50)
        self.name_input_sreda1 = QLineEdit(self)
        self.name_input_sreda1.move(810, 50)

        #sreda2
        self.label_sreda2 = QLabel(self)
        self.label_sreda2.setText("Оптическая плотность второй среды ->")
        self.label_sreda2.move(600, 90)
        self.name_input_sreda2 = QLineEdit(self)
        self.name_input_sreda2.move(810, 90)

        # угол(angle)
        self.label_angle = QLabel(self)
        self.label_angle.setText("Задайте угол (X) падения луча     ->")
        self.label_angle.move(610, 130)
        self.name_input_angle = QLineEdit(self)
        self.name_input_angle.move(800, 130)

        # кнопки

        # начать
        self.btn_go = QPushButton('Начать', self)
        self.btn_go.resize(self.btn_go.sizeHint())
        self.btn_go.move(705, 175)
        self.btn_go.clicked.connect(self.Start)

        # тест
        self.btn_test = QPushButton('Тест', self)
        self.btn_test.resize(self.btn_test.sizeHint())
        self.btn_test.move(600, 300)
        self.btn_test.clicked.connect(self.test)


    def test(self):
        a = 20
        a_prel = 90 - a
        sr1 = 1
        sr2 = 1.6
        a_rad = a_prel*math.pi/180
        n = sr1 / sr2

        cos = str(math.cos(a_rad))[0:3]
        sin = str(math.sin(a_rad))[0:3]

        cos_x = float(cos) * 250
        sin_y = float(sin) * 250

        sin_1 = float(math.sin(a_rad))
        sin_2 = sin_1 / n


        self.curr_image = self.orig_image.copy()
        draw = ImageDraw.Draw(self.orig_image)
        draw.line((int(cos_x), int(sin_y), 250, 250), fill=('red'), width=3)




        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)





    def Start(self):
        sreda1_text = self.name_input_sreda1.text()  # Получим текст из поля ввода
        sreda2_text = self.name_input_sreda2.text()  # Получим текст из поля ввода
        angle_text = self.name_input_angle.text

        self.label_vivod.setText(f"Привет, {int(sreda1_text) + int(sreda2_text)}, {sreda2_text}")
        self.label_test.setText(f"angle_text")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())