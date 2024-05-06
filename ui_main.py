

from PySide6.QtCore import (QCoreApplication, QPointF, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QMimeData)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget, QFileDialog)
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QDrag
from PySide6.QtWidgets import QMainWindow, QSlider
from PySide6.QtWidgets import QScrollArea







# Класс, который имеют фотографии, добавляемые в рабочую область программы
class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.old_pos = None


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.pos()



    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return

        delta = event.pos() - self.old_pos
        # Устанавливаем новое положение виджета
        self.move(self.pos() + delta)

    def mouseReleaseEvent(self, event):
        print('x: {0}, y: {1}'.format(self.pos().x(), self.pos().y()))

    def setPixmap(self, image):
        super().setPixmap(image)

    def event(self, event):
        if event.type() == QtCore.QEvent.MouseMove and event.buttons() == Qt.NoButton:
            event.ignore()  # Пропустить событие мыши, если нет нажатых кнопок
            return True
        return super().event(event)

# Класс для отслеживание курсора мыши
class MouseTracker(QtCore.QObject):
    positionChanged = QtCore.Signal(QtCore.QPoint)

    def __init__(self, widget, label):
        super().__init__(widget)
        self._widget = widget
        self._label = label  # Сохраняем ссылку на метку
        self.widget.setMouseTracking(True)
        self.widget.installEventFilter(self)

    @property
    def widget(self):
        return self._widget

    def eventFilter(self, o, e):
        if o is self.widget and e.type() == QtCore.QEvent.MouseMove:
            mouse_event = QtGui.QMouseEvent(e)
            pos = mouse_event.pos()
            # Обновляем текст метки с текущими координатами курсора
            self._label.setText("X: %d, Y: %d" % (pos.x(), pos.y()))
            return True  # Возвращаем True, чтобы предотвратить передачу события дальше
        return super().eventFilter(o, e)

# Окно настройек проекта
class NewWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Настройки проекта")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.label = QLabel("This is a new window")
        layout.addWidget(self.label)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(868, 582)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"background-color: rgb(58, 58, 58);")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 5, 1, -1)
        self.btn_project = QPushButton(self.groupBox)
        self.btn_project.setObjectName(u"btn_project")
        self.btn_project.setEnabled(True)
        self.btn_project.setMaximumSize(QSize(200, 50))
        self.btn_project.setMinimumSize(QSize(70, 20))
        self.btn_project.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(106, 106, 106);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(130, 130, 130);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(180, 180, 180);\n"
"}")
        self.btn_project.clicked.connect(self.open_new_window)

        self.horizontalLayout.addWidget(self.btn_project)

        self.btn_file = QPushButton(self.groupBox)
        self.btn_file.setObjectName(u"btn_file")
        self.btn_file.setMaximumSize(QSize(200, 50))
        self.btn_file.setMinimumSize(QSize(70, 20))
        self.btn_file.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(106, 106, 106);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(130, 130, 130);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(180, 180, 180);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_file)

        self.btn_edit = QPushButton(self.groupBox)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setMaximumSize(QSize(200, 50))
        self.btn_edit.setMinimumSize(QSize(70, 20))
        self.btn_edit.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(106, 106, 106);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(130, 130, 130);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(180, 180, 180);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_edit)

        self.btn_view = QPushButton(self.groupBox)
        self.btn_view.setObjectName(u"btn_view")
        self.btn_view.setMaximumSize(QSize(200, 50))
        self.btn_view.setMinimumSize(QSize(70, 20))
        self.btn_view.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(106, 106, 106);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(130, 130, 130);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(180, 180, 180);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_view)

        self.btn_panel_edit = QPushButton(self.groupBox)
        self.btn_panel_edit.setMaximumSize(QSize(200, 50))
        self.btn_panel_edit.setMinimumSize(QSize(130, 20))
        self.btn_panel_edit.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(106, 106, 106);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(130, 130, 130);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(180, 180, 180);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_panel_edit)

        self.btn_animation = QPushButton(self.groupBox)
        self.btn_animation.setObjectName(u"btn_animation")
        self.btn_animation.setMaximumSize(QSize(200, 50))
        self.btn_animation.setMinimumSize(QSize(100, 20))
        self.btn_animation.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(106, 106, 106);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(130, 130, 130);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(180, 180, 180);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_animation)
        self.horizontalLayout.addStretch(5)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(0, 0))
        self.frame1.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.frame1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line_search = QLineEdit(self.frame1)
        self.line_search.setObjectName(u"line_search")

        self.verticalLayout_3.addWidget(self.line_search)

        self.search_list = QTableWidget(self.frame1)
        self.search_list.setObjectName(u"search_list")

        self.verticalLayout_3.addWidget(self.search_list)


        self.horizontalLayout_2.addWidget(self.frame1)

        self.work_space = QWidget(self.frame)
        self.work_space.setObjectName(u"work_space")
        self.work_space.setMinimumSize(QSize(400, 0))
        self.work_space.setMouseTracking(True)
        # Включаем прием перетаскиваемых файлов

        self.verticalLayout_5 = QVBoxLayout(self.work_space)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.main_work_space = QWidget(self.work_space)
        self.main_work_space.setLayout(QVBoxLayout())
        self.main_work_space.setObjectName(u"main_work_space")
        self.main_work_space.setMinimumSize(QSize(200, 300))
        self.main_work_space.setMouseTracking(True)
        self.main_work_space.setStyleSheet(u"border: 1px solid rgb(0, 170, 255);")
        # Включаем прием перетаскиваемых файлов
        self.main_work_space.setAcceptDrops(True)

        self.main_work_space.setFixedSize(QSize(300, 1000))

        self.photoViewer = ImageLabel()
        self.photoViewer.setStyleSheet(u"border: 0px solid rgb(0, 170, 255);")
        self.main_work_space.layout().addWidget(self.photoViewer)

        # Создаем виджет с прокруткой
        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setWidgetResizable(True)  # Разрешаем изменение размеров содержимого


        # Создаем main_work_space и устанавливаем его в виджет с прокруткой
        self.scroll_area.setWidget(self.main_work_space)



        self.verticalLayout_5.addWidget(self.scroll_area)





        # Устанавливаем layout для centralwidget
        layout = QVBoxLayout(self.centralwidget)

        # Устанавливаем политику размеров для scroll_area
        self.scroll_area.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)




        self.horizontalLayout_2.addWidget(self.work_space)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.object_properties = QLabel(self.widget)
        self.object_properties.setObjectName(u"object_properties")
        self.object_properties.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.object_properties)

        self.properties = QGridLayout()
        self.properties.setObjectName(u"properties")
        self.pushButton_16 = QPushButton(self.widget)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.properties.addWidget(self.pushButton_16, 1, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.widget)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.properties.addWidget(self.pushButton_15, 0, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.widget)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.properties.addWidget(self.pushButton_13, 0, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.widget)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.properties.addWidget(self.pushButton_14, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.properties)

        self.btn_object_transform = QPushButton(self.widget)
        self.btn_object_transform.setObjectName(u"btn_object_transform")

        self.verticalLayout_2.addWidget(self.btn_object_transform)

        self.btn_fast_animation = QPushButton(self.widget)
        self.btn_fast_animation.setObjectName(u"btn_fast_animation")

        self.verticalLayout_2.addWidget(self.btn_fast_animation)

        self.layers_tree = QTreeWidget(self.widget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"\u0421\u043b\u043e\u0438");
        self.layers_tree.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.layers_tree)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.layers_tree)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(self.layers_tree)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem4 = QTreeWidgetItem(self.layers_tree)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(self.layers_tree)
        __qtreewidgetitem5 = QTreeWidgetItem(self.layers_tree)
        QTreeWidgetItem(__qtreewidgetitem5)
        self.layers_tree.setObjectName(u"layers_tree")

        self.verticalLayout_2.addWidget(self.layers_tree)

        # Создаем метку для отображения координат
        self.label_position = QLabel(self.widget)
        self.label_position.setAlignment(QtCore.Qt.AlignRight)

        self.label_position.setStyleSheet("background-color: white; border: 1px solid black")  # Применяем стили

        self.verticalLayout_2.addWidget(self.label_position)


        self.horizontalLayout_2.addWidget(self.widget)

        self.work_space.raise_()
        self.frame.raise_()

        self.verticalLayout_4.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # Connect drag and drop events
        self.main_work_space.dragEnterEvent = self.drag_enter_event
        self.main_work_space.dropEvent = self.drop_event



    # Ваш метод для открытия нового окна
    def open_new_window(self):
        self.new_window = project_edit_window(self)  # Передача ссылки на экземпляр Ui_MainWindow
        self.new_window.setupUi(self.new_window)
        self.new_window.show()

    def drag_enter_event(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def drop_event(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                self.add_image_label(file_path)
        else:
            event.ignore()
    # setupUi
    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))

    def add_image_label(self, file_path):
        new_image_label = ImageLabel()
        new_image_label.setStyleSheet(u"border: 0px solid rgb(0, 170, 255);")
        pixmap = QPixmap(file_path)
        scaled_pixmap = pixmap.scaled(self.main_work_space.size(), Qt.KeepAspectRatio)
        new_image_label.setPixmap(scaled_pixmap)
        # Настройте новый ImageLabel по вашему усмотрению
        # Затем добавьте его в ваш контейнер main_work_space
        self.main_work_space.layout().addWidget(new_image_label)
        # Добавьте новый ImageLabel в список
        self.image_labels.append(new_image_label)

        # Создаем экземпляр класса MouseTracker и передаем новый ImageLabel и метку для отображения координат
        tracker = MouseTracker(new_image_label, self.label_position)

        # Добавляем новый экземпляр MouseTracker в список
        self.mouse_trackers.append(tracker)




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_project.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442", None))
        self.btn_file.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_view.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434", None))
        self.btn_panel_edit.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043d\u0435\u043b\u044c \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.btn_animation.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0438\u043c\u0430\u0446\u0438\u044f", None))
        self.object_properties.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"1000 px", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"100 px", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"300 px", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"100 px", None))
        self.btn_object_transform.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u043d\u0441\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.btn_fast_animation.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u0430\u044f \u0430\u043d\u0438\u043c\u0430\u0446\u0438\u044f", None))

        __sortingEnabled = self.layers_tree.isSortingEnabled()
        self.layers_tree.setSortingEnabled(False)
        ___qtreewidgetitem = self.layers_tree.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 1", None));
        ___qtreewidgetitem1 = ___qtreewidgetitem.child(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 1", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem.child(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 2", None));
        ___qtreewidgetitem3 = self.layers_tree.topLevelItem(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 2", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem3.child(0)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 1", None));
        ___qtreewidgetitem5 = self.layers_tree.topLevelItem(2)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 3", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 1", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem5.child(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 2", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem5.child(2)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 3", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem5.child(3)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 4", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem5.child(4)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 5", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem5.child(5)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 6", None));
        ___qtreewidgetitem12 = self.layers_tree.topLevelItem(3)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 4", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem12.child(0)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 1", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem12.child(1)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 2", None));
        ___qtreewidgetitem15 = self.layers_tree.topLevelItem(4)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 5", None));
        ___qtreewidgetitem16 = self.layers_tree.topLevelItem(5)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 6", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem16.child(0)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439 1", None));
        self.layers_tree.setSortingEnabled(__sortingEnabled)

    # retranslateUi

class project_edit_window(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # Сохраняем ссылку на экземпляр Ui_MainWindow
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(1000, 200))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.height = QLabel(self.centralwidget)
        self.height.setObjectName(u"height")

        self.gridLayout.addWidget(self.height, 0, 0, 1, 1)

        self.slider_height = QSlider(self.centralwidget)
        self.slider_height.setObjectName(u"slider_height")
        self.slider_height.setMinimum(200)
        self.slider_height.setMaximum(10000)
        self.slider_height.setSingleStep(10)
        self.slider_height.setSliderPosition(1000)
        self.slider_height.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_height, 0, 1, 1, 1)

        self.line_edit_height = QLineEdit(self.centralwidget)
        self.line_edit_height.setObjectName(u"line_edit_height")

        self.gridLayout.addWidget(self.line_edit_height, 0, 2, 1, 1)

        self.width = QLabel(self.centralwidget)
        self.width.setObjectName(u"width")

        self.gridLayout.addWidget(self.width, 1, 0, 1, 1)

        self.slider_width = QSlider(self.centralwidget)
        self.slider_width.setObjectName(u"slider_width")
        self.slider_width.setMinimum(100)
        self.slider_width.setMaximum(1000)
        self.slider_width.setSingleStep(10)
        self.slider_width.setSliderPosition(300)
        self.slider_width.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_width, 1, 1, 1, 1)

        self.line_edit_width = QLineEdit(self.centralwidget)
        self.line_edit_width.setObjectName(u"line_edit_width")

        self.gridLayout.addWidget(self.line_edit_width, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.btn_confirm_size_project = QPushButton(self.centralwidget)
        self.btn_confirm_size_project.setObjectName(u"btn_confirm_size_project")

        self.btn_confirm_size_project.clicked.connect(self.apply_size_and_close)

        self.horizontalLayout.addWidget(self.btn_confirm_size_project)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        # Подключаем сигнал clicked кнопки pushButton_2 к методу close_window
        self.pushButton_2.clicked.connect(self.close_window)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # Подключение сигналов и слотов для сохранения и обновления значений
        self.slider_height.valueChanged.connect(self.update_line_edit_height)
        self.line_edit_height.editingFinished.connect(self.update_slider_height)
        self.slider_width.valueChanged.connect(self.update_line_edit_width)
        self.line_edit_width.editingFinished.connect(self.update_slider_width)

    # Метод для закрытия окна
    def close_window(self):
        self.close()

    def apply_size_and_close(self):
        height = int(self.line_edit_height.text())
        width = int(self.line_edit_width.text())
        # Получаем доступ к элементам интерфейса через main_window
        self.main_window.main_work_space.setFixedSize(width, height)
        self.close()

    def update_line_edit_height(self, value):
        # Обновление значения QLineEdit при изменении QSlider
        self.line_edit_height.setText(str(value))

    def update_slider_height(self):
        # Обновление значения QSlider при завершении редактирования QLineEdit
        value = int(self.line_edit_height.text())
        self.slider_height.setValue(value)

    def update_line_edit_width(self, value):
        # Обновление значения QLineEdit при изменении QSlider
        self.line_edit_width.setText(str(value))

    def update_slider_width(self):
        # Обновление значения QSlider при завершении редактирования QLineEdit
        value = int(self.line_edit_width.text())
        self.slider_width.setValue(value)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u0430\u0437\u043c\u0435\u0440 \u043e\u043a\u043d\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.height.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430", None))
        self.line_edit_height.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.width.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.line_edit_width.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.btn_confirm_size_project.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi