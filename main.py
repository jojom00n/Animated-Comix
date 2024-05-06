import sys

from PySide6.QtWidgets import QWidget
from PySide6 import QtWidgets

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtSql import QSqlTableModel

from ui_main import Ui_MainWindow
from ui_main import MouseTracker

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QPointF


# Класс главного окна интерфейса программы
class Comix(QMainWindow):
    def __init__(self): # Метод инициализации окна
        super(Comix, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Создаем экземпляр класса MouseTracker с передачей метки в качестве аргумента
        self.tracker = MouseTracker(self.ui.main_work_space, self.ui.label_position)
        self.tracker.positionChanged.connect(self.on_positionChanged)


    # Метод вывода в правом нижнем углу экрана координат курсора
    @QtCore.Slot(QtCore.QPoint)
    def on_positionChanged(self, pos):
        # Меняем текст метки с текущими координатами курсора
        self.ui.label_position.setText("X: %d, Y: %d" % (pos.x(), pos.y()))
        self.ui.label_position.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Comix()
    window.show()

    sys.exit(app.exec())