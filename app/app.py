from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget
from .BotTableTab import BotTable

class MyApp(QTabWidget):
    def __init__(self):
        super().__init__()

        # Crear las pestañas
        self.tabs = QTabWidget()

        # Crear las pestañas
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        # Añadir las pestañas al widget
        self.tabs.addTab(self.tab1, "Markets")
        self.tabs.addTab(self.tab2, "Bots")

        # Crear Layout principal y añadir el widget de pestañas
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.tabs)

        # Configurar contenido de pestañas
        self.tab1.setLayout(QVBoxLayout())
        self.tab1.layout().addWidget(QWidget())

        self.tab2.setLayout(QVBoxLayout())
        self.tab2.layout().addWidget(BotTable())

        # Configurar la ventana
        self.setWindowTitle("Quantitative Machine Engine")
        self.resize(800, 600)

