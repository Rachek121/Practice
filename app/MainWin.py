from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon, QPixmap
from app.SelectCarWin import CarWindow
from app.AddClientWin import AddClientWindow
from app.AddCarWin import AddCarWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('GAIJIN')
        self.resize(300, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon(''))

        wid = QWidget()
        main_vl = QVBoxLayout()

        self.label_image = QLabel(self)
        pixmap = QPixmap("")
        self.label_image.setPixmap(pixmap)
        self.label_image.setScaledContents(True)
        self.label_image.setFixedSize(240, 240)
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_vl.addWidget(self.label_image)
        main_vl.addStretch()

        self.view_car_btn = QPushButton('Просмотреть машины')
        self.add_client_btn = QPushButton('Добавить клиента')
        self.add_car_btn = QPushButton('Добавить машину')
        self.cls_btn = QPushButton('Выйти')


        main_vl.addStretch()

        main_vl.addWidget(self.view_car_btn)
        main_vl.addWidget(self.add_client_btn)
        main_vl.addWidget(self.add_car_btn)
        main_vl.addWidget(self.cls_btn)

        main_vl.addStretch()

        wid.setLayout(main_vl)
        self.setCentralWidget(wid)

        self.view_car_btn.clicked.connect(self.show_view_car_btn)
        self.add_client_btn.clicked.connect(self.show_add_client_win)
        self.add_car_btn.clicked.connect(self.show_add_car_win)
        self.cls_btn.clicked.connect(self.close)

    def show_view_car_btn(self):
        self.win_view_car = CarWindow()
        self.win_view_car.show()

    def show_add_client_win(self):
        self.win_add_client = AddClientWindow()
        self.win_add_client.show()

    def show_add_car_win(self):
        self.win_add_car = AddCarWindow()
        self.win_add_car.show()

    def closeEvent(self, event):
        QApplication.quit()
