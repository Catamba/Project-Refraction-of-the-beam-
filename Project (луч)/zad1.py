import sys


from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt


SCREEN_SIZE = [1000, 830]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 60, *SCREEN_SIZE)
        self.setWindowTitle('Шестая программа')


        # рисование 1000, 600
        fon1_color = '#0a0a0a'
        width = 1000
        height = 800
        im = Image.new("RGB", SCREEN_SIZE, ('#0a0a0a'))
        draw = ImageDraw.Draw(im)
        draw.line((0, 400, 1000, 400), fill=('white'), width=5)
        draw.line((0, 420, 1000, 420), fill=('red'), width=3)

        draw.polygon(((0, 0), (1000, 0),(1000, 400),(0, 400),), fon1_color)







        self.orig_image = im
        self.curr_image = im
        self.a = ImageQt(self.orig_image)
        self.pixmap = QPixmap.fromImage(self.a)

        self.image = QLabel(self)
        self.image.move(0, 230)
        self.image.resize(1000, 600)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

        # текс кнопки начать
        self.label_vivod = QLabel(self)
        self.label_vivod.setText("Нажмите кнопку (                            ) что бы программа отрисовала отражение луча")
        self.label_vivod.move(10, 180)

        self.label_test = QLabel(self)
        self.label_test.setText("00000")
        self.label_test.move(700, 180)


        # sreda1
        self.label_sreda1 = QLabel(self)
        self.label_sreda1.setText("Задайте плотность первой среды ->")
        self.label_sreda1.move(10, 50)
        self.name_input_sreda1 = QLineEdit(self)
        self.name_input_sreda1.move(200, 50)

        #sreda2
        self.label_sreda2 = QLabel(self)
        self.label_sreda2.setText("Задайте плотность второй среды ->")
        self.label_sreda2.move(10, 90)
        self.name_input_sreda2 = QLineEdit(self)
        self.name_input_sreda2.move(200, 90)

        # угол(angle)
        self.label_angle = QLabel(self)
        self.label_angle.setText("Задайте угол (X) падения луча     ->")
        self.label_angle.move(10, 130)
        self.name_input_angle = QLineEdit(self)
        self.name_input_angle.move(200, 130)

        # кнопки

        # начать
        self.btn = QPushButton('Начать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(105, 175)
        self.btn.clicked.connect(self.Start)




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