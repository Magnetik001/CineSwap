import sys, os

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

import enter
import register

class AuthenticationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # Экран
        self.setWindowTitle("CineSwap")
        self.resize(700, 500)

        screen = QApplication.primaryScreen().availableGeometry()
        self.move(
            (screen.width() - self.width()) // 2,
            (screen.height() - self.height()) // 2
        )

        layout = QGridLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(60, 70, 60, 50)
        self.setLayout(layout)

        # Логотип
        logo_label = QLabel()
        logo_image = QPixmap("logo.jpg")
        scaled = logo_image.scaled(
            140, 140,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        logo_label.setPixmap(scaled)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo_label, 0, 0, 1, 2)

        # Название
        title_label = QLabel("CineSwap")
        title_font = QFont()
        title_font.setPointSize(32)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-top: 10px;")
        layout.addWidget(title_label, 1, 0, 1, 2)

        # Слоган
        slogan_label = QLabel("Обменивайтесь впечатлениями от фильмов")
        slogan_font = QFont()
        slogan_font.setPointSize(14)
        slogan_label.setFont(slogan_font)
        slogan_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        slogan_label.setStyleSheet("color: #7f8c8d; margin-bottom: 20px;")
        layout.addWidget(slogan_label, 2, 0, 1, 2)

        # Шрифты
        button_font = QFont()
        button_font.setPointSize(14)
        button_font.setBold(True)

        button_style = """
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 14px 30px;
                border-radius: 12px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QPushButton:pressed {
                background-color: #a93226;
            }
        """

        # Кнопка входа
        self.enter_btn = QPushButton("Войти")
        self.enter_btn.setFont(button_font)
        self.enter_btn.setStyleSheet(button_style)
        layout.addWidget(self.enter_btn, 3, 0, Qt.AlignmentFlag.AlignCenter)

        # Кнопка регистрации
        self.register_btn = QPushButton("Регистрация")
        self.register_btn.setFont(button_font)
        self.register_btn.setStyleSheet(button_style)
        layout.addWidget(self.register_btn, 3, 1, Qt.AlignmentFlag.AlignCenter)

        # Логика кнопок
        self.enter_btn.clicked.connect(self.open_enter_window)
        self.register_btn.clicked.connect(self.open_register_window)

    def open_enter_window(self):
        self.enterWin = enter.EnterWindow()
        self.enterWin.show()
        self.close()

    def open_register_window(self):
        self.registerWin = register.RegisterWindows()
        self.registerWin.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QWidget {
            background-color: white;
            font-family: "Segoe UI", "Roboto", sans-serif;
        }
    """)
    win = AuthenticationWindow()
    win.show()
    sys.exit(app.exec())