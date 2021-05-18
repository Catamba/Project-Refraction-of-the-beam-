import sys

from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtCore import Qt
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton, QSlider, QLCDNumber, QLineEdit
# from scipy.misc import imsave

SCREEN_SIZE = [900, 640]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('PhotoRedactor by Саня')
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '',
                                            'Картинка (*.jpg);;Картинка (*.jpg);;Все файлы (*)')[0]
        self.copu_image = Image.open(fname)
        self.orig_image = Image.open(fname)
        self.curr_image = Image.open(fname)
        self.degree = 0

        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)

        self.image = QLabel(self)
        self.image.move(400, 50)
        self.image.resize(400, 400)
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
        self.button_RL.move(20, 300)
        self.button_RL.resize(150, 30)
        self.button_RL.setText("По часовой стрелке")
        self.button_RL.clicked.connect(self.rotate)
        # Надписи
        self.rgb = QLabel(self)
        self.rgb.setText('Фильтры')
        self.rgb.move(40, 20)
        self.rgb__ = QLabel(self)
        self.rgb__.setText('Расширенные Фильтры')
        self.rgb__.resize(150, 30)
        self.rgb__.move(200, 20)
        self.save_text = QLabel(self)
        self.save_text.setText('Напишите название для \nсохраняемого файла с изображением.')
        self.save_text.resize(300, 60)
        self.save_text.move(650, 200)
        self.save_info = QLabel(self)
        self.save_info.resize(300, 60)
        self.save_info.move(650, 350)
        self.blur_info = QLabel(self)
        self.blur_info.setText('Введите число\nчтобы блюр заработал.')
        self.blur_info.move(180, 535)
        self.blur_info.resize(300, 60)
        self.blur_warning = QLabel(self)
        self.blur_warning.resize(300, 30)
        self.blur_warning.move(20, 526)
        self.Start_Info = QLabel(self)
        self.Start_Info.setText('ВНИМАНИЕ  НЕ  ЗАБЫВАЙТЕ НАЖИМАТЬ КНОПКУ\n    ПРИМЕНИТЬ  ИЗМЕНЕНИЯ!!!!!!!')
        self.Start_Info.resize(260, 30)
        self.Start_Info.move(400, 20)
        self.temnota = QLabel(self)
        self.temnota.setText('= ЗАТЕМННЕНИЕ')
        self.temnota.resize(100, 30)
        self.temnota.move(120, 410)
        # кнопки
        self.button_1_negative = QPushButton(self)
        self.button_1_negative.move(20, 350)
        self.button_1_negative.resize(150, 30)
        self.button_1_negative.setText("Негатив")
        self.button_1_negative.clicked.connect(self.negative)
        self.button_2 = QPushButton(self)
        self.button_2.move(20, 450)
        self.button_2.resize(160, 30)
        self.button_2.setText("Mirror")
        self.button_2.clicked.connect(self.Mirror)
        self.button_3 = QPushButton(self)
        self.button_3.move(20, 500)
        self.button_3.resize(80, 30)
        self.button_3.setText('Пиксели BGR')
        self.button_3.clicked.connect(self.RGB_GBR_BRG_BGR)
        self.button_4 = QPushButton(self)
        self.button_4.move(20, 550)
        self.button_4.resize(50, 30)
        self.button_4.setText('Блюр')
        self.button_4.clicked.connect(self.blur)
        self.button_5 = QPushButton(self)
        self.button_5.move(20, 600)
        self.button_5.resize(50, 30)
        self.button_5.setText('Ч/Б')
        self.button_5.clicked.connect(self.Black_White_monochrom)
        self.button_6 = QPushButton(self)
        self.button_6.move(80, 600)
        self.button_6.resize(70, 30)
        self.button_6.setText('Монохром')
        self.button_6.clicked.connect(self.Black_White_monochrom)
        self.button_7 = QPushButton(self)
        self.button_7.move(100, 500)
        self.button_7.resize(80, 30)
        self.button_7.setText('Пиксели BRG')
        self.button_7.clicked.connect(self.RGB_GBR_BRG_BGR)
        self.button_8 = QPushButton(self)
        self.button_8.move(180, 500)
        self.button_8.resize(80, 30)
        self.button_8.setText('Пиксели GBR')
        self.button_8.clicked.connect(self.RGB_GBR_BRG_BGR)
        self.button_9 = QPushButton(self)
        self.button_9.move(260, 500)
        self.button_9.resize(80, 30)
        self.button_9.setText('Пиксели RGB')
        self.button_9.clicked.connect(self.RGB_GBR_BRG_BGR)
        self.button_mikser = QPushButton(self)
        self.button_mikser.move(180, 450)
        self.button_mikser.resize(160, 30)
        self.button_mikser.setText('Графический миксер')
        self.button_mikser.clicked.connect(self.mikser)
        self.button_OKEY = QPushButton(self)
        self.button_OKEY.move(180, 250)
        self.button_OKEY.resize(160, 160)
        self.button_OKEY.setText('Применить ИЗМЕНЕНИЕ')
        self.button_OKEY.clicked.connect(self.OKEY)
        self.button_delete = QPushButton(self)
        self.button_delete.move(650, 30)
        self.button_delete.resize(160, 50)
        self.button_delete.setText('Удалить ВСЕ ИЗМЕНЕНИЕ')
        self.button_delete.clicked.connect(self.delete)
        self.button_save = QPushButton(self)
        self.button_save.move(650, 300)
        self.button_save.resize(160, 50)
        self.button_save.setText('СОХРАНИТЬ ИЗОБРАЖЕНИЕ')
        self.button_save.clicked.connect(self.save)

        self.input_save = QLineEdit(self)
        self.input_save.move(650, 250)

        self.input_blur = QLineEdit(self)
        self.input_blur.move(70, 550)

        self.lcd_blackout = QLCDNumber(self)
        self.lcd_blackout.move(20, 410)

        self.lcdR = QLCDNumber(self)
        self.lcdR.move(250, 50)

        self.lcdG = QLCDNumber(self)
        self.lcdG.move(250, 100)

        self.lcdB = QLCDNumber(self)
        self.lcdB.move(250, 150)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(20, 380)
        self.slider.setMinimum(1)
        self.slider.setMaximum(10)
        self.slider.setValue(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(2)
        self.slider.valueChanged.connect(self.changedValue)
        # R
        self.slider_r = QSlider(Qt.Horizontal, self)
        self.slider_r.move(150, 50)
        self.slider_r.setMinimum(1)
        self.slider_r.setMaximum(255)
        self.slider_r.setValue(1)
        self.slider_r.setTickPosition(QSlider.NoTicks)
        self.slider_r.setTickInterval(50)
        self.slider_r.valueChanged.connect(self.changedValueR)
        # G
        self.slider_G = QSlider(Qt.Horizontal, self)
        self.slider_G.move(150, 100)
        self.slider_G.setMinimum(1)
        self.slider_G.setMaximum(255)
        self.slider_G.setValue(1)
        self.slider_G.setTickPosition(QSlider.NoTicks)
        self.slider_G.setTickInterval(50)
        self.slider_G.valueChanged.connect(self.changedValueG)
        # B
        self.slider_B = QSlider(Qt.Horizontal, self)
        self.slider_B.move(150, 150)
        self.slider_B.setMinimum(1)
        self.slider_B.setMaximum(255)
        self.slider_B.setValue(1)
        self.slider_B.setTickPosition(QSlider.NoTicks)
        self.slider_B.setTickInterval(50)
        self.slider_B.valueChanged.connect(self.changedValueB)

    def delete(self):
        self.orig_image = self.copu_image
        self.curr_image = self.copu_image
        self.curr_image = self.curr_image.rotate(0, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def save(self):
        name = self.input_save.text()
        if name != '':
            name2 = str(name) + str('.jpg')
            self.curr_image.save(name2)
            name3 = 'Изображение ' + name2 + ' успешно сохранено.'
            self.save_info.setText(name3)
        else:
            self.save_info.setText('Введите название!!!!')

    def OKEY(self):
        self.orig_image = self.curr_image

    def mikser(self):
        self.curr_image = self.orig_image.copy()
        im = self.curr_image
        pixels = im.load()
        x, y = im.size
        x2 = x // 2
        for i in range(x):
            for j in range(y):
                if i < x2:
                    pixels[i + x2, j] = pixels[i, j]
                else:
                    pixels[i - x2, j] = pixels[i, j]
        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def Black_White_monochrom(self):
        self.curr_image = self.orig_image.copy()
        if (self.sender().text() == 'Ч/Б'):
            self.curr_image = self.curr_image.convert('L')  # convert image to monochrome - this works

        elif (self.sender().text() == 'Монохром'):
            self.curr_image = self.curr_image.convert('1')  # convert image to black and white
        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def blur(self):
        rad = self.input_blur.text()
        if rad.isdigit():
            rad = int(self.input_blur.text())
            self.curr_image = self.orig_image.copy()
            im = self.curr_image
            self.curr_image = im.filter(ImageFilter.GaussianBlur(radius=rad))
            self.curr_image = self.curr_image.rotate(self.degree, expand=True)
            # python 3.8 garbage collection issue
            self.a = ImageQt(self.curr_image)
            self.pixmap = QPixmap.fromImage(self.a)
            self.image.setPixmap(self.pixmap)
            self.blur_warning.setText('')
        else:
            self.blur_warning.setText('Это НЕ число!!!!!!!!!  Пример:(1,3,15...)')

    def changedValue(self):
        size = str(self.slider.value())
        self.lcd_blackout.display(size)
        self.curr_image = self.orig_image.copy()
        pixels = self.curr_image.load()
        x, y = self.curr_image.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                rr = r // int(size)
                gg = g // int(size)
                bb = b // int(size)
                pixels[i, j] = rr, gg, bb
        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def changedValueR(self):
        size = str(self.slider_r.value())
        self.lcdR.display(size)
        rr = int(size)
        self.curr_image = self.orig_image.copy()
        pixels = self.curr_image.load()
        x, y = self.curr_image.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = rr, g, b
        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def changedValueG(self):
        size = str(self.slider_G.value())
        self.lcdG.display(size)
        gg = int(size)
        self.curr_image = self.orig_image.copy()
        pixels = self.curr_image.load()
        x, y = self.curr_image.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, gg, b
        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def changedValueB(self):
        size = str(self.slider_B.value())
        self.lcdB.display(size)
        bb = int(size)
        self.curr_image = self.orig_image.copy()
        pixels = self.curr_image.load()
        x, y = self.curr_image.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g, bb
        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

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

    def negative(self):
        # self.curr_image = self.orig_image.copy()
        pixels = self.curr_image.load()
        x, y = self.curr_image.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 255 - int(r), 255 - int(g), 255 - int(b)
        # self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def Mirror(self):
        #self.curr_image = self.orig_image.copy()
        im = self.curr_image
        pixels = im.load()  # список с пикселями
        x, y = im.size  # ширина (x) и высота (y) изображения
        for i in range(x):
            for j in range(y):
                pixels[i, j] = pixels[x - i - 1, j]

        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def RGB_GBR_BRG_BGR(self):
        self.curr_image = self.orig_image.copy()
        im = self.curr_image
        pixels = im.load()  # список с пикселями
        x, y = im.size  # ширина (x) и высота (y) изображения
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if (self.sender().text() == 'Пиксели BGR'):
                    rr = b
                    gg = g
                    bb = r
                elif (self.sender().text() == 'Пиксели BRG'):
                    rr = b
                    gg = r
                    bb = g
                elif (self.sender().text() == 'Пиксели GBR'):
                    rr = g
                    gg = b
                    bb = r
                elif (self.sender().text() == 'Пиксели RGB'):
                    rr = r
                    gg = g
                    bb = b
                pixels[i, j] = rr, gg, bb
        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())