import sys


from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton

SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')
        new_image = Image.new("RGB", (512, 200), ('red'))
        self.orig_image = new_image
        self.curr_image = new_image
        self.degree = 0

        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)


        self.image = QLabel(self)
        self.image.move(150, 30)
        self.image.resize(250, 250)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)
        self.button_R = QPushButton(self)
        self.button_R.move(20, 50)
        self.button_R.setText("R")
        self.button_R.clicked.connect(self.run)
        self.button_G = QPushButton(self)
        self.button_G.move(20, 100)
        self.button_G.setText("G")
        self.button_G.clicked.connect(self.run)
        self.button_B = QPushButton(self)
        self.button_B.move(20, 150)
        self.button_B.setText("B")
        self.button_B.clicked.connect(self.run)
        self.button_All = QPushButton(self)
        self.button_All.move(20, 200)
        self.button_All.setText("All")
        self.button_All.clicked.connect(self.run)
        self.button_RR = QPushButton(self)
        self.button_RR.move(20, 250)
        self.button_RR.resize(150, 30)
        self.button_RR.setText("Против часовой стрелки")
        self.button_RR.clicked.connect(self.rotate)
        self.button_RL = QPushButton(self)
        self.button_RL.move(200, 250)
        self.button_RL.resize(150, 30)
        self.button_RL.setText("По часовой стрелке")
        self.button_RL.clicked.connect(self.rotate)

    def run(self):
        self.curr_image = self.orig_image.copy()
        pixels = self.curr_image.load()
        x, y = self.curr_image.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if (self.sender().text() == 'R'):
                    pixels[i, j] = r, 0, 0
                elif (self.sender().text() == 'G'):
                    pixels[i, j] = 0, g, 0
                elif (self.sender().text() == 'B'):
                    pixels[i, j] = 0, 0, b
                else:
                    pass
        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
         # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def rotate(self):
        if self.sender().text() == 'Против часовой стрелки':
            self.degree += 90
            degree = 90
            if self.degree >= 360:
                self.degree -= 360
        elif self.sender().text() == 'По часовой стрелке':
            self.degree -= 90
            degree = -90
            if self.degree < 0:
                self.degree += 360
        self.curr_image = self.curr_image.rotate(degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())