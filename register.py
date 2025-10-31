from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

import menu
import main


class RegisterWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("CineSwap — Регистрация")
        self.resize(700, 500)

        screen = QApplication.primaryScreen().availableGeometry()
        self.move(
            (screen.width() - self.width()) // 2,
            (screen.height() - self.height()) // 2
        )

        layout = QGridLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(80, 80, 80, 50)
        self.setLayout(layout)

        # Шрифты
        font_title = QFont()
        font_title.setPointSize(24)
        font_title.setBold(True)

        font_label = QFont()
        font_label.setPointSize(14)

        # Заголовок
        title_label = QLabel("Создайте аккаунт")
        title_label.setFont(font_title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title_label, 0, 0, 1, 2)  # строка 0

        # Логин
        login_label = QLabel("Логин")
        login_label.setFont(font_label)
        login_label.setStyleSheet("color: #2c3e50;")
        layout.addWidget(login_label, 1, 0, Qt.AlignmentFlag.AlignVCenter)

        self.login_edit = QLineEdit()
        self.login_edit.setFont(font_label)
        self.login_edit.setPlaceholderText("Введите логин")
        self.login_edit.setStyleSheet("background: white; color: black; border: 1px solid #ccc;")
        layout.addWidget(self.login_edit, 1, 1)

        # Пароль
        password_label = QLabel("Пароль")
        password_label.setFont(font_label)
        password_label.setStyleSheet("color: #2c3e50;")
        layout.addWidget(password_label, 2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.password_edit = QLineEdit()
        self.password_edit.setFont(font_label)
        self.password_edit.setPlaceholderText("Введите пароль")
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_edit.setStyleSheet("background: white; color: black; border: 1px solid #ccc;")
        layout.addWidget(self.password_edit, 2, 1)

        # Кнопка назад
        self.back_btn = QPushButton("← Назад", self)
        self.back_btn.setFont(QFont("Segoe UI", 11))
        self.back_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #2c3e50;
                border: none;
                padding: 6px 10px;
            }
            QPushButton:hover {
                color: #e74c3c;
                background-color: rgba(231, 76, 60, 0.1);
                border-radius: 4px;
            }
        """)
        self.back_btn.move(15, 15)

        # Кнопка входа
        self.enter_btn = QPushButton("Войти")
        self.enter_btn.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        self.enter_btn.setStyleSheet("""
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
        """)
        layout.addWidget(self.enter_btn, 3, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Предупреждающая надпись
        self.help_label = QLabel()
        self.help_label.setFont(font_label)
        self.help_label.setStyleSheet("color: #e74c3c;")
        layout.addWidget(self.help_label, 4, 0, 1, 4, Qt.AlignmentFlag.AlignVCenter)

        # Логика кнопок
        self.enter_btn.clicked.connect(self.check_enter)
        self.back_btn.clicked.connect(self.back)

    def check_enter(self):
        if self.login_edit.text() == "Magnetik":
            self.help_label.setText("Такой логин уже существует")
        elif len(self.password_edit.text()) < 6:
            self.help_label.setText("Символов в пароле должно быть 6 или больше")
        else:
            self.menuWin = menu.MenuWindow()
            self.menuWin.show()
            self.close()

    def back(self):
        self.mainWin = main.AuthenticationWindow()
        self.mainWin.show()
        self.close()
